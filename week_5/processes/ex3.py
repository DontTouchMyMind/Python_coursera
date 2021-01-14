# Память родительского и дочернего процесса

import os


foo = 'bar'

if os.fork() == 0:
    # Дочерний процесс
    foo = 'baz'
    print('Child: ', foo)
else:
    # Родительский процесс
    print('parent: ', foo)
    os.wait()