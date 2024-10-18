import pytest
from calc.calc import Calculator

class CalcTests:
    def setup_object(self, method):
        self.calc = Calculator()
    
    def test_addition(self):
        assert self.calc.addition(1,2) == 3
        assert self.calc.addition(1) == 1
        assert self.calc.addition(1,2,3,4) == 10

    def test_substraction(self):
        assert self.calc.substraction(1,2) == 3
        assert self.calc.substraction(1) == 1
        assert self.calc.substraction(1,2,3,4) == 10