# Создание процесса, модуль multiprocessing

from multiprocessing import Process


class PrintProcess(Process):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self) -> None:
        print('Hello,', self.name)


p = PrintProcess('Mike')
p.start()
p.join()