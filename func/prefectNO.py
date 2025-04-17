#write function to check if no. is perfect no. is not

def check_perfect_num(n):
	all_divisors=[]
	for num in range(1,n):
		if n%num==0:
			all_divisors.append(num)
	print(all_divisors)
	total=sum(all_divisors)
	if (total==n):
		print(n,"is a prefect no.")
	else :
		print(n,"is not a perfect no.")
num=int(input("enter the no."))
check_perfect_num(num)
