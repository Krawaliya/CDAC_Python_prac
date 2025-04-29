#example  of multilevel inheritance

class person:
	def __init__(self):
		self.name=input("Enter your name")
class employee(person):
	def __init__(self):
		super().__init__() #parent class __init__
		self.eid= int(input("enter your eid"))
	def display(self):
		print(self.name, self.eid)
class manager(employee):
	def __init__(self):
		super().__init__() #emp class init
		self.team_size=int(input("enter the tm_size"))
	#def display(self):
	#	print(self.name, self.eid, self.team_size)



e1=employee()
e1.display()
m1=manager()
m1.display()
