import json
import sys

from algorithm import Algo
from building import Building
from calls_db import Calls_db
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

def main(name):
    calls = Calls_db(sys.argv[2])
    building = build_building(sys.argv[1])
    algo = Algo(building, calls)
    algo.run()


if __name__ == '__main__':
    main('PyCharm')
