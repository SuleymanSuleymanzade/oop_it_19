
global_list = ['first', 'second', 'third']


def func():
    buff = []
    for i in global_list:
        temp = i.upper()
        buff.append(temp)
    return  buff

def func2():
    for i in global_list:
        temp = i.upper()
        yield temp


def count_generator():
    c = 0
    while True:
        yield c
        c += 1

def main():
   for i in count_generator()
    

if __name__ == "__main__":
    main()