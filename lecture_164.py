# advance min and max

def func(item):
    return len(item)

names=['muskan', 'jyoti', 'akansha']
print(min(names, key=func))

students={
    'muskan' : {'score':90, 'age':17},
    'jyoti' : {'score':80, 'age':18}
    
}

print(max(students, key=lambda item:item.get('score'))['name'])