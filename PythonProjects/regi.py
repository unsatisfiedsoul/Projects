import mysql.connector as my
import bcrypt


mydb = my.connect(
    host = "localhost",
    user = "rony",
    password = "766900",
    database = "DCS"
)

inputUsername = input("What is your Username: ")
inputPassword = input("What is your Password: ")
ps = inputPassword.encode("utf-8")
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(ps,salt)
query = "insert into users(username,password) values (%s,%s)"
value = (inputUsername,hashed)
cursor = mydb.cursor()
cursor.execute(query,value)
mydb.commit()
cursor.close()
mydb.close()

