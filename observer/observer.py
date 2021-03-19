import abc 
#= ============== Subscriber part 
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
    def __init__(self, temperature):
        self.observers = [] 
        self.temperature = temperature 

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.do_update(self.temperature)

    def set_temperature(self, temp):
        self.temperature = temp 
        self.notify()
#======================== Observer Part

class WeatherObserver(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod 
    def do_update(self, temperature):
        pass 


class View(WeatherObserver):
    def __init__(self, title):
        self.title = title 

    def do_update(self, temperature):
        print(f"{self.title}'s wall': temperature has changed to {temperature}")

def main():
    
    Nihad = View('Nihad')
    Murad = View('Murad')

    station = WeatherStation(18)
    station.add_observer(Nihad)
    station.add_observer(Murad)

    station.set_temperature(36)
    print()
    station.remove_observer(subscriber1)
    station.set_temperature(34)


if __name__ == "__main__":
    main()
