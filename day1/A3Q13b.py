import math
num=int(input("enter the no.:"))
sqt=math.sqrt(num)
print("sqrt of ",num,"is :",sqt)

if sqt.is_integer():
	print(sqt,"is integer")
else:
	print(sqt,"is not int")

