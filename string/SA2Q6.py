s1=input("enter the st:")
if len(s1)<3:
	print('nothing change:',s1)
else:
	if s1[-3:]=='ing':
		s2=s1[:-3]+'ly'
		print(s2)
	else:
		s2=s1+'ing'	
		print(s2)
