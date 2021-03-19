from enum import Enum 
from abc import abstractmethod 

class Relationship(Enum):
    PARENT = 0
    CHILD = 1 
    SIBLING = 2

class Person:
    def __init__(self, name):
        self.name = name 


class RelationshipBrowser:
    @abstractmethod 
    def find_all_children_of(self, name):
        pass 

class FamilyRelationship(RelationshipBrowser): #low level of abstraction 
    relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))
    
    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class RelationshipsChecker: # high abstraction
    ''' 
    def __init__(self, name, familyrelationships):
        relations = familyrelationships.relations # BIG BIG BIG PROBLEM Dependency Inversion breaks
        for r in relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                print(f'{name} has a child called {r[2].name}')
    '''
    def __init__(self, name, browser):
        for p in browser.find_all_children_of(name):
            print(f'{name} has a child called {p}')

def main():
    parent = Person('Murad')
    child = Person('Ayaz')
    child2 = Person('Elza')

    relationships = FamilyRelationship()
    relationships.add_parent_and_child(parent, child)
    relationships.add_parent_and_child(parent, child2)

    ch = RelationshipsChecker('Murad', relationships)

if __name__ == "__main__":
    main()

