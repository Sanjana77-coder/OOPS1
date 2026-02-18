class Mobile:
    def __init__(self, brand, model , price):
        self.brand = brand
        self.model = model
        self.price = price
    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model

m1 = Mobile("Redmi","android",20000)
m2 = Mobile("Redmi", "android", 35000)
m3 = Mobile("Apple" , "iphone", 74000)

print(m1 == m2)
print(m2 == m3)
print(m1 == m3)