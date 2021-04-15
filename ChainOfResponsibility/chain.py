import abc 
from enum import IntEnum 

class PlanetEnum(IntEnum):
    MERCURY = 1 
    VENUS = 2 
    EARTH = 3 
    MARS = 4 
    JUPITER = 5 
    SATURN = 6 
    URANUS = 7
    NEPTUNE = 8 


class PlanetHandler(metaclass = abc.ABCMeta):
    def __init__(self):
        self.next = None 

    @abc.abstractmethod 
    def handle_request(self, request):
        pass 

    def set_next_handler(self, handler):
        self.next = handler 

class MercuryHandler(PlanetHandler):
    def handle_request(self, request):
        if request is PlanetEnum.MERCURY:
            print('the mercury is the nearest planet to the sun')
        else:
            print('Venus is pass handle for the next item')
            if self.next is not None:
                self.next.handle_request(request)

class EarthHandler(PlanetHandler):
    def handle_request(self, request):
        if request is PlanetEnum.EARTH:
            print('The Earth is our planet')
        else:
            print('Earth is pass handle for the next item')
            if self.next is not None:
                self.next.handle_request(request)

class MarsHandler(PlanetHandler):
    def handle_request(self, request):
        if request is PlanetEnum.MARS:
            print('the Mars has two moons')
        else:
            print('Mars is pass handle for the next item')
            if self.next is not None:
                self.next.handle_request(request)

def create_handler_list():
    mercury_handler = MercuryHandler()
    earth_handler = EarthHandler()
    mars_handler = MarsHandler()

    mercury_handler.set_next_handler(earth_handler)
    earth_handler.set_next_handler(mars_handler)
    return mercury_handler

def main():
    
    chain = create_handler_list()

    chain.handle_request(PlanetEnum.MARS)
    print()
    chain.handle_request(PlanetEnum.EARTH)
    print()
    chain.handle_request(PlanetEnum.MERCURY)


if __name__ == "__main__":
    main()