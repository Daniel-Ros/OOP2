from unittest import TestCase

from building import Building
from elevator import Elevator


class TestAlgo(TestCase):
    def test_run(self):
        b = Building()
        e1 = Elevator(b, 0, 1, 3, 3, 2, 2)
        e2 = Elevator(b, 1, 1, 3, 3, 2, 2)
        e3 = Elevator(b, 2, 1, 3, 3, 2, 2)
        e4 = Elevator(b, 3, 1, 3, 3, 2, 2)

        b.add_elevator()
        self.fail()
