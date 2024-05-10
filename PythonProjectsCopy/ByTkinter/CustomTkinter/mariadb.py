import mysql.connector as my

mydb = my.connect(
        host = "127.0.0.1",
        user = "rony",
        password = "766900",
        database = "pythonDB"
        )


name = input("name: ")
username = input("username: ")
password = input("password: ")
email = input("email: ")

values = (name,username,password,email)
query = "insert into user_info(name,username,password,email) values (%s,%s,%s,%s)"


mycursor = mydb.cursor()
mycursor.execute(query,values)
mydb.commit()
mydb.close()
