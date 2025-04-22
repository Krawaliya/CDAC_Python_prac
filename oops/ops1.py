class student:
	def __init__(self):
		self.name=input("Enter your name")
		self.rollno=input("enter roll no")
		self.mod1marks=input("mod1 marks")
		self.mod2marks=input("mod2 marks")

	def display(self):
		print(self.name,self.rollno)
		print(self.mod1marks,self.mod2marks)
s1=student()
s1.display()
