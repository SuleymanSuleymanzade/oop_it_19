import abc 

class User(metaclass = abc.ABCMeta):
    def __init__(self, med, name):
        self.med = med 
        self.name = name 

    @abc.abstractclassmethod 
    def send(self, msg):
        pass 

    @abc.abstractclassmethod
    def receive(self, msg):
        pass 

class ChatMediator:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, msg, user):
        for u in self.users:
            if u != user:
                u.receive(msg)

class ChatUser(User):
    def send(self, msg):
        print(f'STATUS: {self.name} user seding "{msg}" message!')
        self.med.send_message(msg, self)
    
    def receive(self, msg):
        print(f"{self.name} Received: {msg}")

def main():

    mediator = ChatMediator()
    
    murad = ChatUser(mediator, 'Murad Abdullayev')
    ayaz = ChatUser(mediator, 'Ayaz Panahov')
    eljan = ChatUser(mediator, 'Eljan Abbaszade')
    asmar = ChatUser(mediator, 'Asmar Hajizade')

    mediator.add_user(murad)
    mediator.add_user(ayaz)
    mediator.add_user(eljan)
    mediator.add_user(asmar)

    murad.send('hello guys I created the groug')
    ayaz.send('Nice now we can talk')

if __name__ == "__main__":
    main()