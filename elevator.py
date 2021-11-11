class Elevator:
    def __init__(self, building, id, speed, close, open, start, stop) -> None:
        self.id = id
        self.speed = speed
        self.open = open
        self.close = close
        self.start = start
        self.stop = stop
        self.calls = []

    def add_call(self, c):
        self.calls.append(c)

    def remove_call(self, c):
        self.calls.remove(c)

    def bid(self, call):
        time = 0
        pos = 0
        for c in self.calls:
            time += self.time_to_finish(pos, call.src) + self.time_to_finish(call.src, call.dest)
            pos = call.dest
        return time

    def time_to_finish(self, src, dest):
        return self.close + self.start + abs(dest - src) / self.speed + self.stop + self.open
