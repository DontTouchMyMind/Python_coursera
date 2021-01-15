# Вызов сопрограмм, PEP 380

def grep(pattern):
    print('Start grep')
    while True:
        line = yield
        if pattern in line:
            print(line)


def grep_python_coroutine():
    g = grep('python')
    next(g)
    g.send('python is the best!')
    g.close()


# g НЕ БУДЕТ корутиной, т.к. не содержит yield
g = grep_python_coroutine()  # is g coroutine?
print(g)


# Делегирование вызова одной корутины другой.
def grep_python():
    g = grep('python')
    yield from g


new_g = grep_python()
print(new_g)
new_g.send(None)
new_g.send('python wow!')


# Для обычных генераторов инструкцию yield можно использовать, как замену циклу for
def chain(x_iterable, y_iterable):
    yield from x_iterable
    yield from y_iterable


def the_same_chain(x_iterable, y_iterable):
    """Аналог функции chain"""
    for x in x_iterable:
        yield x

    for y in y_iterable:
        yield y


a = [1, 2, 3]
b = (4, 5)

for c in chain(a, b):
    print(c)