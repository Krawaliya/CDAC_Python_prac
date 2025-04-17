def palindrom(s1):
	s2=s1[::-1]
	for i in range(len(s2)):
		if s2[i]==s1[i]:
			return True
		else :
			return False
s1=input("enter the string:")
res=palindrom(s1)
print(res)
