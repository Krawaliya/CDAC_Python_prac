l1=[2,4,6,8]
l2=[1,3,4,5,7]
for i in l1:
	if i in l2:
		print(i)
		print("there are common ele")
		break
else:
	print("there are no common ele")
