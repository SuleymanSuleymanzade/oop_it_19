import abc 
from enum import IntEnum 

class ATMHandler(metaclass = abc.ABCMeta):
    def __init__(self):
        self.next = None 

    @abc.abstractmethod 
    def handle_request(self, request):
        pass 

    def set_next_handler(self, handler):
        self.next = handler 

class HandlerOf50Manat(ATMHandler):
    def handle_request(self, amount):
        if amount >= 50:
            number_of_money = amount // 50
            reminder = amount % 50 
            print(f'{number_of_money} 50 AZN')
            if reminder > 0:
                self.next.handle_request(reminder)
        else:
            self.next.handle_request(amount)

class HandlerOf10Manat(ATMHandler):
    def handle_request(self, amount):
        if amount >= 10:
            number_of_money = amount // 10
            reminder = amount % 10 
            print(f'{number_of_money} 10 AZN')
            if reminder > 0:
                self.next.handle_request(reminder)
        else:
            self.next.handle_request(amount)

class HandlerOf5Manat(ATMHandler):
    def handle_request(self, amount):
        if amount >= 5:
            number_of_money = amount // 5
            reminder = amount % 5 
            print(f'{number_of_money} 5 AZN')
            if reminder > 0:
                self.next.handle_request(reminder)
        else:
            self.next.handle_request(amount)

class HandlerOf1Manat(ATMHandler):
    def handle_request(self, amount):
        if amount >= 1:
            number_of_money = amount // 1
            reminder = amount % 1 
            print(f'{number_of_money} 1 AZN')
            if reminder > 0:
                self.next.handle_request(reminder)
        else:
            self.next.handle_request(amount)
  
def create_chain_of_responsibility():
    ''' Create the chain '''
    root_50 = HandlerOf50Manat()
    ten  = HandlerOf10Manat()
    five = HandlerOf5Manat()
    one = HandlerOf1Manat()
    root_50.set_next_handler(ten)
    ten.set_next_handler(five)
    five.set_next_handler(one)
    return root_50

def main():
    root = create_chain_of_responsibility()
    root.handle_request(158)

if __name__ == "__main__":
    main()