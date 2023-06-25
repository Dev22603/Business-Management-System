# stock management
# Credit and Debit entries management
# Debt and Credit
# Customer Data
# Supplier Data

import csv
from Customer import *
from Supplier import *



Customer.instantiate_from_csv()
print(Customer.all)
Supplier.instantiate_from_csv()
print(Supplier.all)