#!/user/bin/python
sum=0
count=0
ch=0
while ch!='q':
	num=int(input("enter the no.:"))
	ch=input("press q to exit ")
	sum=sum+num
	count=count+1
print("sum",sum)
avg=sum/count
print(avg)
print("you have enterned Q")




