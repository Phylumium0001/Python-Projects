import pytest
from source.shapes import Circle 

class TestShapes:
    def setup_method(self,method):
        self.circle = Circle(1)
        print(f"Setting up method : {method}")

    def teardown_method(self,method):
        print(f"Tearing down method : {method}")

    def test_radius(self):
        assert self.circle.radius == 1

    def test_area(self):
        assert self.circle.area() == 3.142 * self.circle.radius ** 2 

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * 3.142 * self.circle.radius 


