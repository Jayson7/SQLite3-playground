import sqlite3
connection = sqlite3.connect("customersinfo.db")

# create sql in memory  connection = sqlite3.connect(":memory:")

c = connection.cursor()

# create a table
# c.execute(""" CREATE TABLE customersinfo(
#     first_name  text,
#     last_name text,
#     phone_number integer,
#     email text
    
# )""")
# ********************************************
# insert into db
# c.execute(""" INSERT INTO customersinfo VALUES(
#     'jay',
#     'jayson',
#     0809999999999,
#     'jayson@gmail.com'
# )""")
# *******************************************

#  insert  multiple data into db
# other_info = [
#     ('ken', 'wyne',555945666, 'kw@gmail.com'),
#     ('king', 'wyne', 20945666, 'kgw@gmail.com'),
#     ('mary', 'wyne',  33945666, 'mw@gmail.com'),
#     ('jessica', 'wyne', 905945666, 'jw@gmail.com'),
    
# ]
# c.executemany(" INSERT INTO customersinfo VALUES(?, ?, ?, ?)", other_info)
# print("Database updated successfully")




# get all data **********************
c.execute("SELECT rowid, * FROM    customersinfo")
# print(c.fetchall())

# fomat results using fetchone ********************
# print(c.fetchone())

# fomat results using fetchmany with amount requuired ********************

# print(c.fetchmany(2))
# or
# print(c.fetchmany(4)) 

# using indexing with fetchone *************** 
# print(c.fetchone()[0]) 
# print(c.fetchone()[0])
# print(c.fetchone()[1])
# print(c.fetchone()[2]) 
 
#   some looping with fetchall ***********************

databases = c.fetchall()

# for i in databases:
#     mane =i
#     print(f"{mane} is an item in the database ")
#     print("***" * 20)

# ********************************************* 
# print("NAME" + '\t LASTNAME ' + "\t PHONE NUMBER ")  
# print("-----------------" + '\t-------------------')

# for i in databases:
#     num = str(i[2])
#     print(i[0] + "     " + i[1]  + "  \t\t" + num  )



# Primary keys 

print("NAME" + '\t LASTNAME ' + "\t PHONE NUMBER ")  
print("-----------------" + '\t-------------------')

for i in databases:
    num = str(i[2])
    t =  "{}. {}  -  {} \t {}"
    result = t.format(i[0], i[1], i[2], i[3] )
    print(result)




connection.commit() #push to database
connection.close() # by default after running your programs you connection will close but its important to close connections by convention
# types of datatypes
# NULL doesnt exist
# INTEGER a whole number
# REAL decimal number 
# BLOB  a file or image in any case