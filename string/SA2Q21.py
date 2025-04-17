str=input("enter the str:")
s1='A,B,C,D,E,F,G,H,J,I,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'
l1=s1.split(",")
s2=str[:4]
counter=0
for i in s2:
	if i in l1:
		counter=counter+1
if counter>=2:
	str=str.upper()
print(str)
