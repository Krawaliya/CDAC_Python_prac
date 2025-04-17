num=int(input("enter the no."))
total=0
'''
for i in range(1,(num+1)):
	total=total+((10**i)-1)
	print((10**i)-1)
'''
for i in range (1,(num+1)):
	print('9'*i)
	total=total+int('9'*i)
print("sum:",total)
