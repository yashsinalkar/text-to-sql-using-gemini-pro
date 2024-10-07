import sqlite3
##Connect to  sqlite
connection=sqlite3.connect("student.db")
#Create a cursor object to insert record,create table
cursor=connection.cursor()
## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)
##Insert more records
cursor.execute('''Insert into STUDENT values('Yash','Artificial Intelligence','B',90)''')
cursor.execute('''Insert into STUDENT values('Somesh','Machine Learning','B',100)''')
cursor.execute('''Insert into STUDENT values('Rahul','Computer Design','B',70)''')
cursor.execute('''Insert into STUDENT values('Shiv','Data Science','B',80)''')
cursor.execute('''Insert into STUDENT values('Soham','Biotechnology','B',90)''')

##Display all the records
print('The insrted records are:')
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)
##Close the connection
connection.commit()
connection.close()
