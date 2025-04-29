class college:
	def __init__(self,name,capacity):
		self.name=name
		self.capacity=capacity
	def display(self):
		print(self.name, self.capacity)
class MBA_clg(college):
	def __init__(self,name,capacity,placement):
		super().__init__(name, capacity)
		#college.__init__(self,name,capacity)
		self.placement=placement
	def display(self):
		print(self.name, self.capacity, self.placement)
c1= college("ABC",120)
c1.display()
c1=MBA_clg("XYZ",254,200)
c1.display()
