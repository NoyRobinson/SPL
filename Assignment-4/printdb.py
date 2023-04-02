from persistence import *

def main():
    #TODO: implement
    print_all_tables()
    print_employees_report()
    print_activity_report()
    
def print_all_tables():
    #Activities
    print("Activities")
    all_activities = repo._conn.cursor().execute("SELECT * FROM activities ORDER BY date ASC").fetchall()
    for activitie in all_activities:
        print(activitie)
        
    #Branches
    print("Branches")
    all_branches = repo._conn.cursor().execute("SELECT * FROM branches ORDER BY id ASC").fetchall()
    for branche in all_branches:
        print(branche)
        
    #Employees
    print("Employees")
    all_employees = repo._conn.cursor().execute("SELECT * FROM employees ORDER BY id ASC").fetchall()
    for employee in all_employees:
        print(employee)
        
    #Products
    print("Products")
    all_products = repo._conn.cursor().execute("SELECT * FROM products ORDER BY id ASC").fetchall()
    for product in all_products:
        print(product)
        
    #Suppliers
    print("Suppliers")
    all_suppliers = repo._conn.cursor().execute("SELECT * FROM suppliers ORDER BY id ASC").fetchall()
    for supplier in all_suppliers:
        print(supplier)
            
def print_employees_report():
    print()
    print("Employees report")    
    all_employees = repo._conn.cursor().execute("""SELECT name, salary, branches.location, COALESCE(SUM(abs(activities.quantity) * products.price), 0) 
                                                FROM employees
                                                JOIN branches ON employees.branche = branches.id
                                                LEFT JOIN activities ON employees.id = activities.activator_id
                                                LEFT JOIN products ON products.id = activities.product_id
                                                GROUP BY employees.id
                                                ORDER BY name ASC""").fetchall()
    for employee in all_employees:
        print(" ".join(map(str, employee)))
        
def print_activity_report():
    print()
    print("Activities report")
    all_activities = repo._conn.cursor().execute("""SELECT date, products.description, activities.quantity, COALESCE(employees.name, NULL), COALESCE(suppliers.name, NULL)
                                                 FROM activities 
                                                 JOIN products ON activities.product_id = products.id 
                                                 LEFT JOIN employees ON activities.activator_id = employees.id
                                                 LEFT JOIN suppliers ON activities.activator_id = suppliers.id
                                                 ORDER BY activities.date ASC""").fetchall()
    for activitie in all_activities:
        print(activitie)
    
    
        
if __name__ == '__main__':
    main()
        
