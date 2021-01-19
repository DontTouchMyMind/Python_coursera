# def parse_input_data(data: str):
#     """Метод преобразовывает входящий запрос в определенную форму"""
#     # put palm.cpu 23.7 1150864247\n
#     # get palm.cpu\n
#     data = data.split()
#     print(data)
#     return data
#
#
# def response_is_valid(data: list) -> bool:
#     """Метод проверяет правильность входящих данных согласно протоколу передачи"""
#
#     # Проверка команды put или get
#     # put
#     if data[0] == 'put':                        # При запросе put,
#         if len(data) != 3 and len(data) != 4:    # длина равна 3(4)['get', 'metrics_name', 'value', 'timestamp']
#             return False
#     elif data[0] == 'get':  # При запросе get,
#         if len(data) != 2:  # длина комманды должна быть = 2, ['get', 'metrics_name']
#             return False
#     else:
#         return False
#     return True
#
# p = 'put palm.cpu 23.7 1150864247\n'
# p1 = 'put palm.cpu 2.0 1150864247 1150864247\n'
# g = 'get palm.cpu\n'
# m = '\n'
#
# r = parse_input_data(m)
# print(r)
# print(len(r))
# print(response_is_valid(r))

storage = {
    'palm.cpu': [(
        10.5,
        1501864247
    ), (
        11.0,
        0
    ), (
        1.0,
        1221112265
    )]
}

# print(storage['palm.cpu'][0][0])
# # if storage['palm.cpu'][0][1] == 1501864247:
# #     storage['palm.cpu'][0] =
for i in storage['palm.cpu']:
    print(i)
    if i[1] == 0:
        storage['palm.cpu'].remove(i)
        storage['palm.cpu'].append((99, 0))
        break
else:
    storage['palm.cpu'].append((99, 1))

print(storage)

