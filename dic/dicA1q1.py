from operator import itemgetter
d1={1:1,'a':2,'c':3,3:4}
print(d1)
sor_ace=dict(sorted(d1.items(),key=itemgetter(1)))
print("acendind:",sor_ace )
sor_dic1=dict(sorted(d1.items(),key=itemgetter(1),reverse=True))
print("decending:",sor_dic1)
