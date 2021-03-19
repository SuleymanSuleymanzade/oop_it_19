import abc 

# familty of the cars 
class Car(metaclass = abc.ABCMeta):
    @abc.abstractclassmethod 
    def assemble(self):
        pass 


class RaceCar(Car):
    def assemble(self):
        print('Race Car')

# Decorator
class Decorator(Car):
    def __init__(self, car):
        self.car = car 

    def assemble(self):
        self.car.assemble()

class StickerOne(Decorator):
    def __init__(self, car):
        super(StickerOne, self).__init__(car)

    def assemble(self):
        super(StickerOne, self).assemble()
        print('Sticker One added')

class StickerTwo(Decorator):
    def __init__(self, car):
        super(StickerTwo, self).__init__(car)

    def assemble(self):
        super(StickerTwo, self).assemble()
        print('Sticker Two added')


def main():
    race_car = StickerOne(StickerOne(StickerTwo(StickerOne(RaceCar()))))
    race_car.assemble()

if __name__ == "__main__":
    main()