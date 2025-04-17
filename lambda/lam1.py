#sort using lambda in reverse

l1=[1,2,3,4,55,667]
def neg(n):
	return -n
sorted_l=sorted(l1,key=neg)
print("by fun:",l1)

l2=[1,3,4,5,6,7,8]
sorted_l2=sorted(l2,key=(lambda x:x))
print("by lambda", l2)
