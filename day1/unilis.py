
l1=[2,3,4,22,3,2]
l2=[]
for i in l1:
	if i not in l2:
		l2.append(i)
print(l2)

#############################
l3=[]
for i in range(len(l1)):
	for j in range(len(l3)):
		if l1[i]==l3[j]:
			break
	else:
		l3.append(l1[i])
print(l3)
###########################
print(l1[3],l1[-5])
print(l1[2:5])
