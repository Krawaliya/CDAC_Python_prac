class base:
	def func1(self):
		print("in base class")
#class derived:
class derived(base):
	def func1(self):
		super().func1()
		print("in derived class")
d1= derived()
d1.func1()
