from enum import Enum
import math 

class CoordinateSystem(Enum):
    CARTESIAN = 1 
    POLAR = 2 

class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"
    '''
    def __init__(self, a, b, system = CoordinateSystem.CARTESIAN):
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif system == CoordinateSystem.POLAR:
            self.x = a * math.sin(b)
            self.y = a * math.cos(b)
    '''

    '''
    @staticmethod
    def new_cartesian_pont(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_pont(rho, theta):
        return Point(rho * math.sin(theta), rho * math.cos(theta))
    '''
    
class PointFactory:
    @staticmethod
    def new_cartesian_pont(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_pont(rho, theta):
        return Point(rho * math.sin(theta), rho * math.cos(theta))



def main():
    p1 = Point(2, 3)
    print(p1)

    p2 = PointFactory.new_cartesian_pont(2, 4)
    p3 = PointFactory.new_polar_pont(4, 5)

    print(p2)
    print(p3)


if __name__ == "__main__":
    main()



