from typing import List, Set 
import datetime 

class Customer:
	def __init__(self, name, sname, email):
		self.__name = name
		self.__sname = sname 
		self.__email = email 

	@property
	def name(self):
		return self.__name

	@property
	def sname(self):
		return self.__sname
	
	@property
	def email(self):
		return self.__email

	@email.setter
	def email(self, new_email):
		self.__email = new_email	

	def __str__(self):
		return f"{self.__name} {self.__sname}"

	def __repr__(self):
		return f"{self.__class__.__name__}({self.__name}, {self.__sname}, {self.__email})"


class UnsubscribedCustomer(Customer):
	def __init__(self, name, sname, email):
		super().__init__(name, sname, email)

	def __str__(self):
		return super().__str__() + " :Unsubscribed"


class SubscribedCustomer(Customer):
	def __init__(self, name, sname, email, phone_number):
		super().__init__(name, sname, email)
		self.__phone_number = phone_number

	@property 
	def phone_number(self):
		return self.__phone_number 

	@phone_number.setter
	def phone_number(self, new_phone):
		self.__phone_number = new_phone 

	def __str__(self):
		return super().__str__() + " :Subscribed"

#-------------------------------------------------------

class Artist:
	def __init__(self, name, sname):
		self.__name = name 
		self.__sname = sname 
		self.__bio = ""

	@property
	def name(self):
		return name 

	@property
	def sname(self):
		return self.__sname

	@property
	def bio(self):
		return self.__bio

	@bio.setter
	def bio(self, b):
		self.__bio = b 

class CD:
	def __init__(self, artists:List[], title, content, price):
		self.__price = price 
		self.__content = content 
		self.__artists = []
		self.__artists.extends(artists)
		self.__title = title

	@property
	def title(self):
		return self.__title 

	@property 
	def artists(self):
		return self.__artists 

	@property
	def content(self):
		return self.__content

	@property 
	def price(self):
		return self.__price 

class Basket:
	def __init__(self, customer: Customer, cd: CD):
		self.__customer = customer 
		self.__datetime = datetime.datetime.now()
		self.__basket = []
		self.__basket.append(cd)
		self.__discount = 0

	@property
	def discount(self):
		return self.__discount

	@discount.setter(self)
	def discount(self, dis_p):
		self.__discount = dis_p
	 


	def get_cd(self, title):
		for cd in self.__basket:
			if cd.title == title:
				return cd  
		return None

	def add_cd(self, cd: CD):
		self.__basket.append(CD)

	def remove_cd(self, title):
		for id, cd in enumerate(self.__basket):
			if cd.title == title:
				del self.__basket[id]
				return 

	@property
	def customer(self):
		return self.__customer

	def get_prices(self):
		total =  sum([cd.price for cd in self.__basket])
		return total - (total / 100) * self.discount


class History:

	def __init__(self):
		self.__deals = []


	def add_deal(self, d):
		self.__deals.append(d)

	def reset(self):
		self.__deals = []

	def show_history(self):
		res = []
		for deal in self.__deals:
			cds = [cd.title for cd in deal]
			res.append(cds, self.get_prices, self.__datetime)
		return res 