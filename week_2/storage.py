import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--key', help='Key help')
parser.add_argument('--val', help='Value help')

args = parser.parse_args()

if not args.val:
    print('val is empty')
    if not args.key:
        print('key is empty')
    else:
        print(f'{args.key=}')
else:
    print(f'{args.val=}')