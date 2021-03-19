from abc import astractmethod
import abc 

class Machine:
    def print(self, document):
        raise NotImplementedError() 

    def fax(self, document):
        raise NotImplementedError
    
    def scan(self, document):
        raise NotImplementedError

class MultiFunctionalMachine(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass
    
    def scan(self, document):
        pass


class OldFashionPrinter(Machine):
    def print(self, document):
        # ok old printer they can print 
        pass 

    def fax(self, document):
        pass # does nothing 

    def scan(self, document):
        '''Not supported'''
        raise NotImplementedError("Printer cannot scan")

# Factory Method design pattern: from the design pattern 

