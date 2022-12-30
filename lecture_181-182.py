# example

def even_generator(n):
    for num in range(1,n+1):
        if num%2==0:
            yield(num)
            
for num in even_generator(20):
    print(num)