class Simulator:
    def __init__(self, building, calls):
        self.building = building
        self.calls = calls
        self.time = 0

    def run(self):
        self.calls