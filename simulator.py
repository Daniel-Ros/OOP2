from call import MultiCall, Direction

class Simulator:
    def bid(self, e, call):
        time = 0
        pos = 0
        for c in e.calls:
            if isinstance(c, MultiCall):
                for cc in self.get_multi_sorted(c):
                    time += self.time_to_finish(e, pos, cc)
                    pos = cc
            else:
                time += self.time_to_finish(e, pos, c.src) + self.time_to_finish(e, c.src, c.dest)
                pos = c.dest
        if call is not None:
            if isinstance(call, MultiCall):
                for cc in self.get_multi_sorted(call):
                    time += self.time_to_finish(e, pos, cc)
                    pos = cc
            else:
                time += self.time_to_finish(e, pos, call.src) + self.time_to_finish(e, call.src, call.dest)
        return time

    def get_floors_sorted(self, e, calls):
        i = 0
        pos = 0
        acc_time = 0
        while i < len(calls) - 1:
            if calls[i].dir == calls[i + 1].dir:
                if self.time_to_finish(e, pos, calls[i].src) + self.time_to_finish(e, calls[i + 1].src,
                                                                                   calls[i + 1].dest) < calls[
                    i + 1].time - calls[i].time:
                    calls[i], calls[i + 1] = calls[i + 1], calls[i]
                acc_time += self.time_to_finish(e, pos, calls[i].src) + self.time_to_finish(e, calls[i + 1].src,
                                                                                            calls[i + 1].dest)
                pos = calls[i].dest
            i += 1
        return calls

    def get_multi_sorted(self, mc):
        ret = []
        for c in mc.calls:
            ret.append(c.src)
            ret.append(c.dest)
        sorted(ret, reverse=True if mc.calls[0].dir == Direction.DOWN else False)
        return ret

    def time_to_finish(self, e, src, dest):
        return 2 * (e.close + e.start) + (abs(dest - src) / e.speed)
