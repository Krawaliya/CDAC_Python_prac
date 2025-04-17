x=int(input("enter the value of x:"))
n=int(input("enter the value of power"))
sum=0
for i in range(n):
	print(x,'^',i,"/",i,"!")
	sum=sum+((x**i)/(math.factorial(i)))
print(sum)
