print("select from given ops")
print("1:reverse||2:center of list|| 3:first 2 ele||4:last two||5: sqrt of no")
l1=[1,2,3,4,5,6,7,8,9,10]
print("list =",l1)
ch=int(input("enter ops"))
match ch:
	case 1:
		print(l1[::-1])
	case 2:
		print(l1)
	case 3:
		print(l1[:2])
	case 4:
		print("last two ele:",l1[-2:])
	case 5:
		l2=[]
		for i in l1:
			l2.append(i**2)
		print(l2)
