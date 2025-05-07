n1=0
n2=1
l1=[0,1]
sum=0
rep= int(input("enter the rep no."))
for i in range(rep-2):
#	if  rep-2<1:
#		break
#	else:

		sum=n1+n2
		l1.append(sum)
		n1=n2
		n2=sum
print(l1)
