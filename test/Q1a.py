st1=input("Enter the string:")
low=''
upe=''
st4='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z '
char_ls=st4.split(" ")


for i in st1:
	if  i in char_ls:
		upe=upe+i
	else:
		low=low+i
f_str=low+upe
print(f_str) 

