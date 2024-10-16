import pytest
import source.sample as sample

def test_add():
    assert sample.add(1,2) == 3
    
    with pytest.raises(TypeError):
        sample.add()
        sample.add(1) == 1
