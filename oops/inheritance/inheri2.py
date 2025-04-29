class person:
	def __init__(self):
		self.name=input("Enter the name : ")
	def display(self):
		print(self.name)
class student(person):
	def __init__(self):
		super().__init__()
		self.rollno=int(input("Enter the roll no:"))
		self.marks=int(input("enter the marks: "))
		self.course=input("enter the course: ")
		self.skills=input("enter the skill")

	def display(self):
		print(self.name, self.rollno, self.marks,self.course, self.skills)
s1=student()
s1.display()
