# Синхронизация потоков, блокировки

import threading


class Point(object):
    def __init__(self):
        self._mutex = threading.RLock()
        self._x = 0
        self._y = 0

    def get(self):
        with self._mutex:
            return (self._x, self._y)

    def set(self, x, y):
        with self._mutex:
            self._x = x
            self._y = y


# Еще вариант создания блокировок

a = threading.RLock()
b = threading.RLock()


def foo():
    try:
        a.acquire()
        b.acquire()
    finally:
        a.release()
        b.release()


# Синхронизация потоков, условные переменные

class Queue(object):

    def __init__(self, size=5):
        self._size = size
        self._queue = []
        self._mutex = threading.RLock()
        self._empty = threading.Condition(self._mutex)
        self._full = threading.Condition(self._mutex)

    def put(self, val):
        with self._full:
            while len(self._queue) >= self._size:
                self._full.wait()

            self._queue.append(val)
            self._empty.notify()

    def get(self):
        with self._empty:
            while len(self._queue) == 0:
                self._empty.wait()

            ret = self._queue.pop(0)
            self._full.notify()
            return ret
