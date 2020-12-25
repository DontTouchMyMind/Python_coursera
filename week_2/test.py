import json
import os


var_key = input('KEY: ')
var_val = input('VAL: ')

if not os.path.isfile('test1.data'):
    with open('test1.data', 'w') as file_create:
        data = {var_key: [var_val]}
        json.dump(data, file_create)
else:
    with open('test1.data', 'r') as file:
        data = json.loads(file.read())

if var_val:
    # Только запись в файл
    pass
else:
    # Вывод значений ключа
    pass
with open('test1.data', 'w') as file:
    json.dump(data, file)
#         for i in data_from_json[var_key]:
#             if i:
#                 data = {var_key: [var_val]}
#             else:
#                 da
#         data_from_json.get(var_key).append(var_val)
#         json.dump(data_from_json, file)
#
# print(data_from_json)
# print(type(data_from_json))



# data = {'key': []}
# with open('test.data', mode='r') as f:
#     data = json.load(f)
#
# with open('test.data', mode='w') as f:
#     choice = input()
#     if choice not in data.get('key'):
#         data.get('key').append(choice)
#     json.dump(data, f)
# with open('test.data', mode='w') as f:
#     data = {'key': []}
#     data.get('key').append('qw')
#     # json.dump(data, f)
#     data.update({'key': ['1']})
#     json.dump(data, f)
    # while n > 0:
    #     choice = input()
    #
    #         #data.get('key').append(choice)
    #         # json.dump(data, f)
    #     n -= 1

# if os.path.isfile('text.txt'):
#     with open('text.txt', 'w'):
#         data = {'key': []}

# key = 'log2'
# val = 'qwe'
# d = {key: [val]}
# r = d.get(key)
# print(r)
# d.get(key).append('2')
# r = d.get(key)
# print(r)