class cooler:
	def __init__(self):
		self.brand=input("Enter Brand")
		self.airflow=60
		self.swing=True

	def __str__(self):
		#returns string representation of the object
		return "Brand="+ self.brand + "airflow" + str(self.airflow)+ "Swing" + str(self.swing)

c1=cooler()
print(c1) # this call str method
