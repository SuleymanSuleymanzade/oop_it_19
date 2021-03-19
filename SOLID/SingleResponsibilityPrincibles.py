# solve the problem of the GOD Object antipattern

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # break Single responsibility princibles
    ''' 
    def save(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()

    def load(self):
        pass

    def load_csv(self):
        pass
    def load_from_db(self):
        pass
    '''

class PersistenceManager:
    def save(self, journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()

    def load(self, filename):
        pass

def main():
    j = Journal()
    j.add_entry("I bought a pizza today")
    j.add_entry("I play PS5")
    j.add_entry("I'm tired")
    #print(j)

    p = PersistenceManager()
    file = f"journal_file.txt"
    p.save(j, file)

    with open(file, 'r') as f:
        print(f.read())

if __name__ == "__main__":
    main()

