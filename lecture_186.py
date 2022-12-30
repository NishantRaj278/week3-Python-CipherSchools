# what is class, ho to create it
# what is init method
# what are attributes, instance variables
# how to create our object

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        
p1=Person('Nishant', 'Raj', 17)
print(p1.first_name)