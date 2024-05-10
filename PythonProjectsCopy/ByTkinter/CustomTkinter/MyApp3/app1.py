import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import os

def makeFile():
    url=instructionEntry.get()
    DIR = os.getcwd()
    os.system(f"cd Output && mkdir {url}")
    os.system(f"wafw00f {url} > {DIR}/Output/{url}/{url}.Waf.txt")
    os.system(f"sublist3r -d {url} -o {DIR}/Output/{url}/{url}.txt")
    os.system(f"cat {url}.txt | httprobe > {DIR}/Output/{url}/{url}1.txt")
    os.system(f"ffuf -w /usr/share/wordlists/dirb/common.txt -u http://{url}/FUZZ -mc all -o {DIR}/Output/{url}/{url}Ffuf.txt")

appPage = ctk.CTk()
appPage.title("MyApp")
appPage.geometry("1000x800")

appFrame = ctk.CTkFrame(appPage,
                                width=900,
                                height=700)
appFrame.pack(expand=True)

instruction = "Welcome User. Please input the website name in the entry below."
textVar = tk.StringVar()
instructionLabel = ctk.CTkLabel(appFrame,
                                width=880,
                                height=200,
                                textvariable = textVar,
                                font=("Helvatica",20)
                                )
instructionLabel.grid(row=0,column=0,sticky="n")

instructionEntry = ctk.CTkEntry(appFrame,
                           width=500,
                           height=50,
                           font=("Helvatica",20),
                           )
instructionEntry.grid(row=1,column=0)

okButton = ctk.CTkButton(appFrame,
                         text="OK",
                         font=("Helvatica",20),
                         width=50,
                         height=20,
                         command=makeFile,
                         )
okButton.grid(row=2,column=0)

index = 0
placeholder = ""

def typeText():
    global index
    global placeholder
    try:
        placeholder += instruction[index]
        textVar.set(placeholder)
        index += 1
        appPage.after(150,typeText)
    except IndexError:
        return

typeText()
appPage.mainloop()
