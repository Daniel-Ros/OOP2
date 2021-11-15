from call import Direction

class Simulator:

    def bid(self, e, call):
        time = 0
        pos = 0
        for c in e.calls:
            time += self.time_to_finish(e, pos, c.src) + self.time_to_finish(e, c.src, c.dest)
            pos = c.dest
            time += (self.time_to_finish(e, pos, call.src) + self.time_to_finish(e, call.src, call.dest))
        return time

    def get_multi_sorted(self, mc):
        ret = []
        for c in mc.calls:
            ret.append(c.src)
            ret.append(c.dest)
        sorted(ret, reverse=True if mc.calls[0].dir == Direction.DOWN else False)
        return ret

    def time_to_finish(self, e, src, dest):
        if src == dest:
            return 0
        return (e.close + e.start) + (abs(dest - src) / e.speed)
