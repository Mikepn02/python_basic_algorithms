import sqlite3

conn = sqlite3.connect('user.db')
cur = conn.cursor()


fname = input("Enter FirstName: ")
email= input('Enter the email: ')
row = cur.execute(f'''
            SELECT * FROM Users WHERE email="{email}"''')
data = row.fetchone()
if not data:
    print("email is invalid")
else:
    if fname == data[0] :
        print("login successful")
    else:
        print("invalid email")
conn.close()