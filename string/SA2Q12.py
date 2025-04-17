str1=input("enter the string:")
l1=str1.split(" ")
for i in l1:
	count=0
	for j in l1:
		if i==j:
			count=count+1
	print (i,":",count)
