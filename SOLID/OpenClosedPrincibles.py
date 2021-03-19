from enum import Enum 

class Color(Enum):
    RED = 1 
    GREEN = 2 
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2 
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name 
        self.color = color 
        self.size = size 

    def __str__(self):
        return f"{self.name}"

# breaking Open Close Princibles
''' 
class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p 

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p 

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.size == size and p.color == color:
                yield p
'''
# Specification pattern !!!! 

class Specification:
    def is_satisfied(self, item):
        pass 

    def __and__(self, other):
        pass 

class ColorSpecificaiton(Specification):
    def __init__(self, color):
        self.color = color 

    def is_satisfied(self, item):
        return item.color == self.color 

class SizeSpecificaiton(Specification):
    def __init__(self, size):
        self.size = size 

    def is_satisfied(self, item):
        return item.size == self.size 

class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args 

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))

class Filter:
    def filter(self, item, spec):
        pass

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

# object abstraction 
def main():
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]
    
    '''
    pf = ProductFilter()
    for p in pf.filter_by_size_and_color(products,Size.LARGE, Color.GREEN):
        print(p)
    '''
    # ^ Before 
    # V After 
    
    bf = BetterFilter()
    
    green = ColorSpecificaiton(Color.GREEN)
    for p in bf.filter(products, green):
        print(p)

    print(f" now is by the size:")
    large = SizeSpecificaiton(Size.LARGE)
    for p in bf.filter(products, large):
        print(p)

    print('-------------------------------------')
    large_blue = large and ColorSpecificaiton(Color.GREEN) 
    for p in bf.filter(products, large_blue):
        print(p)


if __name__ == "__main__":
    main()