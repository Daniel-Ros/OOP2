class Elevator:
    fastest = 0
    fastest_elev = None

    def __init__(self, building, id, speed, close, open, start, stop) -> None:
        self.id = id
        self.speed = speed
        self.open = open
        self.close = close
        self.start = start
        self.stop = stop
        self.calls = []  # calls assigned to this elevator
        self.time = 0
        Elevator.fastest = max(Elevator.fastest, speed)
        if speed == Elevator.fastest:
            Elevator.fastest_elev = self

    def add_call(self, c):
        self.calls.append(c)

    def remove_call(self, c):
        self.calls.remove(c)
