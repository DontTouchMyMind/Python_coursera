# Сопрограммы (корутины)
# Сопрограмма содержит инструкцию yield и ожидает пока кто-то отправит в нее значение при помощи метода send

def grep(pattern):
    print('Start grep')
    while True:
        line = yield
        if pattern in line:
            print(line)


g = grep('python')
next(g)     # g.send(None)
g.send('goland is better')
g.send('python is simple')