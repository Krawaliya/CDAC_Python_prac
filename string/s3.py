s1="Restart"
new_st=s1[0]
f=s1[0]
for char in s1[1:]: #start from 2
	if char==s1:
		new_st=new_st+'$'
	else:
		new_st=new_st+char
