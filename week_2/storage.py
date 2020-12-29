import argparse
import os
import tempfile
import json


def read_file(storage_path):
    if not os.path.isfile(storage_path):
        return {}

    with open(storage_path, 'r') as file:
        data_from_json = file.read()
        if data_from_json:
            return json.loads(data_from_json)
        return {}


def write_file(storage_path, data):
    with open(storage_path, 'w') as file:
        file.write(json.dumps(data))


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Key help')
    parser.add_argument('--val', help='Value help')
    return parser.parse_args()


def get_data(storage_path, key):
    data = read_file(storage_path)
    return data.get(key, [])


def put_data(storage_path, key, value):
    data = read_file(storage_path)
    data[key] = data.get(key, [])
    data[key].append(value)
    write_file(storage_path, data)


def main(storage_path):
    args = parse_arguments()

    if args.key and args.val:
        put_data(storage_path, args.key, args.val)
    elif args.key:
        print(*get_data(storage_path, args.key), sep=', ')
    else:
        print('Invalid arguments')


if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    main(storage_path)

# OLD version
# parser = argparse.ArgumentParser()
# parser.add_argument('--key', help='Key help')
# parser.add_argument('--val', help='Value help')
# args = parser.parse_args()
#
# storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
#
# if args.val:
#     if not os.path.isfile(storage_path):
#         with open(storage_path, 'w') as file_create:
#             data = {args.key: [args.val]}
#             json.dump(data, file_create)
#     else:
#         with open(storage_path, 'r+') as file:
#             data = json.loads(file.read())
#             if args.key not in data:
#                 data[args.key] = [args.val]
#             else:
#                 data.get(args.key).append(args.val)
#     with open(storage_path, 'w') as file_save:
#         json.dump(data, file_save)
# else:
#     if not os.path.isfile(storage_path):
#         print(None)
#     else:
#         with open(storage_path, 'r') as file:
#             data = json.loads(file.read())
#             if args.key in data:
#                 print(', '.join(data.get(args.key)))
#             else:
#                 print(None)
