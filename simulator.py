class Simulator:

    # every elevator has a call list , we want to calculate the time it takes to elevator to finish all calls
    def bid(self, e, call):
        time = 0
        pos = 0
        for c in e.calls:
            time += self.time_to_finish(e, pos, c.src) + self.time_to_finish(e, c.src, c.dest)
            pos = c.dest
            time += (self.time_to_finish(e, pos, call.src) + self.time_to_finish(e, call.src, call.dest))
        return time

    def time_to_finish(self, e, src, dest):
        if src == dest:
            return 0
        return 2 * (e.close + e.start) + (abs(dest - src) / e.speed)
