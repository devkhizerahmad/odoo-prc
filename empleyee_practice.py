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


# ============================================================================
# Employee Management System with Debugging Logs
# ============================================================================
# Data Flow:
# 1. Base Employee class -> Inherited by Manager, Developer, Tester
# 2. Organization class -> Manages collection of Employee objects
# 3. Main execution -> Creates instances and adds them to organization
# ============================================================================

import logging

# Configure logging for debugging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class Employee:
    """
    Base Employee class
    Data Flow: Receives name, age, salary -> Stores as instance attributes
    """
    def __init__(self, name, age, salary):
        logger.debug(f"[Employee.__init__] Creating Employee object")
        logger.debug(f"[Employee.__init__] Input params - name: {name}, age: {age}, salary: {salary}")
        
        self.name = name
        self.age = age
        self.salary = salary
        
        logger.info(f"[Employee.__init__] Employee '{name}' created successfully")

    def show_details(self):
        """
        Display employee details
        Data Flow: Reads instance attributes -> Prints formatted output
        """
        logger.debug(f"[Employee.show_details] Displaying details for: {self.name}")
        print(f"Employee Name: {self.name}, Age: {self.age}, Salary: {self.salary}")
        logger.debug(f"[Employee.show_details] Details displayed successfully")


# ============================================================================
# Child classes inheriting from Employee
# Data Flow: Each child class extends Employee with specific attributes
# ============================================================================

class Manager(Employee):
    """
    Manager class - Extends Employee with department information
    
    Data Flow: Inherits base attributes + adds department
    """
    def __init__(self, name, age, salary, department):
        logger.debug(f"[Manager.__init__] Creating Manager object")
        logger.debug(f"[Manager.__init__] Input params - name: {name}, age: {age}, salary: {salary}, department: {department}")
        
        # Call parent class constructor
        super().__init__(name, age, salary)
        self.department = department
        
        logger.info(f"[Manager.__init__] Manager '{name}' from department '{department}' created successfully")
    
    def show_details(self):
        """
        Display manager details including department
        Data Flow: Calls parent show_details() -> Adds department info
        """
        logger.debug(f"[Manager.show_details] Displaying manager details for: {self.name}")
        super().show_details()
        print(f"Department: {self.department}")
        logger.debug(f"[Manager.show_details] Manager details displayed")


class Developer(Employee):
    """
    Developer class - Extends Employee with programming language
    Data Flow: Inherits base attributes + adds programming_language
    """
    def __init__(self, name, age, salary, programming_language):
        logger.debug(f"[Developer.__init__] Creating Developer object")
        logger.debug(f"[Developer.__init__] Input params - name: {name}, age: {age}, salary: {salary}, programming_language: {programming_language}")
        
        # Call parent class constructor
        super().__init__(name, age, salary)
        self.programming_language = programming_language
        
        logger.info(f"[Developer.__init__] Developer '{name}' specializing in '{programming_language}' created successfully")
    
    def show_details(self):
        """
        Display developer details including programming language
        Data Flow: Calls parent show_details() -> Adds programming language info
        """
        logger.debug(f"[Developer.show_details] Displaying developer details for: {self.name}")
        super().show_details()
        print(f"Programming Language: {self.programming_language}")
        logger.debug(f"[Developer.show_details] Developer details displayed")


class Tester(Employee):
    """
    Tester class - Extends Employee with testing tool
    Data Flow: Inherits base attributes + adds testing_tool
    """
    def __init__(self, name, age, salary, testing_tool):
        logger.debug(f"[Tester.__init__] Creating Tester object")
        logger.debug(f"[Tester.__init__] Input params - name: {name}, age: {age}, salary: {salary}, testing_tool: {testing_tool}")
        
        # Call parent class constructor
        super().__init__(name, age, salary)
        self.testing_tool = testing_tool
        
        logger.info(f"[Tester.__init__] Tester '{name}' using tool '{testing_tool}' created successfully")
    
    def show_details(self):
        """
        Display tester details including testing tool
        Data Flow: Calls parent show_details() -> Adds testing tool info
        """
        logger.debug(f"[Tester.show_details] Displaying tester details for: {self.name}")
        super().show_details()
        print(f"Testing Tool: {self.testing_tool}")
        logger.debug(f"[Tester.show_details] Tester details displayed")


class Organization:
    """
    Organization class - Manages collection of employees
    Data Flow: Stores organization name -> Maintains list of Employee objects
    """
    def __init__(self, name):
        logger.debug(f"[Organization.__init__] Creating Organization object")
        logger.debug(f"[Organization.__init__] Input param - name: {name}")
        
        self.name = name
        self.employees = []  # Initialize empty employee list
        
        logger.info(f"[Organization.__init__] Organization '{name}' created with empty employee list")
    
    def add_employee(self, employee: Employee):
        """
        Add employee to organization
        Data Flow: Receives Employee object -> Appends to employees list
        """
        logger.debug(f"[Organization.add_employee] Adding employee to organization")
        logger.debug(f"[Organization.add_employee] Employee details - Name: {employee.name}, Type: {type(employee).__name__}")
        
        self.employees.append(employee)
        
        logger.info(f"[Organization.add_employee] Employee '{employee.name}' added successfully. Total employees: {len(self.employees)}")
    
    def show_all_employees(self):
        """
        Display all employees in organization
        Data Flow: Iterates through employees list -> Calls show_details() for each
        """
        logger.debug(f"[Organization.show_all_employees] Starting to display all employees")
        logger.debug(f"[Organization.show_all_employees] Total employees to display: {len(self.employees)}")
        
        print(f"\nOrganization: {self.name}")
        print("Employee Details:\n" + "-" * 30)
        
        for idx, employee in enumerate(self.employees, 1):
            logger.debug(f"[Organization.show_all_employees] Displaying employee {idx}/{len(self.employees)}")
            employee.show_details()
            print("-" * 30)
        
        logger.info(f"[Organization.show_all_employees] All employee details displayed successfully")


# ============================================================================
# Main Execution Block
# Data Flow:
# 1. Create Organization instance
# 2. Create Employee objects (various types)
# 3. Add employees to organization
# 4. Display all employee information
# ============================================================================

if __name__ == "__main__":
    logger.info("=" * 50)
    logger.info("[MAIN] Starting Employee Management System")
    logger.info("=" * 50)
    
    # Step 1: Create organization
    logger.info("[MAIN] Step 1: Creating organization")
    org = Organization("TechCorp")
    
    # Step 2: Create employee objects
    logger.info("[MAIN] Step 2: Creating employee objects")
    
    logger.debug("[MAIN] Creating Tester instance")
    test1 = Tester("Mike", 25, 50000, "Selenium")
    
    logger.debug("[MAIN] Creating Employee instance")  
    emp1 = Employee("John", 30, 50000)
    
    logger.debug("[MAIN] Creating Manager instance")
    mgr1 = Manager("Alice", 35, 80000, "IT")
    
    logger.debug("[MAIN] Creating Developer instance developer")
    dev1 = Developer("Bob", 28, 60000, "Python")
    
    logger.info("[MAIN] All employee objects created successfully")
    
    # Step 3: Add employees to organization
    logger.info("[MAIN] Step 3: Adding employees to organization")
    org.add_employee(test1)
    org.add_employee(emp1)
    org.add_employee(mgr1)
    org.add_employee(dev1)
    
    logger.info("[MAIN] All employees added to organization")
    
    # Step 4: Display all employee details
    logger.info("[MAIN] Step 4: Displaying all employee details")
    logger.info("\nOrganization Details:\n" + "-" * 30 + "\n")
    logger.info(f"\nOrganization: {org.name}\n" + "-" * 30 + "\n")
    logger.info(f"\nEmployees:\n" + "-" * 30 + "\n")
    org.add_employee(emp1)

    org.show_all_employees()
    
    logger.info("=" * 50)
    logger.info("[MAIN] Employee Management System execution completed")
    logger.info("=" * 50)

# bank status updated
class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show_status(self):
        print(f"Bank Name: {self.name}, Balance: {self.balance}")
    if __name__ == "__main__":
        bank = Bank("MyBank", 100000)
        bank.show_status()
    for i in range(5):
        if i % 2 == 0:
            bank.balance += 10000  # Deposit
        else:
            if bank.balance < 5000:
                print(f"Transaction {i+1}: Insufficient funds for withdrawal. Current balance: {bank.balance}")
                continue
            bank.balance -= 5000   # Withdrawal
    case 1: Deposit
        print(f"Transaction {i+1}: Deposited 10000. Balance is {bank.balance}")
    case 2: Withdrawal
        for i in range(5):
            if i % 2 == 0:
                bank.balance += 10000  # Deposit
                print(f"Transaction {i+1}: Deposited 10000. Balance is {bank.balance}")
            else:
                if bank.balance < 5000:
                    print(f"Transaction {i+1}: Insufficient funds for withdrawal. Current balance: {bank.balance}")
                    continue
                bank.balance -= 5000   # Withdrawal
                print(f"Transaction {i+1}: Withdrew 5000. Balance is {bank.balance}")

    case 3: Insufficient funds

        print(f"Transaction {i+1}: Balance is {bank.balance}")
        print(f"Transaction {i+1}: Insufficient funds for withdrawal. Current balance: {bank.balance}")
    case 4: Final status
    print(f"Final Bank Status: {bank.name}, Balance: {bank.balance}")
    for i in range(5):
        if i % 2 == 0:
            bank.balance += 10000  # Deposit
            print(f"Transaction {i+1}: Deposited 10000. Balance is {bank.balance}")
        else:
            if bank.balance < 5000:
                print(f"Transaction {i+1}: Insufficient funds for withdrawal. Current balance: {bank.balance}")
                continue
            bank.balance -= 5000   # Withdrawal
            print(f"Transaction {i+1}: Withdrew 5000. Balance is {bank.balance}")
