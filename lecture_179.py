#generators
# generators are iterators

# iterator, iterable

l=[1,2,3] # iterable

for i in l:
    print(i)
    
i=iter(l)
print(next(i))
    
for num in map(lambda a:a**2, l):
    print(num)