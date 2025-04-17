l1=['aaa','a','aaa','aaaaaa']
print(l1)
wordlen=0
lword=''

for word in l1:
	cnt=0
	for char in word:
		cnt=cnt+1
	if wordlen< cnt:
		wordlen=cnt
		lword=word
print(lword,wordlen)
