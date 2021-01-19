import asyncio
import time


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


class ClientServerProtocol(asyncio.Protocol):
    storage = {
        'palm.cpu': [(
            10.5,
            1501864247
        )]
    }

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print(f'Connection from {peername}')
        self.transport = transport

    def data_received(self, data):
        message = data.decode('utf-8')  # Полученные данные
        print(f'Data recieved: {message}')
        message = self._parse_input_data(data.decode('utf-8'))
        if not self._response_is_valid(message):
            response = b'error\nwrong command\n\n'
        else:
            if message[0] == 'get':
                response = self._get_data()     # -> b'ok\npalm.cpu 10.5 1501864247\n\n'
                # b'ok\npalm.cpu 10.5 1501864247\npalm.cpu 0.5 1150864248\neardrum.cpu 15.3 1501864259\n\n'
            elif message[0] == 'put':
                response = self._save_data(message)    # -> b'ok\n\n'
            else:
                # print(message)
                pass    # -> b'error\nwrong command\n\n'

        print(f'Send: {response}')
        self.transport.write(response)

    def _save_data(self, input_data: list) -> bytes:
        """Метод сохраняет данные на сервере"""
        if len(input_data) == 3:
            input_data.append(int(time.time()))
        if input_data[1] in self.storage.keys():
            for data in self.storage[input_data[1]]:
                if data[1] == input_data[3]:
                    self.storage[input_data[1]].remove(data)
                    self.storage[input_data[1]].append((input_data[2], input_data[3]))
                    break
            else:
                self.storage[input_data[1]].append((input_data[2], input_data[3]))
        else:
            self.storage[input_data[1]] = [(input_data[2], input_data[3])]
        print(self.storage)     # ! ->test!
        return b'ok\n\n'

    def _get_data(self) -> bytes:
        """Метод считывает данные с сервера"""
        return b'ok\npalm.cpu 10.5 1501864247\n\n'

    @staticmethod
    def _parse_input_data(data: str) -> list:
        """Метод преобразовывает входящий запрос в список данных"""
        data = data.split()
        return data

    @staticmethod
    def _response_is_valid(data: list) -> bool:
        """Метод проверяет правильность входящих данных согласно протоколу передачи"""
        if not data:
            return False
        if data[0] == 'put':                        # При запросе put,
            if len(data) != 3 and len(data) != 4:   # длина равна 3(4)['get', 'metrics_name', 'value', 'timestamp=None']
                return False
        elif data[0] == 'get':  # При запросе get,
            if len(data) != 2:  # длина комманды должна быть = 2, ['get', 'metrics_name']
                return False
        else:
            return False
        return True


if __name__ == '__main__':
    run_server('127.0.0.1', 8181)
