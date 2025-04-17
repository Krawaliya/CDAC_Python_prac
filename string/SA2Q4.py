def replace_first_char(s1):
	s2=s1[:1]
	for i in range(1,len(s1)):
		if i==s1[0]:
			s2=s2+'$'
		else :
			s2=s2+i
	print(s2)
s1="restart"
replace_first_char(s1)
