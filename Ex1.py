import json
import sys

from algorithm import Algo
from building import Building
from call import Call
from elevator import Elevator


def build_building(file_name):
    f = open(sys.argv[1])
    file = json.load(f)
    b = Building(file['_minFloor'], file['_maxFloor'])
    i = 0
    for e in file['_elevators']:
        elev = Elevator(b, i, e['_speed'], e['_closeTime'], e['_openTime'], e['_startTime'], e['_stopTime'])
        b.add_elevator(elev)
        i += 1
    f.close()
    return b


def build_calls_obj(file):
    calls = []
    f = open(file, "r")
    for i in f.readlines():
        c = i.split(',')
        call = Call(c[2], c[3], c[1])
        calls.append(call)
    f.close()
    return calls


def write_calls(file, calls):
    f = open(file, "w+")
    for c in calls:
        f.write(str(c))
    f.close()


def main(name):
    calls = build_calls_obj(sys.argv[2])
    building = build_building(sys.argv[1])
    algo = Algo(building, calls)
    algo.run()
    write_calls(sys.argv[3], calls)


if __name__ == '__main__':
    main('PyCharm')
