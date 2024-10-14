import pytest
import source.sample as s

def testAdd():
    assert s.add(1, 2) == 3
    assert s.add(-1, 1) == 0

def testDivide():
    with pytest.raises(ZeroDivisionError):
        s.divide(1, 0)