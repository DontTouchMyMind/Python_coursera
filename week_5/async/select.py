# Неблокирующий ввод/ввывод, обучающий пример

import socket
import select


sock = socket.socket()
sock.bind(('', 10001))
sock.listen()

# как обработать запросы для con1, conn2 одновременно буз потоков
conn1, addr = sock.accept()
conn2, addr = sock.accept()

conn1.setblocking(0)    # Сокеты в не блокирующем режиме, равносильно .settimout=0
conn2.setblocking(0)

# Как узнать какие сокеты готовы читать данные, а какие готовы записывать? Для этого воспользуемся epoll
epoll = select.epoll()  # Создаем объект epoll
epoll.register(conn1.fileno(), select.EPOLLIN | select.EPOLLOUT)    # Регистрируем в объекте epoll наши
epoll.register(conn2.fileno(), select.EPOLLIN | select.EPOLLOUT)    # файловые дискрипторы (.fileno()) и маску(.EPOLLIN)

conn_map = {
    conn1.fileno(): conn1,
    conn2.fileno(): conn2,

}

# Цикл обработки событий в epoll (Event Loop)
while True:
    events = epoll.poll(1)
    for fileno, event in events:
        if event & select.EPOLLIN:
            data = conn_map[fileno].recv(1024)
            print(data.decode('utf-8'))
        elif event & select.EPOLLOUT:
            conn_map[fileno].send('ping'.encode('utf-8'))
