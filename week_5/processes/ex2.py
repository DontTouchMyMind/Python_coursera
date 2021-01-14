import time
import os


pid = os.fork()
if pid == 0:
    # Дочерний процесс
    while True:
        print('Child: ', os.getpid())
        time.sleep(5)
else:
    # Родительский процесс
    print('parent: ', os.getpid())
    os.wait()
