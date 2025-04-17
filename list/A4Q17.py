l1[2,3,4,5,6]
for i in l1:
	if i>1:
		for j in range(2:i:):
			if i%j==0:
				print("False")
		else:
			print("True") 
