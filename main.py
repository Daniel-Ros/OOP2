import json
import sys

from algorithm import Algorithm
from building import Building
from elevator import Elevator
from simulator import Simulator


def build_building(file_name):
    f = open(sys.argv[1])
    print("sys:{}".format(sys.argv[1]))
    file = json.load(f)
    print("file:{}".format(file))

    b = Building(file['_minFloor'], file['_maxFloor'])
    for e in file['_elevators']:
        elev = Elevator(b, e['_id'], e['_speed'], e['_closeTime'], e['_openTime'], e['_startTime'], e['_stopTime'])
        b.add_elevator(elev)
    f.close()
    return b


def main(name):
    building = build_building(sys.argv[1])
    sim = Simulator(building, Algorithm())
    sim.run(sys.argv[2])


if __name__ == '__main__':
    main('PyCharm')
