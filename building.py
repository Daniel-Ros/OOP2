class Building(object):
    def __init__(self, min_floor, max_floor) -> None:
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.elev = []

    def add_elevator(self, elev) -> None:
        self.elev.append(elev)

    def print_self(self):
        print("{} {}".format(self.min_floor, self.max_floor))
