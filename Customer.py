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
                    PhoneNo=i['PhoneNo']
                )

    def __repr__(self) -> str:
        return f"Customer('{self.Customer_id}', '{self.Full_Name}', '{self.Enterprise_Name}', '{self.Address}', '{self.PhoneNo}')"
