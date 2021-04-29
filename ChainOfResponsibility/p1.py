import abc 

class WebsiteScraper(metaclass = abc.ABCMeta):
    def __init__(self):
        pass
    @abc.abstractclassmethod
    def get_data(self , d):
        pass 

class TapAzScraper(Website):
    def __init__(self):
        pass 

    def get_data(self, d):
        d = self.d 


class AmazonScraper(Website):
    def __init__(self):
        pass 

    def get_data(self, d):
        d = self.d      

    
class Filter:
    def __init__(self, scraper: Website):
        self.scraper = scraper 

def main():
    
    tapazscraper: WebsiteScraper  = TapAzScraper()
    amazonscraper: WebsiteScraper = AmazonScraper() 
    
    filter  = Filter(tapazscraper)
    filter2  = Filter(amazonscraper)

if __name__ == "__main__":
    main()