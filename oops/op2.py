#create a class person
#name, weight, height, age,
#Paopulstion(class variable)
class person:
	def __init__(self):
		self.name=input("enter your name:")
		self.weight=float(input("enter your weight:"))
		self.height=float(input("enter your height"))
		self.age=float(input("enter yourage"))
	def increase_population(cls):
		person.population +=1
	def display():
		print(self.name,self.weight,self.height, self.age)
p1=person()
p1.dispaly()
