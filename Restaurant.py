import threading

commands = ["hour", "name", "price", "rating", "open"]

class Restaurant(object):
    

	def __init__(self, name, price, open_now, rating):
         self.name = name
         self.price = price
         self.open_now = open_now
         self.rating = rating
 
    	 def display(self):
         	print("Restaurant: ", self.name, "\n Price Range: ", self.price, "\n Open: ", self.open_now, "\n Rating: ", self.rating)
 
    	 def getName(self):
         	print("Restaurant: ", self.name, "\n")
 
    	 def getPrice(self):
         	print("Price Range: ", self.price, "\n")
 
    	 def getOpen(self):
         	print("Open: ", self.open_now, "\n")
 
     	def getRating(self):
        	 print("Rating: ", self.rating, "\n")
