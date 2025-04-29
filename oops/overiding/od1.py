class point :
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __str__(self):
		return "point is x : "+ str(self.x) + 'y' + str(self.y)

	@staticmethod
	def dist(p1,p2):
		point_dist=((p1.x-p2.x)**2+(p1.y-p2.y)**2)**0.5
		return point_dist


	def __add__(self,other):
		if isinstance(other, (int,float)):
			new_x=self.x + other
			new_y=self.y + other
		else:
			new_x=self.x + other.x
			new_y=self.y + other.y

		new_point= point(new_x, new_y)
		return new_point


	def __radd__(self,other):
		if isinstance(other, (int,float)):
			new_x=self.x + other
			new_y=self.y + other
		else:
			new_x=self.x + other.x
			new_y=self.y + other.y
		new_point= point(new_x, new_y)
		return new_point

	def __sub__(self, other):
		new_x=self.x - other.x
		new_y=self.y - other.y
		new_point= point(new_x, new_y)
		return new_point

	def __mul__(self, other):
		new_x=self.x * other.x
		new_y=self.y * other.y
		new_point= point(new_x, new_y)
		return new_point
		

p1=point(10,10)
p2=point(20,20)
print(p1)
print(p2)
print(point.dist(p1,p2))
print(p1+p2)
print(p1+40)
print(50+p1)
print(p1-p2)
print(p1*p2)
