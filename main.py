from dir_wolker import walk_dir
from parser import parse_ars


def main():
    for place in parse_ars():
        for item in (walk_dir(place)):
            print(repr(item))


if __name__ == '__main__':
    main()
    # python main.py -p  C:/Users/User/Desktop/ - пример для запуска из cmd
