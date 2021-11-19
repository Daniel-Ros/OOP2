import json
import sys

from algorithm import Algo
from building import Building
from call import Call
from elevator import Elevator

# build building , elevators from json
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

# build calls from csv
def build_calls_obj(file):
    calls = []
    f = open(file, "r")
    tmin = 0
    tmax = 0
    for i in f.readlines():
        c = i.split(',')
        call = Call(c[2], c[3], c[1])
        tmin = min([tmin, int(c[2]), int(c[3])])
        tmax = max([tmin, int(c[2]), int(c[3])])
        calls.append(call), tmin, tmax
    f.close()
    return calls, tmin, tmax

# creating out.csv file
def write_calls(file, calls):
    f = open(file, "w+")
    for c in calls:
        f.write(str(c))
    f.close()

def main():
    calls, tmin, tmax = build_calls_obj(sys.argv[2])
    building = build_building(sys.argv[1])
    building.set_active_minmax(tmin, tmax)
    algo = Algo(building, calls)
    algo.run()
    write_calls(sys.argv[3], calls)


if __name__ == '__main__':
    main()
