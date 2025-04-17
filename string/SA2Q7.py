s1='the lyrics is not that poor'
s2="the lyrics is poor"
notpo1=s1.find("not")
poorpo1=s1.find("poor")
print("position of not in s1 :",notpo1)
print("position of poor in s1 :",poorpo1)

if notpo1<poorpo1 and (notpo1 != -1) and (poorpo1 != -1):
	s3=s1[:notpo1]
	s4=s1[poorpo1+len("poor"):]
	s5=s3+' good '+s4
	print(s5)
else:

	print(s1)
