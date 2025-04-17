num=int(input("enter the no."))
n=num
bit_lis=[]
while n!=num:
	bit=n%2
	n=n/2
	bit_lis.append(bit)
print(bit_lis[::-1])
