import abc 
import copy 

class Shape(metaclass=abc.ABCMeta):
    def __init__(self):
        self.id = None 
        self.type = None 
    @abc.abstractmethod 
    def draw(self):
        pass

    def get_type(self):
        return self.type 

    def get_id(self):
        return self.id 

    def set_id(self, sid):
        self.id = sid 

    def clone(self):
        return copy.copy(self) 

class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.type = "Rectangle"

    def draw(self):
        print('draw method called by rectangle object')

class Square(Shape):
    def __init__(self):
        super().__init__()
        self.type = "Square"

    def draw(self):
        print('draw method called by square object')

class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.type = "Circle"

    def draw(self):
        print('draw method called by circle object')

class ShapeCache:
    cache = {}

    @staticmethod 
    def get_shape(sid):
        shape = ShapeCache.cache.get(sid, None)
        return shape.clone()

    @staticmethod 
    def set_shape(object_ref, sid):
        object_ = object_red()
        object_.set_id(sid)
        if object_.get_id() not in ShapeCache.cache:
            ShapeCache.cache[object_.get_id()] = object_

    @staticmethod 
    def load():
        circle = Circle()
        circle.set_id('1')
        ShapeCache.cache[circle.get_id()] = circle
        
        square = Square()
        square.set_id('2')
        ShapeCache().cache[square.get_id()] = square  

        rectangle = Rectangle()
        rectangle.set_id('3')
        ShapeCache().cache[rectangle.get_id()] = rectangle 

def main():

    ShapeCache.load()
    circle = ShapeCache.get_shape("1")
    print(circle.get_type())

    square = ShapeCache.get_shape('2')
    print(square.get_type()) 

    rectangle = ShapeCache.get_shape('3')
    print(rectangle.get_type()) 

    print(rectangle.__dict__)

if __name__ == "__main__":
    main()  
