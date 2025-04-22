#create class shape
#height, width, length
#display> instance method
#display_count --> class ,ethod
#streech __> static method

class shape:
	def __init__(self):
		self.height=10
		self.width=20
		self.length=100
	def display(self):
		print(self.height,self.width, self.length)

	@classmethod
	def display_count(cls):
		print("this is class method")
	@staticmethod
	def stretch():
		print("this is ststic method")

sh1=shape()
sh1.display()
#shape.dispaly() #error

#call class method
shape.display_count()
sh1.display_count()

#calling static method
shape.stretch()
sh1.stretch()  #error in old vresion
