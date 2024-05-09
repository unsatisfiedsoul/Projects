import customtkinter as ctk
import tkinter as tk
import center
import bcrypt
import mysql.connector as my
from tkinter import messagebox as mb

#Fungtion Portion
def login():
    regiWindow.destroy()
    import loginPage
def regi():
    name = nameEntry.get()
    username = usernameEntry.get()
    password = passwordEntry.get()
    confirmpassword = confirmpasswordEntry.get()
    email = emailEntry.get()
    checkbox = termCheckbox.get()

    if (name == "" and username == "" and password == "" and confirmpassword == "" and email == ""):
        mb.showwarning("warning","All field required")
    elif (password!=confirmpassword):
        mb.showwarning("Warning","Password do not match")
    elif (checkbox==False):
        mb.showwarning("Warning","Accept terms and conditions")
    else:
        mydb = my.connect(
                host = "127.0.0.1",
                user = "rony",
                password = "766900",
                database = "pythonDB")
        encode = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashedPassword = bcrypt.hashpw(encode,salt)

        values = (name,username,hashedPassword,email)
        query = "insert into userInfo(name,username,password,email) values (%s,%s,%s,%s)"

        mycursor = mydb.cursor()
        mycursor.execute(query,values)
        mydb.commit()
        mydb.close()

        regiWindow.destroy()

        import loginPage
        print(mydb)

#Design Portion
regiWindow = ctk.CTk()
regiWindow.title("Welcome to Registration")
center.center_screen(regiWindow,600,500)

#Main frame to hold everything in the center
regiFrame = ctk.CTkFrame(regiWindow,
                          width = 400,
                          height = 500,
                          fg_color = "#240a34",
                          border_width = 2,
                          border_color = "green")
regiFrame.pack(expand=True)

#Name Portion
nameLabel = ctk.CTkLabel(regiFrame,
                             text="Name",
                             width = 20,
                             height = 20,
                             text_color = "#ffedd8",
                             font = ("Helvatica",16,"bold"))
nameLabel.grid(row=0,column=0,sticky="w",padx=(30,0),pady=(20,10))

nameEntry = ctk.CTkEntry(regiFrame,
                             width = 300,
                             height = 30,
                             text_color = "#ffedd8",
                             font = ("Helvatica",16))
nameEntry.grid(row=0,column=1,padx=(0,10),pady=(20,10))


#Username Portion
usernameLabel = ctk.CTkLabel(regiFrame,
                             text="Username",
                             width = 20,
                             height = 20,
                             text_color = "#ffedd8",
                             font = ("Helvatica",16,"bold"))
usernameLabel.grid(row=1,column=0,sticky="w",padx=(30,0),pady=(20,10))

usernameEntry = ctk.CTkEntry(regiFrame,
                             width = 300,
                             height = 30,
                             text_color = "#ffedd8",
                             font = ("Helvatica",16))
usernameEntry.grid(row=1,column=1,padx=(0,10),pady=(20,10))


#Password Portion
passwordLabel = ctk.CTkLabel(regiFrame,
                             text="Password",
                             width = 20,
                             height = 20,
                             text_color = "#ffedd8",
                             font = ("Helvatica",16,"bold"))
passwordLabel.grid(row=2,column=0,sticky="w",padx=(30,0),pady=5)

passwordEntry = ctk.CTkEntry(regiFrame,
                             width = 300,
                             height = 30,
                             text_color = "#ffedd8",
                             font = ("Helvatica",16),
                             show = "*")
passwordEntry.grid(row=2,column=1,sticky="w",padx=(0,10),pady=10)


#Confirm Password Portion
confirmpasswordLabel = ctk.CTkLabel(regiFrame,
                             text="Confirm Password",
                             width = 20,
                             height = 20,
                             text_color = "#ffedd8",
                             font = ("Helvatica",16,"bold"))
confirmpasswordLabel.grid(row=3,column=0,sticky="w",padx=(30,0),pady=5)

confirmpasswordEntry = ctk.CTkEntry(regiFrame,
                             width = 300,
                             height = 30,
                             text_color = "#ffedd8",
                             font = ("Helvatica",16),
                             show = "*")
confirmpasswordEntry.grid(row=3,column=1,sticky="w",padx=(0,10),pady=10)


#Email Portion
emailLabel = ctk.CTkLabel(regiFrame,
                             text="Email",
                             width = 20,
                             height = 20,
                             text_color = "#ffedd8",
                             font = ("Helvatica",16,"bold"))
emailLabel.grid(row=4,column=0,sticky="w",padx=(30,0),pady=5)

emailEntry = ctk.CTkEntry(regiFrame,
                             width = 300,
                             height = 30,
                             text_color = "#ffedd8",
                             font = ("Helvatica",16))
emailEntry.grid(row=4,column=1,sticky="w",padx=(0,10),pady=10)


#Terms and Condition Portion
termCheckbox = ctk.CTkCheckBox(regiFrame,
                               text="By clicking this checkbox you are excepting our terms and conditions ",
                               checkbox_width = 18,
                               checkbox_height = 18,
                               cursor = "hand2")
termCheckbox.grid(row=5,columnspan=2,sticky="w",padx=(30,10),pady=10)



#Button Portion
regiButton = ctk.CTkButton(regiFrame,
                            text="Register",
                            width = 300,
                            height= 30,
                            text_color = "#ffedd8",
                            font = ("Helvatica",14,"bold"),
                            cursor = "hand2",
                            command = regi)
regiButton.grid(row=6,columnspan=2,padx=10,pady=(10,20))

#Login Label portion
loginLabel = ctk.CTkLabel(regiFrame,
                         text = "Already have an account??",
                         )
loginLabel.grid(row=7,column=0,padx=20,pady=(0,10))
loginButton = ctk.CTkButton(regiFrame,
                           text = "Login Here",
                           font = ("Helvatica",10,"underline"),
                           fg_color = "#240a34",
                           hover = False,
                           cursor = "hand2",
                           command = login,
                           width = 5)
loginButton.grid(row=7,column=1,sticky="e",padx=5)

regiWindow.mainloop()
