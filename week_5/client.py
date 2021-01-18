# import socket
#
#
# HOST = '127.0.0.1'
# PORT = 8888
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect((HOST, PORT))
# sock.sendall('p'.encode('utf-8'))
# result = sock.recv(1024)
#
# sock.close()
# print(result.decode('utf-8'))


class Class:

    def __pasrse(self):
        pass

    def put(self):
        print(self.__pasrse())

    def get(self):
        self.__pasrse()


c = Class()
c.put()