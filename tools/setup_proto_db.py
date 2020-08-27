import argparse
import os
from pathlib import Path

PROTO_BINARY = "/Users/plavrov/anaconda3/bin/protoc"  # todo: same as /Users/plavrov/anaconda3/bin/python

from calmlib.proto_utils import compile_proto

def main(path):
    path = Path(path)
    # todo: go over all the files
    # for path in os.walk():
    #     if path.ext == 'proto':

    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--path')  # just get it

    args = parser.parse_args()

    main(path=args.path)
