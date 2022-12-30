# class methods

class Person:
    count_instance=0
    def __init__(self, first_name, last_name, age):
        Person.count_instance+=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        
    # @classmethod
    # def count_instances(cls):
    #     return f"You have created {cls.count_instance} instances of {cls.__name__}"
    
    @classmethod
    def  from_string(cls,string):
         first,last,age=string.split(',')
         return cls(first,last,age)
        
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_above_18(self):
        return self.age>18

p1=Person('Nishant', 'Raj', 18)
p2=Person('Tushar', 'Singh', 18)
p3=Person('Sunny', 'Saini', 19)
p3=Person.from_string('Nishant,Raj,18')
print(p3.full_name())