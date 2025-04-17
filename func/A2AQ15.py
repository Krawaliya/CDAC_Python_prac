def sort_hyphen(s1):
	lt1=s1.split("-")
	lt1.sort()
#	print(lt1)
	s2="-".join(lt1)
	print(s2)
str1=input("Enter the str with'-':")
sort_hyphen(str1)
