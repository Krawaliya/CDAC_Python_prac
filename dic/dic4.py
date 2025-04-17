sen="exam is an opportunity exam gives us lesson"
sen_li=sen.split(" ")
word_count=dict()

for i in sen_li:
	counter=0
	for j in sen_li:
		if i==j:
			counter=counter+1
	word_count[i]=counter
print(word_count)
for i in  sen_len:
	word_count[word]=words.count(word)
print(word_count)
