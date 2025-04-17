print("Welcome to DBDA")
print("1:chai,2:kaffi,3:juice")
choice=int(input("enter choice:"))
match choice:
	case 1:
		print("price of tea 12")
	case 2:
		print("price of kaffi 20")
	case 3:
		print("price of juice 30")
	case _:
		print("invalid input......")

