import pandas as pd
import numpy as np


class Calls_db:
    def __init__(self, file):
        self.dt = pd.read_csv(file, header=None, index_col=1).drop([0, 4], axis=1).rename_axis(["time"])
        self.dt = self.dt.set_axis(["src", "dest", "elev"], axis=1)
        self.dt["dir"] = np.where(self.dt["src"] < self.dt["dest"],"up","down")

    def __str__(self):
        ret =[]
        for idx, c in self.dt.iterrows():
            ret.append("Elevator call,{},{},{},0,{}\n".format(idx,c["src"],c["dest"],c["elev"]))
        return "".join(map(str,ret))
