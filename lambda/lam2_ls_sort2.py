l1=["sss","ddd","fff","eee","abc","ba"]

sorted_ls=sorted(l1, key=(lambda x : x[1]))
print("with lambda:",sorted_ls)
def sec_char(s1):
	return s1[1]
sorted_ls=sorted(l1,key=sec_char)
print(sorted_ls)
