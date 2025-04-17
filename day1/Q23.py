'''roll=int(input("enter the roll no."))
name=input("enter name:")
marks=float(input("enter marks"))
cno=complex(input("enter comp no"))

print(roll, name, marks, cno)
'''
'''num=int(input("enter the no."))
print(bin(num))
print(hex(num))
print(oct(num))

'''
#bin  to int
'''bin_str=input("enter the str") #ob100
print(bin_str)
print(int(bin_str,base=2))
'''

#oct to int

bin_str=input("enter the str") #0o10
print(bin_str)
print(int(bin_str,base=8))

#hext to int

bin_str=input("enter the str") #0x100
print(bin_str)
print(int(bin_str,base=16))
