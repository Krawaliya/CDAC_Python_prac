#create class mart

class mmart:
	def __init__(self):
		self.items=["oreo", "goodday", "parle g"]
		self.area=2000
		self.owner="Krish"
		self.location="pune"
	def display(self):
		print(self.items, self.area, self.owner, self.location)
	def display_items(self):
		print(self.items)
	def display_details(self):
		print("owner:", self.owner,"location : ", self.location, " area : ", self.area)

m1=mmart()

m1.display_items()
m1.display_details()
