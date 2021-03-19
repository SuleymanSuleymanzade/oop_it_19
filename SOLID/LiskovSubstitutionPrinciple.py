'''
Let Q(x) be a property in object of X of the type T, then Q(Y) should be
provable for objects Y of type S where S is a subtype of T
'''
class Rectangle:
    def __init__(self, width, height):
        self._height = height 
        self._width = width

    @property
    def area(self):
        return self._width * self._height 

    def __str__(self):
        return f"width {self._width}, height: {self._height}"

    @property 
    def width(self):
        return self._width 

    @width.setter 
    def width(self, val):
        self._width = val 

    @property 
    def height(self):
        return self._height 

    @height.setter 
    def height(self, val):
        self._height = val 

class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter 
    def width(self, value):
        _width = _height = value 

    @Rectangle.height.setter 
    def height(self, value):
        _width = _height = value 

def use_geometry(rc):
    w = rc.width 
    rc.height = 10 # !!!!!! LIS princibles has been broked 
    expected = int(w * 10)
    print(f'expected an area of {expected}, got {rc.area}')

def main():
    
    rc = Rectangle(2, 3)
    use_geometry(rc) # so far so good !

    sq = Square(5)
    use_geometry(sq) # Ups. now we got a wrong report 

if __name__ == "__main__":
    main()




    