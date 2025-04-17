st1=input("Enter the string:")
n_char=''
s_char=''
st4='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z'
char_ls=st4.split(" ")


for i in st1:
	if  i in char_ls:
		n_char=n_char+i
	else:
		s_char=s_char+i
f_str=n_char+s_char
print(f_str) 

