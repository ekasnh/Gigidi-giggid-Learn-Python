class Laptop:
	discount_percent = 10 
	count_instance = 0 
	def __init__(self,name,model,price):
		Laptop.count_instance += 1
		self.name = name
		self.age = model
		self.price = price
	@classmethod
	def from_string(cls,string):
		name,model,price = string.split(',')
		return cls(name,model,price)

	def apply_discount(self):
		off_price = (self.discount_percent/100)*self.price
		return self.price - off_price

p1 = Laptop("sajkasjksjk",90,19999)
p2 = Laptop("sajkasjksjk",90,19999)
Laptop.discount_percent = 50
print(p1.apply_discount())


#aek aur tareeka object create karne ka 


p2._price= 500
print(p2.price()) 