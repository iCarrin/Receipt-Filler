# make an recipte orginizer
import sqlite3

# con = sqlite3.connect(':memory:') this is if you only needed a small thing that deletes once saved to memory
conn = sqlite3.connect('customer.db')

#create a cursor (a "finger" hence the f )
f = conn.cursor()

#create a table
# f.execute("""CREATE TABLE customers(
#           first_name text,
#           last_name text,
#           email text)

# """)




# #adding one line of data to data base
# f.execute("INSERT INTO customers  VALUES ('John', 'Smith', 'tim.co@yourmom.com')")

#building a list of data
many_customers = [
    ('Adam', 'Smith', 'Adam.co@yourmom.com'),
    ('Mike', 'Smith', 'Mike.bro@yourmom.com'),
    ('Jessica', 'Smith', 'Jessica.hoe@yourmom.com'),
]
#adding a whole list to a database
f.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)



# #how to select some item from a list
# f.execute("SELECT * FROM customers")
# # f.fetchone()
# # f.fetchmany(3)
# # f.fetchall()



# #GIVING YOURself a premade data base
# f.execute("SELECT * FROM customers")
# items = f.fetchall()

# # nice header
# print("NAME " + "\t\tEMAIL")
# for item in items:
#     #print nicely formated table
#     print(item[0] + " " + item[1] + "\t " + item[2])


##row ID
# f.execute("SELECT rowid * FROM customers")

# #Where clause and LIKE clause. the % sign is a whild card
# f.execute("SELECT * FROM customers WHERE last_name LIKE 'Sm%' ")
# # logic opperators are = < > and LIKE




# update records by finding them (the AND totally worked, ya boi!)
# f.execute("""UPDATE customers SET first_name = 'Bob'
#           WHERE last_name = 'Smith' AND first_name = 'Mike'
# """)
# ##using rowid to update the customers is mucho better
# f.execute("""UPDATE customers SET first_name = 'Bobert'
#           WHERE rowid = 3

# """)

# #how to delete something.
# f.execute("DELETE from customers WHERE rowid = 2")


# #How to order
# f.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")
# #ACS and DECS are how your organize ascending and descending. asending is defaults

# #and or
# f.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Smi%' AND first_name LIKE 'Jessica'")


# #Limiting how many are shown
# f.execute("SELECT rowid, * FROM customers DESC LIMIT 3")

# #how to drop a table
# f.execute("DROP TABLE customers")



# ?commit our command? # always have to commit before showing off what you've done.
conn.commit()

items = f.execute("SELECT rowid, * FROM customers")
items = f.fetchall()

for item in items:
    print(item)

# quite connects
conn.close()