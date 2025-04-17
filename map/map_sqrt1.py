#take list of char as input 
#convert every char to int
# assume every char is a digit

#inp= l1=["8","6,"9"]

#op[8,6,9]

def func1(s1):
	return int(s1)
l1=["2","7","4","6"]
int_digit=map(func1,l1)
print(list(int_digit))
