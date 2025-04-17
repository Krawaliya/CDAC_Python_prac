st=input("enter the string")
nstr=''
if len(st)<2:
	print(nstr)
else:
	nstr=nstr+st[:2]+st[-2:]
print(nstr)
