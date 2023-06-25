import csv


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
