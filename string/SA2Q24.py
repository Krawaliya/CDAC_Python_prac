sen=input("Enter the string:")
print(sen)
ch=input("enter the start char:")
print("without fun")
if sen[0]==ch:
	print("true")
else:
	print("False")
print("withfun")
if sen.startswith(ch,0):
	print("true")
else:
	print("false")

