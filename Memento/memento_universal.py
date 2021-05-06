def copy_object_util(obj1, mem_obj):
    for k, v in mem_obj.__dict__.items():
        if k not in obj1.__dict__:
            obj1.__dict__[k] = v 

class Memento:
    def __init__(self, mem_obj):
        #copy_object_util(self, object_)
        for k, v in mem_obj.__dict__.items():
            if k not in self.__dict__:
                self.__dict__[k] = v           

class FileWriterUtil:
    def __init__(self, file):
        self.file = file 
        self.content = ""

    def write(self, str_):
        self.content += str_

    def save(self):
        return Memento(self)

    def undo(self, memento):
        self.__dict__ = memento.__dict__

class FileWriterCaretaker:
    def save(self, writer):
        self.obj = writer.save() 

    def undo(self, writer):
        writer.undo(self.obj)

def main():

    caretaker = FileWriterCaretaker()
 
    writer = FileWriterUtil("./data.txt")
    writer.write('the new line\n')

    caretaker.save(writer)

    writer.write("second set of data\n")
    
    print(writer.content)
    caretaker.undo(writer)
    print('<after undo operation>')

    print(writer.content)


if __name__ == "__main__":
    main()


