import sqlite3

conn = sqlite3.connect('user.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Users')
cur.execute("CREATE TABLE Users(fname VARCHAR(200) , lname VARCHAR(128) ,email VARCHAR(128))")

fname = input("Enter FirstName: ")
lname= input("Enter lastName: ")
email= input('Enter the email: ')
cur.execute('''
            INSERT INTO Users(fname,lname,email) VALUES(?,?,?)''',(fname,lname,email))
conn.commit()