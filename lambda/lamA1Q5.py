#take emp id and anme in dic
#sort by key empid 
#sort  by value name
dic1={1:"aa",2:"bb",3:"cc",4:"ee"}
#sort by id
sorted_emp=sorted(dic1)
#return list
print(sorted_emp)

sorted_emp_dic={}
for k in sorted_emp:
	sorted_emp_dic[k]=dic1[k]
print(sorted_emp_dic)
##
#sort on name
'''
ls=[]
for i in dic1:
	ls.append(dic1[i])
ls.sort()
emp_sort_name={}
for i in ls:
	ind=dic1.find(i)
	emp_sort_name[ind]=ls[i]
print(emp_sort_name)
'''
sorted_val=sorted(dic1.values())
print(sorted_val)

sorted_emp_name={}
for val in sorted_val:
	key=None
	for k,v in dic1.items():
		if v == val:
			key=k
			break
	sorted_emp_dic[key]=val
print(sorted_emp_dict)


#################
#SORT DIC ON VAL
sort_keys=sorted(emp, key=(lambda k: emp[k]))
sorted_emp_dict={}
for k in sorted_keys:
	sorted_emp_dic[k]=emp[K]
print(sorted_emp_dict)
