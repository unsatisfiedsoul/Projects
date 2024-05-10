import tkinter as tk
from tkinter import ttk, END
import customtkinter as ctk
import mysql.connector as my
from tkcalendar import Calendar,DateEntry



def insert():
    id = idInsertEntry.get()
    name = nameInsertEntry.get()
    join = joinInsertDateEntry.get_date()
    section = sectionInsertOption.get()

    mydb = my.connect(
        host = "127.0.0.1",
        user = "root",
        password = "766900",
        database = "my_app_db"
    )
    print(mydb)
    mycursor = mydb.cursor()
    values = (id,name,join,section)
    query = "insert into operator_data(dcs_id,name,join_date,section) values(%s,%s,'%s',%s)"
    try:
        mycursor.execute(query,values)
        mydb.commit()
    except:
        try:

            query = "create table operator_data(id int not null auto_increment,dcs_id varchar(10) not null,name varchar(100) not null,join_date date not null,section varchar(50) not null, primary key(id))"
            mycursor.execute(query)
            mydb.commit()
        except:
            print("Table already existed")
        query = "insert into operator_data(dcs_id,name,join_date,section) values(%s,%s,%s,%s)"
        mycursor.execute(query,values)
        mydb.commit()
    mydb.close()
    idInsertEntry.delete(0,END)
    nameInsertEntry.delete(0,END)
    




root = ctk.CTk()
root.title("My App")
root.geometry("800x600")
rootFrame = ctk.CTkFrame(root)
rootFrame.pack(expand="Yes")

firstFrame = ctk.CTkFrame(rootFrame,width=600,height=600)
firstFrame.grid(row=0,column=0)
operatorDataFrame = ctk.CTkFrame(firstFrame,width=200,height=100)
operatorDataFrame.grid(row=0,column=0,padx=40,pady=20)
idDataLabel = ctk.CTkLabel(operatorDataFrame,text="Operator's ID:")
idDataLabel.grid(row=0,column=0)
idDataEntry = ctk.CTkEntry(operatorDataFrame,width=200)
idDataEntry.grid(row=0,column=1)
enterDataButton = ctk.CTkButton(operatorDataFrame,text="Enter")
enterDataButton.grid(row=1,columnspan=2)

operatorDataScrollableFrame = ctk.CTkScrollableFrame(firstFrame,width=200,height=100)
operatorDataScrollableFrame.grid(row=1,column=0)

secondFrame = ctk.CTkFrame(rootFrame,width=600,height=600)
secondFrame.grid(row=0,column=1)

operatorInsertFrame = ctk.CTkFrame(secondFrame)
operatorInsertFrame.grid(row=0,column=0,padx=40,pady=20)
idInsertLabel = ctk.CTkLabel(operatorInsertFrame,text="ID: ")
idInsertLabel.grid(row=0,column=0)
idInsertEntry = ctk.CTkEntry(operatorInsertFrame,width=200)
idInsertEntry.grid(row=0,column=1)
nameInsertLabel = ctk.CTkLabel(operatorInsertFrame,text="Name: ")
nameInsertLabel.grid(row=1,column=0)
nameInsertEntry = ctk.CTkEntry(operatorInsertFrame,width=200)
nameInsertEntry.grid(row=1,column=1)
joinInsertLabel = ctk.CTkLabel(operatorInsertFrame,text="Join Date: ")
joinInsertLabel.grid(row=2,column=0)
joinInsertDateEntry = DateEntry(operatorInsertFrame,width=20,date_pattern='YYYY-mm-dd', background="darkblue", foreground="white", borderwidth=2)
joinInsertDateEntry.grid(row=2,column=1)
#joinInsertCalendar = Calendar(operatorInsertFrame,width=20)
#joinInsertCalendar.grid(row=3,columnspan=2)
sectionInsertLabel = ctk.CTkLabel(operatorInsertFrame,text="Section: ")
sectionInsertLabel.grid(row=4,column=0)
sectionInsertOption = ctk.CTkOptionMenu(operatorInsertFrame,values=["Hydrated Lime","Power House","Utility","Lime Kiln","Boiler","Crane","Mechanic","Workshop","Store","Pmcc","Feeding"],)
sectionInsertOption.grid(row=4,column=1)
enterInsertButton = ctk.CTkButton(operatorInsertFrame,text="Enter",command=insert)
enterInsertButton.grid(row=5,columnspan=2)

root.mainloop()