s1=input("enter the str:")
words=s1.split(" ")
#count total eords
noofwords=len(words)
print(noofwords)
cnt=0
#avg char in word
for word in words:
	for char in word:
		cnt=cnt+1
avg=cnt/noofwords
print(avg)
#combine all words without space print result in  reverse
s2=''.join(words)
print(s2[::-1])
#from the given sentence all the cap letter come at the end and result should not have any spaces
capStr=''
lowStr=''
for letter in s2:
	if letter.isupper():
		capStr=capStr+letter
	else:
		lowStr=lowStr+letter
s3=lowStr+capStr
#method 2
s4=s2.sort()
print(s4)
print(s3)
