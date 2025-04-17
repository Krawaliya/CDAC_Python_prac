l1=[10,20,30,40,88,9]
l2=[43,23,13,17]
if len(l2)<len(l1):
	for i in range(len(l2)):
		print(l1[i],l2[i])
if len(l1)<len(l2):
	for i in range(len(l1)):
		print(l1[i],l2[i])
