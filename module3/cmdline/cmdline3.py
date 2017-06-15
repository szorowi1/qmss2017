import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--in", default=False, type=str, required=True,
                    dest='src',help='Source directory.')
parser.add_argument("-o","--out", default=False, type=str, required=True, 
                    dest='targ', help='Target directory.')
parser.add_argument("--silence", default=False, required=False, action='store_true',
                    dest='silence', help='Do not print src/targ.')
args = parser.parse_args()

if not args.silence:
    print('src: %s' %args.src)
    print('targ: %s' %args.targ)
    