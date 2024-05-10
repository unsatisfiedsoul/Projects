import mysql.connector as my
import bcrypt

def mariacrypt(name,username,password,email):

    byte = password.encode("utf-8")
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(byte,salt)
    values = (name,username,hashed_password,email)

    mydb = my.connect(
            host = "127.0.0.1",
            user = "rony",
            password = "766900",
            database = "pythonDB"
            )

    query = "insert into user_info(name,username,password,email) values(%s,%s,%s,%s)"
    mycursor = mydb.cursor()
    mycursor.execute(query,values)
    mydb.commit()
    mydb.close()

    return "Registration Success"
