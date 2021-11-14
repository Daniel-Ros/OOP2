import pandas as pd


class Calls_db:
    def __init__(self, file):
        self.dt = pd.read_csv(file, header=None, index_col=1).drop([0, 4], axis=1).rename_axis(["time"])
        self.dt = self.dt.set_axis(["src", "dest", "elev"], axis=1)
