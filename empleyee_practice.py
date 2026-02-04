# 1. Ek class banao jiska naam ho "Mobile"
class Mobile:
    # 2. Ek constructor (__init__) banao jo 'brand' aur 'price' le
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        print(f"Mobile created with brand {self.brand} and price {self.price}")
    
    # 3. Ek function banao jo print kare "Ye mobile [brand] ka hai"
    def show_details(self):
        print(f"modile brand {self.brand} with the price {self.price} ")

# 4. Class ka object banao (jaise JS mein new Mobile())
# Samsung mobile banao price 50000 ka
my_phone = Mobile("Samsungg", 80000)

# 5. Function call karo
my_phone.show_details()  