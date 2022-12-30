# kwargs 
# **kwargs

# kwargs as a parameter

def func(name, **kwargs):
    # print(kwargs)
    # print(type(kwargs))
    for k,v in kwargs.items():
        print(f"{k} : {v}")
    
func('mann', first_name='Nishant', last_name='Raj')