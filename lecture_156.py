# map function

numbers=[1,2,3,4]

def square(a):
    return a**2

squares=list(map(square, numbers))
print(squares)

# list comp

squares_new=[i**2 for i in numbers]
print(squares_new)

newlist=[]
for num in numbers:
    newlist.append(square(num))
print(newlist)