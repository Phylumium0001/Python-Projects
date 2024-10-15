import pytest
from source.shapes import Reactangle

class Test_Reactangle:
    def setup_method(self,method):
        self.rectangle = Reactangle(10,20)
    
    def teardown_method(self, method):
        return
    
    def test_argument_error(self):
        with pytest.raises(TypeError):
            Reactangle(1)
    
    def test_area(self):
        assert self.rectangle.area() == 200

    def test_perimeter(self):
        assert self.rectangle.perimeter() == 60 