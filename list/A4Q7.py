l1=[22,33,22,4,5,33,33,5,6,44,2,1,44]
l2=[]
for i in l1:
	if i not in l2:
		l2.append(i)
print(l2)
################################################
for i in range(len(l1)):
	for j in range(len(l2)):
		if l1[i]==l2[j]:
			break
	else:
		l2.append(l1[i])
print(l2)

