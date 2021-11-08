class Call:
    def __init__(self, src, dest, time):
        self.src = src
        self.dest = dest
        self.time = time
        self.elev = -1

    def alloc(self, elev):
        self.elev = elev

    def __repr__(self):
        return "Elevator call,{},{},{},0,{}\n".format(self.time, self.src, self.dest, self.elev)

    def __str__(self):
        return "Elevator call,{},{},{},0,{}\n".format(self.time, self.src, self.dest, self.elev)
