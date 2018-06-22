
# coding: utf-8

# In[14]:

#Stanley Scott Henry (schenry) 81390908

# these should be the only imports you need
import sys
import sqlite3

conn = sqlite3.connect('Northwind_small.sqlite')
c = conn.cursor()
user_input = sys.argv

#  python3 part2.py customers
if len(user_input) > 1 and user_input[1] == 'customers':
    statement = 'SELECT ID, ContactName FROM Customer'
    customers = c.execute(statement)
    
    print("Id 	 Customer Name")
    for customer in customers:
        (ID, CustomerName) = customer;
        print ("%s 	 %s"%(ID, CustomerName))

#  python3 part2.py employees  
elif len(user_input) > 1 and user_input[1] == 'employees':
    statement = 'SELECT ID, FIRSTNAME, LASTNAME FROM Employee'
    employees = c.execute(statement)

    print('ID	 Employee Name')
    for employee in employees:
        (ID, FirstName, LastName) = employee;
        print ("%s 	 %s %s"% (ID, FirstName, LastName))

#  python3 part2.py orders cust=<customer id>
elif len(user_input) > 2 and 'cust=' in user_input[2]:
    cust_id = '"'+  user_input[2][5:] + '"'
    statement = "SELECT OrderDate FROM [Order] WHERE CustomerId = %s" %(cust_id)
    orders = c.execute(statement)

    print ("Order Dates")
    for order in orders:
        (OrderDate) = order;
        print ("%s"%(OrderDate))

#  python3 part2.py orders emp=<employee last name>
elif len(user_input) > 2 and 'emp=' in user_input[2]:
    last_name = '"'+ user_input[2][4:] + '"'
    statement = "SELECT OrderDate from 'Order' WHERE EmployeeID = (SELECT Id from Employee WHERE LastName = %s)" %(last_name)
    orders = c.execute(statement)

    print ("Order Dates")
    for order in orders:
        (OrderDate) = order;
        print ("%s"%(OrderDate)) 
    
conn.close()

