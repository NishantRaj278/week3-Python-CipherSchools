# class variable
class Circle:
    pi=3.14
    def __init__(self, radius):
        self.radius=radius
    def calc_circumference(self):
        return 2*Circle.pi*self.radius
c=Circle(4)
c1=Circle(5)
print(c.calc_circumference())

class laptop:
    discount_percent=10
    def __init__(self, brand, model_name, price):
        self.brand=brand
        self.name=model_name
        self.price=price
        self.laptop_name=brand+' '+model_name
        
    def apply_discount(self):
         off_price=(laptop.discount_percent/100)*self.price
         return self.price-off_price 
     
laptop.discount_percent=100
laptop1=laptop('hp', 'ay114tx', 63000)
laptop1.discount_percent=50
# print(laptop1.apply_discount())

print(laptop1.__dict__)
print(laptop1.apply_discount())