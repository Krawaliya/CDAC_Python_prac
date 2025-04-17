#sort given string in reverse

s1="IACSD"
def func1(char):
	return -ord(char)
sorted_s1=sorted(s1,key=func1)
print(sorted_s1)
sorted_s1=sorted(s1,key=(lambda x: -ord(x)))
print(sorted_s1)


