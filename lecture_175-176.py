import time

t1=time.time()
x = 5
if x==5:
    print('x is equal to five')
print('this is line 2')

t2=time.time()
t2=time.time()
print(t2-t1)

# @calculate_time
# def func():
#     print('this is function')
    
# func()
# this function took 3 sec to run

from functools import wraps

def calculate_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f'Executing .... {function.__name__}')
        t1=time.time()
        returned_vaslue=function(*args, **kwargs)
        t2=time.time()
        total_time=t2-t1
        print(f'this function took {total_time} seconds')
        return returned_vaslue
    return wrapper

@calculate_time
def square_finder(n):
    return [i**2 for i in range(1,n+1)]

square_finder(1000)