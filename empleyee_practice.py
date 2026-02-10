# # 1. Ek class banao jiska naam ho "Mobile"
# class Mobile:
#     # 2. Ek constructor (__init__) banao jo 'brand' aur 'price' le
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
#         print(f"Mobile created with brand {self.brand} and price {self.price}")
    
#     # 3. Ek function banao jo print kare "Ye mobile [brand] ka hai"
#     def show_details(self):
#         print(f"modile brand {self.brand} with the price {self.price} ")

# # 4. Class ka object banao (jaise JS mein new Mobile())
# # Samsung mobile banao price 50000 ka
# my_phone = Mobile("Samsung", 80000)
# my_phone2 = Mobile("Iphone", 100000)
# my_phone3 = Mobile("OnePlus", 60000)
# my_phone4 = Mobile("Xiaomi", 30000)
# my_phone5 = Mobile("Realme", 20000)
# updated_phones = [my_phone, my_phone2, my_phone3, my_phone4, my_phone5]
# sorted_phones = sorted([my_phone, my_phone2, my_phone3, my_phone4, my_phone5], key=lambda x: x.price)
# print("Phones sorted by price:", [phone.brand for phone in sorted_phones])
# # 5. Function call karo
# my_phone.show_details()  
# my_phone2.show_details()
# my_phone3.show_details()
# sorted_phones[0].show_details()  # Sabse sasta phone dikhaye
# sorted_phones[-1].show_details()  # Sabse mehnga phone dikhaye
# sorted_phones[2].show_details()  # Beech ka phone dikhaye
# my_phone3.show_details()
# updated_phones[2].show_details()
# updated_phones[3].show_details()

# my_phone4.show_details()


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def show_details(self):
        print(f"Employee Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

# Child classes inheriting from Employee
class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department
    
    def show_details(self):
        super().show_details()
        print(f"Department: {self.department}")


class Developer(Employee):
    def __init__(self, name, age, salary, programming_language):
        super().__init__(name, age, salary)
        self.programming_language = programming_language
    
    def show_details(self):
        super().show_details()
        print(f"Programming Language: {self.programming_language}")


class Tester(Employee):
    def __init__(self, name, age, salary, testing_tool):
        super().__init__(name, age, salary)
        self.testing_tool = testing_tool
    
    def show_details(self):
        super().show_details()
        print(f"Testing Tool: {self.testing_tool}")


class Organization:
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def add_employee(self, employee: Employee):
        self.employees.append(employee)
    
    def show_all_employees(self):
        print(f"\nOrganization: {self.name}")
        print("Employee Details:\n" + "-" * 30)
        for employee in self.employees:
            employee.show_details()
            print("-" * 30)


# Using OOP to manage employees
if __name__ == "__main__":
    org = Organization("TechCorp")

    # Creating objects
    test1 = Tester("Mike", 25, 50000, "Selenium")
    emp1 = Employee("John", 30, 50000)
    mgr1 = Manager("Alice", 35, 80000, "IT")
    dev1 = Developer("Bob", 28, 60000, "Python")

    # Adding to organization
    org.add_employee(test1)
    org.add_employee(emp1)
    org.add_employee(mgr1)
    org.add_employee(dev1)

    # Display all employee details
    org.show_all_employees()
