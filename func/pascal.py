def pascal_tree()
n=int(input("enter the row no."))
prev_r=[1]
print(prev_r)
curr_r=[]
for row_no in range(n):
	curr_r.append(1)
	for i in range(1,len(prev_r)):
		s=prev_r[i-1]+prev_r[i]
		curr_r.append(s)
	curr_r.append(1)
	print(curr_r)
	prev_r=curr_r
	curr_r=[]
