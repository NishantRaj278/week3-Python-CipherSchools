# make flexible functions
# *operator
# *args

def total(a,b):
    return a+b
print(total(3,4))

def all_total(*args):
    # print(args)
    # print(type(args))
    total=0
    for i in args:
        total+=i
    return total
print(all_total(1,2,3,4,65,77))