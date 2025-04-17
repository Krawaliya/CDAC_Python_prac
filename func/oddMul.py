def mul(a,b):
	c=a*b
	return c
ans=1
for i in range(1,100,2):
	ans=mul(i,ans)
print(ans)
