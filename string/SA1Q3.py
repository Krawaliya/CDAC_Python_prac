s1=input("Enter the s1")
s2=input("enter the s2")
m1=len(s1)//2
m2=len(s2)//2
s3=s1[0]+s2[0]+s1[m1]+s2[m2]+s1[-1]+s2[-1]
print(s3)
