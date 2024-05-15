import customtkinter as ctk
import center
import tkinter as tk
from tkinter import messagebox as mb
import mysql.connector as my

#Function Portion
def regi():
    loginWindow.destroy()
    import regiPage
def login():
    username = usernameEntry.get()
    password = passwordEntry.get()

    if (username == "" or password == ""):
        mb.showinfo("Warning","All field required")
    else:
        mydb = my.connect(
                host = "127.0.0.1",
                user = "rony",
                password = "766900",
                database = "pythonDB")

        #data = (username,password)
        data = username
        query = "select username, password from userInfo where username = '%s'"
        mycursor = mydb.cursor()
        mycursor.execute(query,data)
        row = mycursor.fetchone()
        for row in mycursor:
            print(row)

#Design Portion
loginWindow = ctk.CTk()
loginWindow.title("Welcome to Login")
center.center_screen(loginWindow,500,300)

#Main frame to hold everything in the center
loginFrame = ctk.CTkFrame(loginWindow,
                          width = 300,
                          height = 300,
                          fg_color = "#240a34",
                          border_width = 2,
                          border_color = "green")
loginFrame.pack(expand=True)

#Username Portion
usernameLabel = ctk.CTkLabel(loginFrame,
                             text="Username",
                             width = 20,
                             height = 20,
                             text_color = "#ffedd8",
                             font = ("Helvatica",16,"bold"))
usernameLabel.grid(row=0,column=0,sticky="w",padx=(30,0),pady=(20,10))

usernameEntry = ctk.CTkEntry(loginFrame,
                             width = 300,
                             height = 30,
                             text_color = "#ffedd8",
                             font = ("Helvatica",16))
usernameEntry.grid(row=0,column=1,padx=(0,10),pady=(20,10))


#Password Portion
passwordLabel = ctk.CTkLabel(loginFrame,
                             text="Password",
                             width = 20,
                             height = 20,
                             text_color = "#ffedd8",
                             font = ("Helvatica",16,"bold"))
passwordLabel.grid(row=1,column=0,sticky="w",padx=(30,0),pady=5)

passwordEntry = ctk.CTkEntry(loginFrame,
                             width = 300,
                             height = 30,
                             text_color = "#ffedd8",
                             font = ("Helvatica",16),
                             show = "*")
passwordEntry.grid(row=1,column=1,sticky="w",padx=(0,10),pady=10)


#Terms and Condition Portion
termCheckbox = ctk.CTkCheckBox(loginFrame,
                               text="Remember me",
                               checkbox_width = 18,
                               checkbox_height = 18,
                               cursor = "hand2")
termCheckbox.grid(row=2,columnspan=2,sticky="w",padx=(30,10),pady=10)



#Button Portion
loginButton = ctk.CTkButton(loginFrame,
                            text="Login",
                            width = 300,
                            height= 30,
                            text_color = "#ffedd8",
                            font = ("Helvatica",14,"bold"),
                            cursor = "hand2",
                            command = login)
loginButton.grid(row=3,columnspan=2,padx=10,pady=(10,20))

#Regi Label portion
regiLabel = ctk.CTkLabel(loginFrame,
                         text = "Don't have an account??",
                         )
regiLabel.grid(row=4,column=0,padx=20,pady=(0,10))
regiButton = ctk.CTkButton(loginFrame,
                           text = "Register Here",
                           font = ("Helvatica",10,"underline"),
                           fg_color = "#240a34",
                           hover = False,
                           cursor = "hand2",
                           command = regi,
                           width = 5)
regiButton.grid(row=4,column=1,sticky="e",padx=5)

loginWindow.mainloop()
