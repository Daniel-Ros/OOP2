from algorithm import Algorithm
from building import Building


class Simulator(object):
    def __init__(self, building: Building, algo: Algorithm):
        self.building = building
        self.algo = algo

    def run(self, file):
        calls = self.read_calls(file)
        self.algo.make_plan(calls)

    def read_calls(self, file):
        f = open(file)
        calls = []
        for line in f.readlines():
            data = line.split(',')
            time, src, dest = data[1], data[2], data[3]
            calls.append({
                'time': time,
                'src': src,
                'dest': dest
            })
        return calls
