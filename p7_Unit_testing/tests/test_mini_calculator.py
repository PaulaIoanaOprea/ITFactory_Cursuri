import unittest

from p7_Unit_testing.app.mini_calculator import MiniCalculator


class TestMiniCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = MiniCalculator()

    def tearDown(self):
        pass

    # toate metodele de test trebuie sa inceapa cu test_
    def test_adunare(self):
        assert self.calculator.adunare(1, 1) == 2

    def test_scadere(self):
        assert self.calculator.scadere(5, 4) == 1

    def test_inmultire(self):
        assert self.calculator.inmultire(5, 5) == 25

    def test_impartire(self):
        assert self.calculator.impartire(30, 6) == 5