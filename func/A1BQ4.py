def prime(no):
	for i in range(2,no):
		if no%i==0:
			return False
			break
	else:
		return True
no=int(input("Enter the no."))
res=prime(no)
print(res)
