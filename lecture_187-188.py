class laptop:
    def __init__(self, brand, model_name, price):
        self.brand=brand
        self.name=model_name
        self.price=price
        self.laptop_name=brand+' '+model_name
        
laptop1=laptop('hp', 'ay114tx', 63000)
print(laptop1.laptop_name)