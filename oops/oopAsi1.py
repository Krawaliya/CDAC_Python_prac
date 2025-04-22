class employee:
	#compan_ name can also assign here
	def __init__(self):
		self.emp_id=int(input("enter the emp id:"))
		self.name=input("enter the name:")
		self.desig=input("designamtion")
		self._sal=10000
		employee.company="google"
		
		
	def display_project(self):
		print("display all project ids")
	def dispaly_id(self):
		print("dispalay identiyi")
	def cheak_rev_skill(self):
		print("dsfa")
	
	@classmethod
	def display_company_details(cls):
		print(cls.company)

e1=employee()
e1.dispaly_id()
e1.display_company_details()
print(__dict__)
print(__name__)

