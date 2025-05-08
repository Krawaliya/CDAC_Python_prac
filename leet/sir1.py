l_b_b=[]
l_b_l_e=[]
l_b_l_o=[]
l_a_w_l=[]
for i in range(1,101,1):
	l_b_b.append(i);
print("plates order before breakfast:",l_b_b[::-1])

for i in range(len(l_b_b)):
	n=l_b_b.pop()
	if n%2==0:
		l_b_l_e.append(n)
	else:
		l_b_l_o.append(n)
print("plate on lunch at even counter is: " , l_b_l_e[::-1])
print("plate on lunch at odd counter is: " , l_b_l_o[::-1])
for i in range(len(l_b_l_e)):
	wash=[]
	if len(l_b_l_o)>=2:
		a=l_b_l_o.pop()
		wash.append(a)
		c=l_b_l_o.pop()
		wash.append(c)
	b=l_b_l_e.pop()
	wash.append(b)
	wash.sort()
	l_a_w_l.extend(wash)
print("list after lunch wash:",l_a_w_l[::-1])


