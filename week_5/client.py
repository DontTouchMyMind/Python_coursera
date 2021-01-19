import socket
import time


class ClientError(BaseException):
    pass


class Client:

    def __init__(self, ip_addr, host, timeout=None):
        self._sock = self.connect(ip_addr, host, timeout)

    def _parse_response(self):
        return self._sock.recv(1024).decode('utf-8').split('\n')

    def get(self, metrics_name):
        data = f'get {metrics_name}\n'
        self._sock.send(data.encode('utf-8'))

        response = self._parse_response()

        if not self.response_is_valid(response):
            raise ClientError

        result = response[1:-2]
        answer = {}

        if metrics_name == '*':
            for i in result:
                lst = i.split()
                if lst[0] not in answer:
                    answer[lst[0]] = [(int(lst[2]), float(lst[1]))]
                else:
                    answer[lst[0]].append((int(lst[2]), float(lst[1])))
            return self.sort_by_timestamp(answer)
        else:
            answer = {metrics_name: []}
            for i in result:
                if i.find(metrics_name) == 0:
                    lst = i.split()
                    answer[metrics_name].append((int(lst[2]), float(lst[1])))
            if not answer[metrics_name]:
                answer = {}
            return self.sort_by_timestamp(answer)

    def put(self, metrics_name, value, timestamp=None):
        if timestamp is None:
            timestamp = int(time.time())

        data = f'put {metrics_name} {value} {timestamp}\n'

        self._sock.send(data.encode('utf-8'))

        response = self._parse_response()
        if not self.response_is_valid(response):
            raise ClientError

    @staticmethod
    def sort_by_timestamp(input_data):
        for k, v in input_data.items():
            v.sort(key=lambda i: i[0])
        return input_data

    @staticmethod
    def connect(ip, host, timeout):
        sock = socket.create_connection((ip, host), timeout)
        return sock

    @staticmethod
    def response_is_valid(data: list):
        if data == ['ok', '', '']:
            return True
        if data[0] != 'ok':
            return False
        else:
            data = data[1:-2]
            for d in data:
                value = d.split()
                if len(value) != 3:
                    return False
                try:
                    float(value[1])
                    int(value[2])
                except ValueError:
                    return False
            return True


if __name__ == '__main__':
    client = Client('127.0.0.1', 8181, 15)
    print(client.get('palm.cpu'))
    client.put("palm.cpu", 2.0, timestamp=1150864248)
    client.put("palm.cpu", 0.5, timestamp=1150864248)
    client.put("palm.cpu", 1.5, timestamp=1150864248)
    client.put("eardrum.memory", 4)
    print(client.get('palm.cpu'))
    print(client.get('*'))
