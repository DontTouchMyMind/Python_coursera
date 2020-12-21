import argparse
import os
import tempfile
import json


parser = argparse.ArgumentParser()
parser.add_argument('--key', help='Key help')
parser.add_argument('--val', help='Value help')
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'w') as f:
    d = {'key': None, 'val': None}

with open(storage_path, 'r') as f:
    if args.val:
        print(f'write {args.key=} and {args.val=} in the data file.')
        data = json.load(f)
        if data[args.key] in data:
            data[args.key] = data[args.key] + [args.val]
        else:
            data.update({args.key: [args.val]})
        json.dump(data, f)
    else:
        print(f'read {args.key=} from data file')
        data = json.load(f)
        if len(data[args.key]) > 1:
            print(', '.join(data.get(args.key)))
        else:
            print(*data.get(args.key))
