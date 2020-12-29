import json
import os


var_key = input('KEY: ')
var_val = input('VAL: ')

if var_val:
    if not os.path.isfile('test.data'):
        with open('test.data', mode='w') as file_create:
            data = {var_key: [var_val]}
            json.dump(data, file_create)
    else:
        with open('test.data', mode='r+') as file:
            data = json.loads(file.read())
            if var_key not in data:
                data[var_key] = [var_val]
            else:
                if var_val not in data.get(var_key):
                    data.get(var_key).append(var_val)

    with open('test.data', 'w') as file:
        json.dump(data, file)

else:
    if not os.path.isfile('test.data'):
        print(None)
    else:
        with open('test.data', mode='r') as file:
            data = json.loads(file.read())
            if var_key in data:
                print(', '.join(data.get(var_key)))
            else:
                print(None)

