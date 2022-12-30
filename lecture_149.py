# function with all type of parameters

# ORDER
# parameters
# *args
# default paramaters
# **kwargs

def func(name,*args, last_name='unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
    
func('Muskan', 1,2,3, a=1, b=2)
    
