import os

try:
    os.system("pip install mysql-connector-python")
except:
    print("mysql-connector-python exists")
import mysql.connector as my

try:
    mydb = my.connect(

        host = "127.0.0.1",
        user = "root",
        password = "766900",
        database = "my_app_db"
    )
    print(mydb)
except:
    os.system("sudo apt install mariadb-client mariadb-server")    
    os.system("sudo mariadbd-safe")
    os.system("sudo mysql_secure_installation")

    #os.system("sudo mariadb -u root -p")

    passwd = input("Again input mariadb root password: ")
    mydb = my.connect(
        host="127.0.0.1",
        user="root",
        password = passwd,

    )
    print(mydb)
    #mycursor = mydb.cursor()
    #query = "create database my_app_db;use my_app_db"
    #mycursor.execute(query)
    #mydb.commit()
    #values = ("root","root")
    #query = "insert into users(username,password) values(%s,%s)"
    #mycursor.execute(query,values)
    #mydb.commit()
try:
    mycursor = mydb.cursor()    
    query = "create database my_app_db;use my_app_db;"
    mycursor.execute(query)
except:
    mycursor = mydb.cursor()
    query = "use my_app_db"
    mycursor.execute(query)

try:
    mycursor = mydb.cursor()
    query = "create table users(id int not null auto_increment,username varchar(50) not null,password varchar(100) not null,primary key(id))"
    mycursor.execute(query)
    values = ("root","root")
    query = "insert into users(username,password) values(%s,%s)"
    mycursor.execute(query,values)
    mydb.commit()
except:
    values = ("root","root")
    query = "insert into users(username,password) values(%s,%s)"
    mycursor.execute(query,values)
    mydb.commit()
