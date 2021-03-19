import abc 
#= ============== Published part 
class WeatherInterface(metaclass = abc.ABCMeta):
    ''' Abstract Subject part'''
    @abc.abstractclassmethod 
    def add_observer(self, weather_observer):
        pass 

    @abc.abstractclassmethod 
    def remove_observer(self, weather_observer):
        pass

    @abc.abstractclassmethod 
    def notify(self):
        pass 

class WeatherStation(WeatherInterface):
    def __init__(self, temperature, title):
        self.observers = [] 
        self.title = title 
        self.temperature = temperature

    def get_title(self):
        return self.title 

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.do_update(self.temperature, self.get_title())

    def set_temperature(self, temp):
        self.temperature = temp 
        self.notify()
#======================== Observer Part (Subscriber)

class WeatherObserver(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod 
    def do_update(self, temperature, title):
        pass

    def subscribe(self, observer):
        observer.add_observer(self)

    def unsubscribe(self, observer):
        observer.remove_observer(self)

class View(WeatherObserver):
    def __init__(self, title):
        self.title = title 

    def do_update(self, temperature, title):
        print(f"{self.title}'s wall': {title} temperature has changed to {temperature}")

class View2(WeatherObserver):
    def __init__(self, title):
        self.title = title 

    def do_update(self, temperature, title):
        print('--------REPORT FROM {title}---------------------')
        print(f"<h1> {self.title} </h1> <p> T{temperature} <p>")
        print('-----------------------------------------------')


def main():

    baku_station = WeatherStation(18, 'BakuStation')
    ganja_station = WeatherStation(15, 'GanjaStation')
    '''
    Nihad = View('Nihad')
    Murad = View2('Murad') 
    Nihad.subscribe(station)
    Murad.subscribe(station)

    station.set_temperature(36)
    print()
    Nihad.unsubscribe(station)
    station.set_temperature(34)
    Murad.unsubscribe(station)
    '''
    ayaz = View('Ayaz')
    
    ayaz.subscribe(baku_station)
    ayaz.subscribe(ganja_station)

    baku_station.set_temperature(11)
    ganja_station.set_temperature(22)
    baku_station.set_temperature(23)

    #ayaz.unsubscribe(ganja_station)
    ganja_station.set_temperature(35)

if __name__ == "__main__":
    main()
