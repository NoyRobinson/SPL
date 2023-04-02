from persistence import *

import sys
import os


def add_branche(splittedline : list[str]):
    #TODO: add the branch into the repo
    branche_object = Branche(splittedline[0], splittedline[1], splittedline[2])
    repo.branches.insert(branche_object)


def add_supplier(splittedline : list[str]):
    #TODO: insert the supplier into the repo
    supplier_object = Supplier(splittedline[0], splittedline[1], splittedline[2])
    repo.suppliers.insert(supplier_object)


def add_product(splittedline : list[str]):
    #TODO: insert product
    product_object = Product(splittedline[0], splittedline[1], splittedline[2], splittedline[3])
    repo.products.insert(product_object)


def add_employee(splittedline : list[str]):
    #TODO: insert employee
    employee_object = Employee(splittedline[0], splittedline[1], splittedline[2], splittedline[3])
    repo.employees.insert(employee_object)


adders = {  "B": add_branche,
            "S": add_supplier,
            "P": add_product,
            "E": add_employee}


def main(args : list[str]):
    inputfilename = args[1]
    # delete the database file if it exists
    repo._close()
    # uncomment if needed
    if os.path.isfile("bgumart.db"):
        os.remove("bgumart.db")
    repo.__init__()
    repo.create_tables()
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(",")
            adders.get(splittedline[0])(splittedline[1:])


if __name__ == '__main__':
    main(sys.argv)