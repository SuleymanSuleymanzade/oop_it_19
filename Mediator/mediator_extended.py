import abc 

class User(metaclass = abc.ABCMeta):
    def __init__(self, med, name):
        self.med = med 
        self.med.add_user(self)
        self.name = name

    def swap_group(self, new_mediator):
        self.med.remove_user(self)
        self.med = new_mediator 
        self.med.add_user(self)


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

    def remove_user(self, user):
        self.users.remove(user)

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

    chat_group1 = ChatMediator()
    chat_group2 = ChatMediator()

    murad = ChatUser(chat_group1, 'Murad Abdullayev')
    ayaz = ChatUser(chat_group1, 'Ayaz Panahov')
    eljan = ChatUser(chat_group1, 'Eljan Abbaszade')
    #asmar = ChatUser(mediator, 'Asmar Hajizade')
    '''
    mediator.add_user(murad)
    mediator.add_user(ayaz)
    mediator.add_user(eljan)
    mediator.add_user(asmar)
    '''

    murad.send('hello guys I created the groug')
    ayaz.send('Nice now we can talk')
    print()
    ayaz.swap_group(chat_group2)
    eljan.swap_group(chat_group2)
    ayaz.send('hello Eljan now we have separated group')

if __name__ == "__main__":
    main()