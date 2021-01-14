# Создание потока

from threading import Thread


class PrintThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self) -> None:
        print('Hello', self.name)


th = PrintThread('Mike')
th.start()
th.join()