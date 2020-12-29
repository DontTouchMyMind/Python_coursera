import argparse
import os
import tempfile
import json


parser = argparse.ArgumentParser()
parser.add_argument('--key', help='Key help')
parser.add_argument('--val', help='Value help')
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if args.val:
    if not os.path.isfile(storage_path):
        with open(storage_path, 'w') as file_create:
            data = {args.key: [args.val]}
            json.dump(data, file_create)
    else:
        with open(storage_path, 'r+') as file:
            data = json.loads(file.read())
            if args.key not in data:
                data[args.key] = [args.val]
            else:
                data.get(args.key).append(args.val)
    with open(storage_path, 'w') as file_save:
        json.dump(data, file_save)
else:
    if not os.path.isfile(storage_path):
        print(None)
    else:
        with open(storage_path, 'r') as file:
            data = json.loads(file.read())
            if args.key in data:
                print(', '.join(data.get(args.key)))
            else:
                print(None)
