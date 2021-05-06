class Memento:
    def __init__(self, file, content):
        self.file = file 
        self.content = content 

class FileWriterUtil:
    def __init__(self, file):
        self.file = file 
        self.content = ""

    def write(self, str_):
        self.content += str_

    def save(self):
        return Memento(self.file, self.content)

    def undo(self, memento):
        self.file = memento.file 
        self.content = memento.content 

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


