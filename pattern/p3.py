li=int(input("Enter no. of lines:"))
for i in range(0,(li//2)+1):
	print(" "*(li-(i*2))+'*'*(i*2)+'*')
###########################

for i in range(1,(li//2)+1):
	print(" "*((i*2)+1)+"*"*((li-(i*2))))
print("p1")

for i in range(0,(li//2)+1):
	print(" "*(li-i)+'*'*i)
###########################

for i in range(1,(li//2)+2):
	print(" "*(i+1)+"*"*((li-i)-1))


