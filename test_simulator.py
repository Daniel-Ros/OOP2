from unittest import TestCase

from call import Call
from elevator import Elevator
from simulator import Simulator


class TestSimulator(TestCase):

    def test_bid(self):
        e1 = Elevator(None, 0, 1, 3, 3, 2, 2)
        e2 = Elevator(None, 0, 1, 3, 3, 2, 2)
        sim = Simulator()
        c = Call(0, 5, 0)
        t1 = sim.bid(e1, c)
        t2 = sim.bid(e2, c)
        self.assertEqual(t1, t2)
        c.alloc(e1)
        c = Call(0, 10, 10)
        t1 = sim.bid(e1, c)
        t2 = sim.bid(e2, c)
        self.assertTrue(t1 > t2)

    def test_time_to_finish(self):
        e1 = Elevator(None, 0, 1, 3, 3, 2, 2)
        sim = Simulator()
        self.assertEqual(sim.time_to_finish(e1, 0, 1), 1 + 3 + 3 + 2 + 2)
        self.assertEqual(sim.time_to_finish(e1, 0, 6), 6 + 3 + 3 + 2 + 2)
        self.assertEqual(sim.time_to_finish(e1, 0, -1), 1 + 3 + 3 + 2 + 2)
        self.assertEqual(sim.time_to_finish(e1, 0, -6), 6 + 3 + 3 + 2 + 2)
