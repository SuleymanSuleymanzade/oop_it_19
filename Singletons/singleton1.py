
class UniqueObject:
    _singleton = None 
    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(UniqueObject, cls).__new__(cls, *args, **kwargs)
        return cls._singleton 


def main():
    a1 = UniqueObject()
    a2 = UniqueObject()

    print(a1)
    print(a2)



if __name__ == "__main__":
    main()