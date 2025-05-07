s1= input("enter the floating points")
try:
	num1=float(s1)
except ValueError:
	print("problem in floating points")
	raise TypeErrr
num2 = input("Enter the no")
if "*" in num2: 
	l1=num2.split("*")
	for n in l1:
		if n.isdigit()==False:
			raise TypeError
else:
	if num2.isdigit()==False:
		raise TypeError
