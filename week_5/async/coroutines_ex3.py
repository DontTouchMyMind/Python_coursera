# Сопрограммы, генерация исключений

def grep(pattern):
    print('Start grep')
    try:
        while True:
            line = yield    # Отправленное исключение будет сгененрированно именно в этом месте!
            if pattern in line:
                print(line)
    except GeneratorExit:
        print('Stop grep')


g = grep('python')
next(g)     # g.send(None)
g.send('goland is better')
g.send('python is simple')
g.throw(RuntimeError, 'Something wrong')    # Передаем исключение в саму корутину
