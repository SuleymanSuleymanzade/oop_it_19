from template_hook_with_singleton import Website 

class Ebay(Website):
    def find_max_price(self):
        print('in ebay.az we found the max prices')

    def filter_website(self, websites):
        ans = [word.lower() for word in websites]
        return ans 

    def query_website(self, n):
        a = ['first', 'second', 'third', 'fourth', 'fifth', 'six']
        if n <= 5:
            return a[:n]
        else:
            return a[0] 

        
def main():
    ebay:Website = Ebay()
    res = ebay.get_n_websites(3)
    for i in res:
        print(i)

if __name__ == "__main__":
    main()
