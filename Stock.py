import csv
class Stock:
    all = []

    def __init__(self, Stock_id, Stock_Name, Price, Quantity_left):
        self.Stock_Id = Stock_id  # id is an integer value
        self.Stock_name = str(Stock_Name).title()   # title makes the
        self.Price = float(Price)    # price a floating point number
        self.Quantity_Left = int(Quantity_left)


        # self.Customer_id = input("Enter Customer ID: ")
        # self.Full_Name = input("Enter Full Name of Customer: ")
        # self.Enterprise_Name = input("Enter name Enterprise of Customer: ")
        # self.Address = input("Enter Address of Customer: ")
        # self.PhoneNo = input("Enter Phone Number of Customer: ")
        Stock.all.append(self)
    @classmethod
    def instantiate_from_csv(cls):
        with open('stock.csv', 'r') as f:
            reader = csv.DictReader(f)
            stock_dict = list(reader)
            for i in stock_dict:
                Stock(
                    Stock_id=i['Customer_id'],
                    Stock_Name=i['Stock_Name'],
                    Price=i['Price'],
                    Quantity_left=i['Quantity_left']
                )

    def __repr__(self) -> str:
        return f"Stock('{self.Stock_Id}', '{self.Stock_name}', '{self.Price}', '{self.Quantity_Left}')"

