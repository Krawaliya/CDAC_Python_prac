num1=int(input("enter the num 1:"))
num2=int(input("enter yhe num 2:"))
print("1:add, 2:sub, 3:mul, 4:div")
choice=int(input("enter ops:"))
match choice:
	case 1:
		print("sum of ",num1,", and ", num2,"is:", num1+num2)
	case 2:
		print("sub of ",num1,", and ", num2,"is:", num1-num2)
	case 3:
		print("mul of ",num1,", and ", num2,"is:", num1*num2)
	case 4:
		print("div of ",num1,", and ", num2,"is:", num1/num2)
	case _:
		print("invalid ops")
