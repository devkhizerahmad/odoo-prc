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
my_phone = Mobile("Samsung", 80000)
my_phone2 = Mobile("Iphone", 100000)
my_phone3 = Mobile("OnePlus", 60000)
my_phone4 = Mobile("Xiaomi", 30000)
my_phone5 = Mobile("Realme", 20000)
updated_phones = [my_phone, my_phone2, my_phone3, my_phone4, my_phone5]
sorted_phones = sorted([my_phone, my_phone2, my_phone3, my_phone4, my_phone5], key=lambda x: x.price)
print("Phones sorted by price:", [phone.brand for phone in sorted_phones])
# 5. Function call karo
my_phone.show_details()  
my_phone2.show_details()
my_phone3.show_details()
sorted_phones[0].show_details()  # Sabse sasta phone dikhaye
sorted_phones[-1].show_details()  # Sabse mehnga phone dikhaye
sorted_phones[2].show_details()  # Beech ka phone dikhaye
m_phone3.show_details()

my_phone4.show_details()