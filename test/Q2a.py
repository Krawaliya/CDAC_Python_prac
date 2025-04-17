eid_na=input("enter empId and name as: (empid_name):")
cnt=0
for i in eid_na:
	if i!='_':
		cnt=cnt+1
	else:
		break
id=int(eid_na[:cnt])
na=eid_na[(cnt+1):]
print("name:",na)
print(id)
vowel=['a','e','i','o','u']
vo_str=''

for i in range(2,id):
	if id%i==0:
		print("id is not prime")
		break
else:
	for i in na:
		if i in vowel:
			vo_str=vo_str+i
	print(vo_str)

if len(na)%2==1:
	print("cube of id:", id**3)

al_st=''
for i in range(len(na),2):
	al_st=al_st+na(i)
print(al_st)
