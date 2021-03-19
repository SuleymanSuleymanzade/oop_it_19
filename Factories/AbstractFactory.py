import abc 

# the interface for shape 
class Shape(metaclass = abc.ABCMeta):
    @abc.abstractclassmethod 
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self):
        print('Calling draw method of Triangle')

class Circle(Shape):
    def draw(self):
        print('Calling draw method of Circle')

class Square(Shape):
    def draw(self):
        print('Calling draw method of Square')

# interface for color family 
class Color(metaclass = abc.ABCMeta):
    @abc.abstractclassmethod 
    def fill(self):
        pass 

class Blue(Color):
    def fill(self):
        print('calling Blue method')

class Red(Color):
    def fill(self):
        print('calling Red method')

class Green(Color):
    def fill(self):
        print('calling Green method')

#Abstract factory family 

class AbstractFactory: 
    def get_color(self):
        pass 
    
    def get_shape(self):
        pass 

class ColorFactory(AbstractFactory):
    def get_color(self, color_type):
        if color_type == None:
            return None 
        return eval(color_type)()

class ShapeFactory(AbstractFactory):
    def get_shape(self, color_type):
        if color_type == None:
            return None 
        return eval(color_type)()


class FactoryProducer:
    def get_factory(choice):
        if choice == "Shape":
            return ShapeFactory()
        elif choice == "Color":
            return ColorFactory()
        else:
            return None

def main():
    
    shape_factory = FactoryProducer.get_factory("Shape") # returns a factory
    shape1 = shape_factory.get_shape("Circle") # retursn an object

    shape1.draw()
    shape2 = shape_factory.get_shape("Rectangle")
    shape2.draw()

    color_factory = FactoryProducer.get_factory("Color")
    red = color_factory.get_color("Blue")
    blue = color_factory.get_color("Green")

    red.fill()
    blue.fill()

if __name__ == "__main__":
    main()
