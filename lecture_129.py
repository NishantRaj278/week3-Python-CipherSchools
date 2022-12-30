# set data type
s = {1,2,3,4,2}
print(s)

l=[1,2,2,3,4,5,5,5,5,5,6,7,1,]
# remove duplicate
s2=list(set(l))
print(s2)
s.add(9)
print(s)
s.remove(3)
print(s)
#
s1=s.copy()
print(s1)