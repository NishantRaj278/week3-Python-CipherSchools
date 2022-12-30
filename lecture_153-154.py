# lambda expressions (anonymous functions)

add2=lambda a,b : a+b
print(add2(2,3))

multiply=lambda a,b : a*b
print(multiply(3,9))

# lambda expression practice

def iseven(a):
    return a%2==0 
print(iseven(5))

iseven2=lambda a : a%2==0
print(iseven2(8))

def last_char(s):
    return s[-1]

lastchar2=lambda s : s[-1]
print(lastchar2('muskan'))

# if else with lambda

def func(s):
    if len(s)>5:
        return True
    return False

func=lambda s : True if len(s)>5 else False
print(func('abcdefg'))