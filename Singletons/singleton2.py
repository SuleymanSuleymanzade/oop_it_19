class MetaSingleton(type):
    __instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]

class UniqueObj(metaclass = MetaSingleton):
    def __init__(self, name, sname):
        self.name = name 
        self.sname =sname 

class OnlyHuman(metaclass = MetaSingleton):
    def __init__(self, name, sname, email):
        self.name = name 
        self.sname = sname 
        self.email = email 

def main():

    uo1 = UniqueObj('Kamran', 'Mammadov')
    print(uo1)
    del uo1

    uo2 = UniqueObj('Ayaz', 'Panahov')
    print(uo2)
    #print(f"{uo1.name} {uo1.sname}")
    print(f"{uo2.name} {uo2.sname}")

    oh1 = OnlyHuman('Ayaz', 'Panahov', 'ayaz.panahov@bhos.edu.az')
    oh2 = OnlyHuman('Eljan', 'Abbaszade', 'eljan.abbaszade@bhos.edu.az')

    print(oh1.name)
    print(oh2.name)

if __name__ == "__main__":
    main()