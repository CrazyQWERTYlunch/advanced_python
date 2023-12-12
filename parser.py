import argparse


def parse_ars():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', metavar='path', type=str, nargs='*', default='.', help='введите путь к директории')
    args = parser.parse_args()
    return args.p
