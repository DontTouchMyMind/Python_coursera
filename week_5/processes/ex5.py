# Создание процесса, модуль multiprocessing

from multiprocessing import Process


def f(name):
    print('Hello,', name)


p = Process(target=f, args=('Bob',))
p.start()   # Только здесь будет создан процесс! И будет вызван fork
p.join()    # Ожидаем завершения всех созданных дочерних процессов
