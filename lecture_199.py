# Encapsulation
# Abstraction
# Some special naming convention
# Name Mangling

class Phone:
    def __init__(self, brand, model_name, price):
        self.brand=brand
        self.model_name=model_name
        self.price=price
        
    def make_a_call(self, phone_number):
        print(f"calling {phone_number} ...")
        
    def full_name(self):
        return f"{self.brand} {self.model_name}"
    
    def send_message(self):
        pass

phone1=Phone('nokia', '1100', 1000)
print(phone1.price)
phone1._price=-1000
print(phone1._price)

 
# _name # convention of private name
# __name__ # dunder/magic methods



l=[3,4,1,2]
l.sort()
print(l)
    