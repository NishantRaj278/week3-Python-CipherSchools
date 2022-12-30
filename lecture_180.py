# create your first generator with generator function

def nums(n):
    for i in range(1,n+1):
        yield(i)
        


numbers=nums(10)
for n in numbers:
    print(numbers)