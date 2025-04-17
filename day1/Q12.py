num=int(input("enter the no."))
total=0
'''for i in range(num):
	if i%2!=0:
		total=total+i
'''
for i in range(1,num,2):
	total=total+i
print (total)
