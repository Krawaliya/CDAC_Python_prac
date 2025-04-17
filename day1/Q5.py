#!/user/bin/python
num=int(input("enter the no.:"))
count=0
sum=0
mul=1
while num!=0:
	q=num%10
	sum=sum+q
	mul=mul*q
	num=num//10
	count=count+1
print("count of no =",count)
print("mul of no =",mul)
print("sum of no =",sum)
