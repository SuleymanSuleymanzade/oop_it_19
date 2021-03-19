import abc 
#= ============== Published part 
class PublisherInterface(metaclass = abc.ABCMeta):
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

class Publisher(PublisherInterface):
    def __init__(self, title):
        self.observers = [] 
        self.title = title 
        self.status = ""

    def get_title(self):
        return self.title 

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.do_update(self.status, self.get_title())

    def set_status(self, stat):
        self.status = stat 
        self.notify()
#======================== Observer Part (Subscriber)

class SubscriberInterface(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod 
    def do_update(self, status, title):
        pass

    def subscribe(self, observer):
        observer.add_observer(self)

    def unsubscribe(self, observer):
        observer.remove_observer(self)

class View(SubscriberInterface):
    def __init__(self, title):
        self.title = title 

    def do_update(self, status, title):
        print(f"[{self.title}'s wall'] {title}:\n     {status}")

class View2(SubscriberInterface):
    def __init__(self, title):
        self.title = title 

    def do_update(self, status, title):
        print('--------REPORT FROM {title}---------------------')
        print(f"<h1> {self.title} </h1> <p> T{status} <p>")
        print('-----------------------------------------------')

class TwitterUser:
    '''Publisher-Subscriber system Fasade'''
    def __init__(self, title):
        self.publisher = Publisher(title)
        self.subscriber = View(title)

    def get_publisher(self):
        return self.publisher 

    def get_subscriber(self):
        return self.subscriber

    def subscribe(self, obj):
        self.subscriber.subscribe(obj.get_publisher())

    def unsubscribe(self, obj):
        self.subscriber.unsubscribe(obj.get_publisher())

    def publish(self, status):
        self.publisher.set_status(status)

def main():
    '''
    Murad = Publisher('Murad')
    Ayaz  = View('Ayaz')

    Murad.set_status('hello today I was in BHOS')
    Ayaz.subscribe(Murad)
    Murad.set_status('Going back to home')
    '''

    Ayaz = TwitterUser('Ayaz')
    Murad = TwitterUser('Murad')

    Ayaz.subscribe(Murad)
    Murad.subscribe(Ayaz)

    Murad.publish("hello guys I'm here")
    Ayaz.publish("What's up guys")

if __name__ == "__main__":
    main()
