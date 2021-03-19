import abc 

class AbstractPizza(metaclass = abc.ABCMeta):
    @abc.abstractclassmethod 
    def get_price(self):
        pass 

    @abc.abstractclassmethod 
    def get_status(self):
        pass 

class Margarita(AbstractPizza):
    def get_price(self):
        return 3.0 

    def get_status(self):
        return "Margarita Pizza\n"

class Pepperoni(AbstractPizza):
    def get_price(self):
        return 5.0 

    def get_status(self):
        return "Pepperoni Pizza\n"

class PizzaDecorator(AbstractPizza):
    def __init__(self, pizza):
        self.pizza = pizza 

    def get_price(self):
        return self.pizza.get_price() 

    def get_status(self):
        return self.pizza.get_status()

class Tomato(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza) 

    def get_price(self):
        p = super().get_price()
        return p + 1 

    def get_status(self):
        temp = super().get_status()
        return temp  + "added tomato\n"


class Cheese(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_price(self):
        p = super().get_price()
        return p + 2 

    def get_status(self):
        temp = super().get_status()
        return temp + "added cheese\n"

# Facade 
class PizzaManager:
    def __init__(self, pizza_sort):
        self.extentions = [] 
        self.pizza = pizza_sort() 

    def add_extention(self, title):
        self.extentions.append(title)

    def produce_extentions(self):
        for ex in self.extentions:
            if ex == 'tomato':
                self.pizza = Tomato(self.pizza)
            elif ex == 'cheese':
                self.pizza = Cheese(self.pizza)

    def get_price(self):
        return self.pizza.get_price()

    def get_status(self):
        return self.pizza.get_status() 

def main():

    '''
    pizza = Tomato(Tomato(Cheese(Tomato(Margarita()))))
    print(pizza.get_price())
    print(pizza.get_status())
    '''

    pizza = PizzaManager(Pepperoni)
    pizza.add_extention('tomato')
    pizza.add_extention('cheese')
    pizza.add_extention('cheese')
    
    pizza.produce_extentions()

    print(pizza.get_price())
    print(pizza.get_status())



if __name__ == "__main__":
    main()