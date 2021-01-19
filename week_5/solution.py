import socket
import time


class ClientError(BaseException):
    """
    Исключение выбрасывается в случае не успешного получения ответа от сервера(wrong command) - get

    """
    pass


class Client:

    def __init__(self, ip_addr, host, timeout=None):
        self._sock = self.__connect(ip_addr, host, timeout)

    def __create_request(self):

        pass

    def __parse_response(self):
        return self._sock.recv(1024).decode('utf-8').split('\n')

    def get(self, metrics_name):
        data = f'get {metrics_name}\n'
        self._sock.send(data.encode('utf-8'))

        response = self.__parse_response()

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
            return answer
        else:
            answer = {metrics_name: []}
            for i in result:
                if i.find(metrics_name) == 0:
                    lst = i.split()
                    answer[metrics_name].append((int(lst[2]), float(lst[1])))
            if not answer[metrics_name]:    # Это должно происходить при ответе ok\n\n
                answer = {}
            return answer

    def put(self, metrics_name, value, timestamp=None):
        if timestamp is None:
            timestamp = int(time.time())

        data = f'put {metrics_name} {value} {timestamp}\n'

        self._sock.send(data.encode('utf-8'))

        response = self.__parse_response()
        if not self.response_is_valid(response):
            raise ClientError

    @staticmethod
    def __connect(ip, host, timeout):
        sock = socket.create_connection((ip, host), timeout)
        return sock

    @staticmethod
    def response_is_valid(data: list):
        metrics_list = [
            'palm.cpu', 'palm.usage', 'palm.disk_usage', 'palm.network_usage', 'palm.memory',
            'eardrum.cpu', 'eardrum.usage', 'eardrum.disk_usage', 'eardrum.network_usage', 'eardrum.memory',
            'temperature',
            ''
        ]
        # Ответ ok\n\n должен быть верным
        # Обработка ответа error\nwrong command\n\n
        # случай, когда строка ответа сервера содержит кроме ожидаемого содержания и другую текстовую информацию.
        # Пример такого ответа: "some_text\nok\n\n". Какие варианты неправильных ответов еще могут быть,
        # вы можете подумать самостоятельно.

        # Поскольку клиент (при его нормальной реализации) всегда отправляет валидные запросы,
        # ожидаемый ответ сервера должен всегда иметь статус ответа "ok".
        # Проверять необходимо не только поле статуса ответа, но и другие поля.
        # Например: на наличие необходимых полей или "лишних" в данных,
        # на возможность привести данные к нужному типу и т.д. Так же не стоит забывать про ответ сервера в ситуации,
        # когда данные по ключу на сервере отсутствует "ok\n\n"
        # (такой ответ считается валидным и клиент должен возвращать пустой словарь).
        if data[0] != 'ok':
            return False
        else:
            data = data[1:-2]
            for d in data:
                value = d.split()
                if value[0] not in metrics_list:    #
                    return False
                if value[1] in ['not_value']:   # is int or float
                    return False
                if value[2] in ['not_timestamp']:   # is int
                    return False
            return True


if __name__ == '__main__':
    client = Client('127.0.0.1', 8888, 15)
    # print(client.get('palm.cpu'))
    client.put("palm.cpu", 2.0, timestamp=1150864248)
    client.put("palm.cpu", 0.5, timestamp=1150864247)
    client.put("palm.cpu", 0.5, timestamp=1150864248)
    client.put("eardrum.memory", 4200000)
    print(client.get('palm.cpu'))
    print(client.get('*'))
