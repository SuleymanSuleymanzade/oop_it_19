import abc 

class SortingStrategy(metaclass = abc.ABCMeta):
    @abc.abstractclassmethod 
    def sort(self, data):
        pass 

class BubbleSort(SortingStrategy):
    def sort(self, data):
        for i in range(len(data)):
            for j in range(len(data) - i - 1):
                if data[j] < data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return (data, 'bubble_sort')


class MergeSort(SortingStrategy):
    def sort(self, data):
        return (sorted(data), 'merge_sort')


class Contex:
    def __init__(self, data, strategy):
        self.__data = data 
        self.__strategy = strategy
        #self.__strategy_status = ""

    def set_strategy(self, strategy):
        self.__strategy = strategy
         

    def get_data(self):
        return self.__data  

    def sort_by_strategy(self):
        return self.__strategy.sort(self.__data)

def main():
    d = [10, 2, 65, 23, 76, 34, 888, -1]
    
    merge_sort_strategy = MergeSort()
    contex = Contex(d, merge_sort_strategy)

    res = contex.sort_by_strategy()
    print(f'the data {d} is sorted {res[0]} by {res[1]} algorithm')
    
    bubble_sort_strategy = BubbleSort()
    contex.set_strategy(bubble_sort_strategy)
    res2 = contex.sort_by_strategy()
    print(f'the data {d} is sorted {res2[0]} by {res2[1]} algorithm')    

if __name__ == "__main__":
    main()