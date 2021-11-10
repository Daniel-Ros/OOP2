import random
from functools import cmp_to_key


class Algo:
    def __init__(self, b, c):
        self.building = b
        self.calls = c

    def run(self):
        sorted(self.building.elev, key=cmp_to_key(lambda item1, item2: item1.speed - item2.speed))
        for c in self.calls:
            c.alloc(random.randint(0, self.building.num_elev()))
