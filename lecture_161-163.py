# def average_finder(*args):
#     average=[]
#     for pair in zip(*args):
#         average.append(sum(pair)/len(pair))
#     return average

average_finder=lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]
print(average_finder([1,2,3], [4,5,6], [7,8,9]))

# any and all function

numbers1=[2,4,9,8,10]
numbers2=[1,3,5,7,9]

evens1=[]
for num in numbers1:
    if num%2==0:
        evens1.append(num%2==0)

print(evens1)
print(all([num%2==0 for num in numbers1]))
print(any([num%2==0 for num in numbers1]))

def my_sum(*args):
    if all([(type(arg)==int or type(arg)==float) for arg in args]):
        total=0
        for num in args:
            total+=num
        return total
    else:
        return('wrong input')
print(my_sum(1,2,3,4,5,8.9,'muskan',['muskan']))
        