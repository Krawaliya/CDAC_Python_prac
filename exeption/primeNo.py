num=int(input("enter the no:"))
flag=0

for i in range (2,num):
	if i%2==0:
		print("not a prime")
		break
else:
	print("prime")
#####################################################
print("s2")
if num<2:
	print("not a prime")
elif num==2:
	print("prime")
elif num%2==0:
	print("not a prime")
else:
	for n in range(3, int(num**0.5)+1, 2):
		if num%n == 0:
			print("Not a prime")
			break
	else:
		print("prime")
#################################################
print("S3")

print("s2")
if num<2:
	print("not a prime")
elif num==2:
	print("prime")
elif num%2==0:
	print("not a prime")
else:
	for n in range(3, num/2, 2):
		if num%n == 0:
			print("Not a prime")
			break
	else:
		print("prime")
