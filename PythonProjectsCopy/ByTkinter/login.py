#!/bin/python3

import tkinter as tk
from tkinter import ttk
def regiExit():
    regiFrame.destroy()

def regiScreen():
    global regiFrame
    regiFrame = tk.Toplevel()
    regiFrame.title("Registration")
    regiFrame.geometry(middleScreen())
    regiFrame.resizable(False,False)
    
    regiLabelFrame = ttk.Labelframe(regiFrame,text="Registration")
    regiLabelFrame.pack(expand="yes")
    
    regiInfoFrame = ttk.Frame(regiLabelFrame)
    regiInfoFrame.grid(row=0,column=0,padx=10,pady=20)

    regiNameFrame = ttk.Frame(regiInfoFrame)
    regiNameFrame.grid(row=0,column=0,pady=10)
    regiNameLabel = ttk.Label(regiNameFrame,text="Name: ")
    regiNameLabel.grid(row=0,column=0,padx=16)
    regiNameEntry = ttk.Entry(regiNameFrame,width=50)
    regiNameEntry.grid(row=0,column=1)
    
    regiUsernameFrame = ttk.Frame(regiInfoFrame)
    regiUsernameFrame.grid(row=1,column=0,pady=10)
    regiUsernameLabel = ttk.Label(regiUsernameFrame,text="Username: ")
    regiUsernameLabel.grid(row=0,column=0)
    regiUsernameEntry = ttk.Entry(regiUsernameFrame,width=50)
    regiUsernameEntry.grid(row=0,column=1)

    regiPasswordFrame = ttk.Frame(regiInfoFrame)
    regiPasswordFrame.grid(row=2,column=0,pady=10)
    regiPasswordLabel = ttk.Label(regiPasswordFrame,text="Password: ")
    regiPasswordLabel.grid(row=0,column=0,padx=2)
    regiPasswordEntry = ttk.Entry(regiPasswordFrame,width=50,show="*")
    regiPasswordEntry.grid(row=0,column=1)

    regiConfirmFrame = ttk.Frame(regiInfoFrame)
    regiConfirmFrame.grid(row=3,column=0,pady=10)
    regiConfirmLabel = ttk.Label(regiConfirmFrame,text="Confirm: ")
    regiConfirmLabel.grid(row=0,column=0,padx=8)
    regiConfirmEntry = ttk.Entry(regiConfirmFrame,width=50,show="*")
    regiConfirmEntry.grid(row=0,column=1)

    regiEmailFrame = ttk.Frame(regiInfoFrame)
    regiEmailFrame.grid(row=4,column=0,pady=10)
    regiEmailLabel = ttk.Label(regiEmailFrame,text="Email: ")
    regiEmailLabel.grid(row=0,column=0,padx=16)
    regiEmailEntry = ttk.Entry(regiEmailFrame,width=50)
    regiEmailEntry.grid(row=0,column=1)
    
    regiButtonFrame = ttk.Frame(regiLabelFrame)
    regiButtonFrame.grid(row=1,column=0,pady=10)

    regiRegiButton = ttk.Button(regiButtonFrame,text="Registration")
    regiRegiButton.grid(row=0,column=1,padx=30)
    regiExitButton = ttk.Button(regiButtonFrame,text="Exit",command=regiExit)
    regiExitButton.grid(row=0,column=0,padx=70)

def appScreen():
    main.destroy()
    
    app = tk.Tk()
    app.title("Unsatisfied World")
    
    app.geometry(middleScreen())

    mainFrame = ttk.Frame(app)
    mainFrame.pack(expand = "yes")
    
    loginLabelFrame = ttk.Labelframe(mainFrame,text="Login")
    loginLabelFrame.grid(row=0,column=0)
    
    loginInfoFrame = ttk.Frame(loginLabelFrame)
    loginInfoFrame.grid(row=0,column=0,padx=10,pady=20)

    loginUsernameFrame = ttk.Frame(loginInfoFrame)
    loginUsernameFrame.grid(row=0,column=0,pady=10)
    loginUsernameLabel = ttk.Label(loginUsernameFrame,text="Username: ")
    loginUsernameLabel.grid(row=0,column=0)
    loginUsernameEntry = ttk.Entry(loginUsernameFrame,width=50)
    loginUsernameEntry.grid(row=0,column=1)

    loginPasswordFrame = ttk.Frame(loginInfoFrame)
    loginPasswordFrame.grid(row=1,column=0,pady=10)
    loginPasswordLabel = ttk.Label(loginPasswordFrame,text="Password: ")
    loginPasswordLabel.grid(row=1,column=0,padx=2)
    loginUsernameFrame = ttk.Frame(loginInfoFrame)
    loginUsernameFrame.grid(row=0,column=0)
    loginPasswordEntry = ttk.Entry(loginPasswordFrame,width=50,show="*")
    loginPasswordEntry.grid(row=1,column=1)

    loginButtonFrame = ttk.Frame(loginLabelFrame)
    loginButtonFrame.grid(row=1,column=0,pady=10)

    loginRegiButton = ttk.Button(loginButtonFrame,text="Registration",command=regiScreen)
    loginRegiButton.grid(row=0,column=0,padx=70)
    loginLoginButton = ttk.Button(loginButtonFrame,text="Login")
    loginLoginButton.grid(row=0,column=1,padx=30)

    app.mainloop()

def loginScreen():
    mainFrame = ttk.Frame(main)
    mainFrame.pack(expand = "yes")
    
    loginLabelFrame = ttk.Labelframe(mainFrame,text="Login")
    loginLabelFrame.grid(row=0,column=0)
    
    loginInfoFrame = ttk.Frame(loginLabelFrame)
    loginInfoFrame.grid(row=0,column=0,padx=10,pady=20)

    loginUsernameFrame = ttk.Frame(loginInfoFrame)
    loginUsernameFrame.grid(row=0,column=0,pady=10)
    loginUsernameLabel = ttk.Label(loginUsernameFrame,text="Username: ")
    loginUsernameLabel.grid(row=0,column=0)
    loginUsernameEntry = ttk.Entry(loginUsernameFrame,width=50)
    loginUsernameEntry.grid(row=0,column=1)

    loginPasswordFrame = ttk.Frame(loginInfoFrame)
    loginPasswordFrame.grid(row=1,column=0,pady=10)
    loginPasswordLabel = ttk.Label(loginPasswordFrame,text="Password: ")
    loginPasswordLabel.grid(row=1,column=0,padx=2)
    loginUsernameFrame = ttk.Frame(loginInfoFrame)
    loginUsernameFrame.grid(row=0,column=0)
    loginPasswordEntry = ttk.Entry(loginPasswordFrame,width=50,show="*")
    loginPasswordEntry.grid(row=1,column=1)

    loginButtonFrame = ttk.Frame(loginLabelFrame)
    loginButtonFrame.grid(row=1,column=0,pady=10)

    loginRegiButton = ttk.Button(loginButtonFrame,text="Registration",command=regiScreen)
    loginRegiButton.grid(row=0,column=0,padx=70)
    loginLoginButton = ttk.Button(loginButtonFrame,text="Login",command=appScreen)
    loginLoginButton.grid(row=0,column=1,padx=30)

def middleScreen():
    global value
    #screenWidth = main.winfo_screenwidth()
    #screenHeight = main.winfo_screenheight()
    appWidth = 900
    appHeight = 700
    xPosition = (screenWidth - appWidth)//2
    yPosition = (screenHeight - appHeight)//2
    value = f"{appWidth}x{appHeight}+{xPosition}+{yPosition}"
    return value


def mainWindow():
    global main
    global screenWidth
    global screenHeight
    main = tk.Tk()

    screenWidth = main.winfo_screenwidth()
    screenHeight = main.winfo_screenheight()
    
    main.title("Unsatisfied_Soul")
    main.geometry(middleScreen())
    main.resizable(False,False)
    loginScreen()
    main.mainloop()


mainWindow()
