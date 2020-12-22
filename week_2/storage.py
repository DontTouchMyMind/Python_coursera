import argparse
import os
import tempfile
import json


parser = argparse.ArgumentParser()
parser.add_argument('--key', help='Key help')
parser.add_argument('--val', help='Value help')
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage18.data')

if not os.path.isfile(storage_path):
    with open(storage_path, 'w') as file_create:
        data = {args.key: [args.val]}
        json.dump(data, file_create)
        print('file was created')
else:
    with open(storage_path, 'r') as file_read:
        data = json.load(file_read)

print(data)
with open(storage_path, mode='r+') as file:
    if args.val:
        if args.val not in data.get(args.key):
            data.get(args.key).append(args.val)
        json.dump(data, file)
    else:
        data = json.load(file)
        if None not in data.get(args.key, None):
            print(', '.join(data.get(args.key)))
        else:
            print(None)



# with open(storage_path, 'r') as f:
#     if args.val:
#         print(f'write {args.key=} and {args.val=} in the data file.')
#         data = json.load(f)
#         if data[args.key] in data:
#             data[args.key] = data[args.key] + [args.val]
#         else:
#             data.update({args.key: [args.val]})
#         json.dump(data, f)
#     else:
#         print(f'read {args.key=} from data file')
#         data = json.load(f)
#         if len(data[args.key]) > 1:
#             print(', '.join(data.get(args.key)))
#         else:
#             print(*data.get(args.key))
