def mul(n1,n2):
	mul_ans=n1*n2
	return mul_ans

def fact(n1):
	fact=1
	for num in range(n1,1,-1):
		fact=mul(num,fact)
	print(fact)
n1=int(input("Enter the no."))
fact(n1)

################################################################
def fac_rec(n1):
	if n1>=1:
		return n1*fac_rec(n1-1)
	else :
		return 1
print("rec fun")
res=fac_rec(n1)
print(res)
