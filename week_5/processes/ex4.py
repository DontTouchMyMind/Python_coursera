# Файлы в родительском и дочернем процессе

import os


f = open('data.txt')
foo = f.readline()

if os.fork() == 0:
    # Дочерний процесс
    foo = f.readline()
    print('Child: ', foo)
else:
    # Родительский процесс
    foo = f.readline()
    print('parent: ', foo)
