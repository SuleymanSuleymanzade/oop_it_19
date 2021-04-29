import abc 

class ItemElement(metaclass=abc.ABCMeta):
    @abc.abstractmethod 
    def accept(self):
        pass 

class ShoppingCartVisitor(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def visit(self, item):
        pass

class Book(ItemElement):
    def __init__(self, price, isbn):
        self.price = price  
        self.isbn = isbn 

    def get_price(self):
        return self.price 

    def get_isbn(self):
        return self.isbn 

    def accept(self, visitor):
        return visitor.visit(self) 

class Fruit(ItemElement):
    def __init__(self, price, wt, nm):
        self.price = price 
        self.wt = wt 
        self.nm = nm 

    def get_price(self):
        return self.price 
    
    def get_weight(self):
        return self.wt 

    def get_name(self):
        return self.nm 

    def accept(self, visitor):
        return visitor.visit(self)

class ShoppingCartVisitorImpl(ShoppingCartVisitor):
    def visit(self, item):
        if isinstance(item, Book):
            cost = 0
            if item.get_price() > 50:
                cost = item.get_price() - 5 
            else:
                cost = item.get_price() 
            print(f"ISBN: {item.get_isbn()}, cost={cost}")
        elif isinstance(item, Fruit):
            cost = item.get_price() * item.get_weight() 
            print(f"ISBN: {item.get_name()}, cost={cost}")
        return cost 

class ItemCollection:
    def __init__(self, items):
        self.items = items
        self.allower_types = [Fruit, Book]

    def add_allowed_type(self, new_type):
        self.allower_types.append(new_type)

    def add_item(self, item):
        for allowed_type in self.allower_types:
            if isinstance(item, allowed_type): 
                self.items.append(item)

    def calculate_price(self, visitor):
        visitor:ShoppingCartVisitor = visitor
        sum = 0
        for item in self.items:
            sum += item.accept(visitor) 
        return sum 

def main():

    items = [
        Book(20, "4321"),
        Book(100, "6543"),
        Fruit(10, 2, "Banana"),
        Fruit(5, 5, "Apple")
    ]

    item_collection = ItemCollection(items)
    visitor:ShoppingCartVisitor = ShoppingCartVisitorImpl()
    total = item_collection.calculate_price(visitor)

    print(f"totalcost is {total}")

if __name__ == "__main__":
    main()
 


