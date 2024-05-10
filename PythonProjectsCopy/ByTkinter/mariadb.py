import mysql.connector as mariadb

def mariaDb():
    mydb = mariadb.connect(
            host = "localhost",
            user = "rony",
            password = "766900",
            database = "pythonDB"
            )
    #print(mydb)
    mycursor = mydb.cursor()
    query = "select * from user_info"
    mycursor.execute(query)
    for i in mycursor:
        print(i)

mariaDb()
