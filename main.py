import json
import sys

from building import Building


def main(name):
    f = open(sys.argv[1])
    print("sys:{}".format(sys.argv[1]))
    file = json.load(f)
    print("file:{}".format(file))

    b = Building(file['_minFloor'], file['_maxFloor'])
    b.print_self()


if __name__ == '__main__':
    main('PyCharm')
