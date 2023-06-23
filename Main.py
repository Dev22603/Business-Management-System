# stock management
# Credit and Debit entries management
# Debt and Credit
# Customer Data
# Supplier Data
import csv


class Customer:
    all = []

    def __init__(self, Customer_id, Full_Name, Enterprise_Name, Address, PhoneNo):
        self.Customer_id = Customer_id
        self.Full_Name = Full_Name
        self.Enterprise_Name = Enterprise_Name
        self.Address = Address
        self.PhoneNo = PhoneNo

        # self.Customer_id = input("Enter Customer ID: ")
        # self.Full_Name = input("Enter Full Name of Customer: ")
        # self.Enterprise_Name = input("Enter name Enterprise of Customer: ")
        # self.Address = input("Enter Address of Customer: ")
        # self.PhoneNo = input("Enter Phone Number of Customer: ")
        Customer.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open('customer.csv', 'r') as f:
            reader = csv.DictReader(f)
            customers_dict = list(reader)
            for i in customers_dict:
                Customer(
                    Customer_id=i['Customer_id'],
                    Full_Name=i['Full_Name'],
                    Enterprise_Name=i['Enterprise_Name'],
                    Address=i['Address'],
                    PhoneNo=i['PhoneNo'],
                )

    def __repr__(self) -> str:
        return f"Customer('{self.Customer_id}', '{self.Full_Name}', '{self.Enterprise_Name}', '{self.Address}', '{self.PhoneNo}')"


class Supplier:
    all = []
    def __init__(self, Supplier_id, Full_Name, Enterprise_Name, Address, PhoneNo):
        self.Supplier_id = Supplier_id
        self.Full_Name = Full_Name
        self.Enterprise_Name = Enterprise_Name
        self.Address = Address
        self.PhoneNo = PhoneNo
        Supplier.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open('supplier.csv', 'r') as f:
            reader = csv.DictReader(f)
            supplier_dict = list(reader)
            for i in supplier_dict:
                Supplier(
                    Supplier_id=i['Supplier_id'],
                    Full_Name=i['Full_Name'],
                    Enterprise_Name=i['Enterprise_Name'],
                    Address=i['Address'],
                    PhoneNo=i['PhoneNo'],
                    # Supplier_id=i.get('Supplier_id'),
                    # Full_Name=i.get('Full_Name'),
                    # Enterprise_Name=i.get('Enterprise_Name'),
                    # Address=i.get('Address'),
                    # PhoneNo=i.get('PhoneNo'),
                )
    def __repr__(self) -> str:
        return f"Supplier('{self.Supplier_id}', '{self.Full_Name}', '{self.Enterprise_Name}', '{self.Address}', '{self.PhoneNo}')"

    # def get_details(self):
    #     self.Customer_id = input("Enter Supplier ID: ")
    #     self.Full_Name = input("Enter Full Name of Supplier: ")
    #     self.Enterprise_Name = input("Enter name of Enterprise of Supplier: ")
    #     self.Address = input("Enter Address of Supplier: ")
    #     self.PhoneNo = input("Enter Phone Number of Supplier: ")
# a = Customer(1, "abc", "def", "ghi", "1234567890")
# b = Customer(2, "abc", "def", "ghi", "1234567890")
Customer.instantiate_from_csv()
print(Customer.all)
Supplier.instantiate_from_csv()
print(Supplier.all)
