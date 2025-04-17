#wrt to take list 
#and find sqrt of every no in list
l1=[10,20,30]

sqrt_l1=map((lambda x:x**0.5), l1)
print(sqrt_l1)
for i in sqrt_l1:
	print(i)
sqrt_l1=map((lambda x:x**0.5), l1)

print(list(sqrt_l1))
