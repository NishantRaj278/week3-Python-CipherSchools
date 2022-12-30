# iterator vs iterables

numbers=[1,2,3,4] # tuples, string ---- iterables
squares=map(lambda a:a**2, numbers) #iterator


for i in numbers:
    print(i)