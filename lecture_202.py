class Phone:
    def __init__(self, brand, model_name, price):
        self.brand=brand
        self.model_name=model_name
        self.price=price
        
    def make_a_call(self, phone_number):
        print(f"calling {phone_number} ...")
        
    def full_name(self):
        return f"{self.brand} {self.model_name}"

class Smartphone(Phone):
    def __init__(self, brand, model_name, price, ram):
        # self.brand=brand
        # self.model_name=model_name
        # self.price=price
        Phone.__init__(self, brand, model_name, price)
        self.ram=ram
        
    def make_a_call(self, phone_number):
        print(f"calling {phone_number} ...")
        
    def full_name(self):
        return f"{self.brand} {self.model_name}"

phone=Phone('nokia', '1100', 1000)
smartphone=Smartphone('oneplus', '5',30000, '6 GB')
print(phone.full_name())
print(smartphone.full_name() + f"and price is {smartphone._price}")

class Flagshipphone(Smartphone):
    def __init__(self, brand, model_name, price, ram, front_camera):
        super().__init__(brand, model_name, price, ram)
        self.front_camera=front_camera
        
        
smartphone=smartphone('oneplus', '5', 30000, '6 GB')
oneplus=Flagshipphone('oneplus', '5', 30000, '6 GB', '20 MP')
print(smartphone.full_name())
print(help(Smartphone))
        
        