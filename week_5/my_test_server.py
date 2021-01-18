import socket


with socket.socket() as sock:
    sock.bind(('', 8888))
    sock.listen()

    while True:

        conn, addr = sock.accept()

        print('Соединение установлено:', addr)

        response = b'ok\npalm.cpu 10.5 1501864247\npalm.cpu 0.5 1150864248\neardrum.cpu 15.3 1501864259\n\n'

        while True:
            data = conn.recv(1024)
            if not data:
                break
            request = data.decode('utf-8')
            print(f'Получен запрос: {ascii(request)}')
            print(f'Отправлен ответ {ascii(response.decode("utf-8"))}')
            conn.send(response)