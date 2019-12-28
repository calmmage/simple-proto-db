import argparse
import os
from pathlib import Path

PROTO_BINARY = "/Users/plavrov/anaconda3/bin/protoc"  # todo: same as /Users/plavrov/anaconda3/bin/python


# todo: autoconvert arguments
def compile_proto(path):
    """
    :param path:
    :type path: Path
    :return:
    """

    python_out = path.parent / (path.stem + '_pb2.py')
    cmd = f"{PROTO_BINARY} --python_out {python_out} {path}"
    # todo: run_cmd
    os.execl()


def main(path):
    path = Path(path)
    # go over all the files
    # for path in os.walk():
    #     if path.ext == 'proto':

    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--path')  # just get it

    args = parser.parse_args()

    main(path=args.path)
