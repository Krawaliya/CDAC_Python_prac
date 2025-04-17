s1=input("enter string of odd length:")
if len(s1)>7 and len(s1)%2==1:
	mid=len(s1)//2
	res=s1[mid-1:mid+2]
	print(res)
else:
	print("enter str correctly")
