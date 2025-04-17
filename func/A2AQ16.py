def sqr_no(num1,num2):
	sq_lt=[]
	for i in range(num1,(num2+1)):
		if i**0.5==int(i**0.5):
			sq_lt.append(i)
	print(sq_lt)
no1=int(input("enter the start no.:"))
no2=int(input("enter the start no.:"))
sqr_no(no1,no2)
