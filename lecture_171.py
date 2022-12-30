# decorators - enhance the functionality of other functions
# @ use for decorators


def decorator_function(any_function):
    def wrapper_function():
        print('this is awesome function')
        any_function()
    return wrapper_function

@decorator_function
def func1():
    print('this is function 1')
    
def func2():
    print('this is function 2')
    
func1()