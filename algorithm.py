from call import MultiCall


class Algo:
    def __init__(self, b, c):
        self.building = b
        self.calls = c

    def run(self):
        self.join_calls()
        print(len(self.calls))
        for c in self.calls:
            min_time = 2147483647
            min_elev = None
            for e in self.building.elev:
                time_wasted = e.bid(c)
                if time_wasted <= min_time:
                    min_time = time_wasted
                    min_elev = e
            c.alloc(min_elev)

    def join_calls(self):
        i = 0
        j = 0
        while i < len(self.calls)-2:



        # i = 0
        # while i < len(self.calls) - 2:
        #     j = i + 1
        #     if abs(self.calls[i].src - self.calls[j].src) < (self.building.max_floor - self.building.min_floor) * 0.1:
        #         if self.calls[i].src > self.calls[i].dest and self.calls[j].src > self.calls[j].dest or self.calls[
        #             i].src < self.calls[i].dest and self.calls[j].src < self.calls[j].dest:
        #             if abs(self.calls[i].time - self.calls[j].time) < 10:
        #                 multi_call = MultiCall([self.calls[i], self.calls[j]])
        #                 self.calls[i] = multi_call
        #                 self.calls.remove(self.calls[j])
        #                 i += 1
        #     i += 1
