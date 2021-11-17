from unittest import TestCase

from Ex1 import build_calls_obj
from algorithm import Algo
from building import Building
from elevator import Elevator


class TestAlgo(TestCase):
    def test_run(self):
        b = Building(-100, 100)
        e1 = Elevator(b, 0, 1, 3, 3, 2, 2)
        e2 = Elevator(b, 1, 1, 3, 3, 2, 2)
        e3 = Elevator(b, 2, 1, 3, 3, 2, 2)
        e4 = Elevator(b, 3, 1, 3, 3, 2, 2)

        b.add_elevator(e1)
        b.add_elevator(e2)
        b.add_elevator(e3)
        b.add_elevator(e4)

        calls = build_calls_obj("Ex1_Calls/Calls_b.csv")
        a = Algo(b, calls[0])
        a.run()
        for c in calls[0]:
            if c.elev == -1:
                print(c)
                self.fail()
        self.assertTrue(True)
