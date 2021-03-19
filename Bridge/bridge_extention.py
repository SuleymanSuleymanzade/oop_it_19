from .bridge_extention import Rectangle 
from .extended_colors import Green 

class Cirlce(Rectangle):
    def __init__(self, color):
        super().__init__(color)

    def color_it(self):
        print('Circle')
        self.color.fill_color()


