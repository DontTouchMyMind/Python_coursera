import socket


with socket.create_connection(('127.0.0.1', 10001), 5) as sock:
    # set socket read timeout
    sock.settimeout(2)
    try:
        sock.sendall('ping'.encode('utf-8'))
    except socket.timeout:
        print('Send data timeout')
    except socket.error as ex:
        print('Send data error:', ex)