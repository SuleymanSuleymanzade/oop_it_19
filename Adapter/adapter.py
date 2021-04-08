class Volt:
    '''adaptee'''
    def __init__(self, volt):
        self.volt = volt 

    def get_volt(self):
        return self.volt 

    def set_volt(self, v):
        self.volt = v 

class SocketAdapter:
    def get_volt(self):
        return Volt(220)

class ConcretteAdapter(Socket):

    def convert_volt(self, v, i):
        return Volt(v.get_volt() / i)

    def get_220volt(self):
        return self.get_volt()

    def get_110volt(self):
        v = self.get_volt()
        return self.convert_volt(v, 2)

    def get_55volt(self):
        v = self.get_volt()
        return self.convert_volt(v, 4)

def produce_volt(sock_adapter, i):
    if i == 110:
        return sock_adapter.get_110volt()
    elif i == 220:
        return sock_adapter.get_220volt()
    else:
        return sock_adapter.get_55volt()

def main():
    sock_adapter: SocketAdapter = ConcretteAdapter()
    v1 = produce_volt(sock_adapter, 110)
    v2 = produce_volt(sock_adapter, 220)
    v3 = produce_volt(sock_adapter, 55 )

    print(v1.get_volt())
    print(v2.get_volt())
    print(v3.get_volt())
if __name__ == "__main__":
    main()