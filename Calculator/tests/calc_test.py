import pytest
from calc.calc import Calculator

class CalcTests:
    def test_addition(self,method):
        assert Calculator.addition(1,2) == 3
        assert Calculator.addition(1) == 1
        assert Calculator.addition(1,2,3,4) == 10

    def test_substraction(self,method):
        assert Calculator.substraction(1,2) == 3
        assert Calculator.substraction(1) == 1
        assert Calculator.substraction(1,2,3,4) == 10