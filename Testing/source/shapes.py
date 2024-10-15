class Shapes:
    def area(self):
        return
    
    def perimeter(self):
        return
    
    def volume(self):
        return
    
class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.142 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.142 * self.radius

class Reactangle(Shapes):
    def __init__(self,length, width):
        self.length = length
        self.width  = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return (2*self.length) + (2*self.width)
    
    