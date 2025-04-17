print("select the ops:")
print("1:bin->int, 2:oct->int, 3:hex->int")
ops=int(input())
match ops:
	case 1:
		num=input("enter bin no. start with 0b:")
		print(int(num,2))

	case 2:
		num=input("enter octal no. start with 0o:")
		print(int(num,8))
	case 3:
		num=input("enter hex no. start with 0x:")
		print(int(num,16))
	case _:
		print("invalid ops")
