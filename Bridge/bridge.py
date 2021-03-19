import abc 

# implementor part
class Color(metaclass=abc.ABCMeta):
    @abc.abstractmethod 
    def fill_color(self):
        pass 

class RedColor(Color):
    def fill_color(self):
        print('filled with Red color')

class BlueColor(Color):
    def fill_color(self):
        print('filled with Blue color')

# Abstraction part 
class Shape(metaclass = abc.ABCMeta):
    def __init__(self, color):
        self.color = color 

class Rectangle(Shape):
    def __init__(self, color):
        super().__init__(color)

    def color_it(self):
        print('Rectangle')
        self.color.fill_color()

class Circle(Shape):
    def __init__(self, color):
        super().__init__(color)

    def color_it(self):
        print('Circle')
        self.color.fill_color()

def main():
    rc = RedColor()
    r1 = Rectangle(rc)
    r1.color_it()

    circle = Circle(BlueColor())
    circle.color_it()

if __name__ == "__main__":
    main()
