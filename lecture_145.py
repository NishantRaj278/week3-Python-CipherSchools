# args vs arguments

def multiply_nums(*args):
    multiply=1
    print(args)
    for i in args:
        multiply*=i
    return multiply

nums=[2,3,4]
print(multiply_nums(*nums)) # unpack

