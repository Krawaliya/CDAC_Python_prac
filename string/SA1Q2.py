s1=input("Enter the string s1")
s2=input("Enter yhe string s2")
s3=''
mid=len(s1)//2
s3=s1[:mid]+s2+s1[mid:]
print(s3)
