def fucn1_handler(a,b):
	try:
		#quarantine
		c=a/b
		print(c)
	except ZeroDivisionError:
		print("there is zero dev erre")
	except ArithmeticError:
		print("there is arithmetiac erre")
	except exception :
		print("there is prob")

