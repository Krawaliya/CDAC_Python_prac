#sort first string on pasition of char  on second str
#s1="IACSD"
#s2="zdsaikjlc"
#out=['d','s','a','i','c']

st1="IACSD"
st2="ZDSAIKJLC"

sort1= sorted(st1, key=(lambda s: st2.find(s)))
print(sort1)


def pos(char):
	return st2.find(char)

sort2= sorted(st1, key = pos)
print(sort2)
