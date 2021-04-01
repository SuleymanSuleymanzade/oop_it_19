class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Website:
    ''' Template '''
    def search_site(self):
        pass

    def get_detail(self):
        pass

    def find_max_price(self):
        pass
    
    def query_website(self, n):
        pass

    def filter_website(self, websites):
        pass 

    def algorithm(self):
        self.search_site()
        self.get_detail()
        self.find_max_price()

    def get_n_websites(self, n):
        temp = self.query_website(n)
        ans = self.filter_website(temp)
        return ans         

class TapAz(Website, metaclass = MetaSingleton):
    ''' Hook '''
    def get_detail(self):
        print('shows detail from Tap.az')

    def search_site(self):
        print('We search in Tap.az')

    def find_max_price(self):
        print('in Tap.az we found the max prices')

    def query_website(self, n):
        a = ['first', 'second', 'third', 'fourth', 'fifth', 'six']
        if n <= 5:
            return a[:n]
        else:
            return a[0] 

    def filter_website(self, websites):
        ans = [word.upper() for word in websites]
        return ans 

'''
class Amazon(Website):
    # hook part
    def get_detail(self):
        print('shows detail from Amazon.az')

    def search_site(self):
        print('We search in Amazon.az')

    def find_max_price(self):
        print('in Amazon.az we found the max prices')
'''
'''
def main():
    tapaz: Website = TapAz()
    #tapaz.algorithm()
    res = tapaz.get_n_websites(2)
    print(res)
    print(tapaz)
    del tapaz 

    tapaz: Website = TapAz()
    print(tapaz)

if __name__ == "__main__":
    main()
'''