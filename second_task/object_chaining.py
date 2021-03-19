class Calculator:

    def __init__(self, num):
        self.__num = num 

    def add(self, num):
        self.__num += num
        return self 

    def multiply(self, num):
        self.__num *= num
        return self 

    def minus(self, num):
        self.__num -= num
        return self 

    def result(self):
        return self.__num

    def __str__(self):
        return str(self.__num)

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, new_data):
        temp = self.head 
        while temp.next != None:
            temp = temp.next 
        temp.next = Node(new_data)
        return self 

    def traverse(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next 


ll = LinkedList(2)
ll.add(3).add(6).add(7)
ll.traverse()