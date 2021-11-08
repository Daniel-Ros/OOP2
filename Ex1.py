import json
import random
import sys

from building import Building
from call import Call
from elevator import Elevator


def build_building(file_name):
    f = open(sys.argv[1])
    file = json.load(f)
    b = Building(file['_minFloor'], file['_maxFloor'])
    for e in file['_elevators']:
        elev = Elevator(b, e['_id'], e['_speed'], e['_closeTime'], e['_openTime'], e['_startTime'], e['_stopTime'])
        b.add_elevator(elev)
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
    for c in calls:
        c.alloc(random.randint(0, building.num_elev()))
    write_calls("out.csv", calls)


if __name__ == '__main__':
    main('PyCharm')
