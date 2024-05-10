import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import os
import subprocess


def makeFile():
    url=instructionEntry.get()
    DIR = os.getcwd()
    
#    os.system(f"cd Output && mkdir {url}")
#    os.system(f"wafw00f {url} > {DIR}/Output/{url}/{url}.Waf.txt")
#    os.system(f"sublist3r -d {url} -o {DIR}/Output/{url}/{url}.txt")
#    os.system(f"cat {url}.txt | httprobe > {DIR}/Output/{url}/{url}1.txt")
#    os.system(f"ffuf -w /usr/share/wordlists/dirb/common.txt -u http://{url}/FUZZ -mc all -o {DIR}/Output/{url}/{url}Ffuf.txt")


    text12 =f"wafw00f {url} > {DIR}/Output/{url}/{url}.Waf.txt && echo 'Wafw00f finished' && sublist3r -d {url} -o {DIR}/Output/{url}/{url}.txt && echo 'Sublist3r Finished' && cat {url}.txt | httprobe > {DIR}/Output/{url}/{url}1.txt && echo 'Httprobe Finished' && ffuf -w /usr/share/wordlists/dirb/common.txt -u http://{url}/FUZZ -mc all -o {DIR}/Output/{url}/{url}Ffuf.txt && echo 'Ffuf Finished' && katana -u https://{url} -o {DIR}/Output/{url}/{url}.katana.txt && echo 'Katana Finished' && httpx https://{url} -v > {DIR}/Output/{url}/{url}.httpx.txt && echo 'Httpx Finished'"
    os.system(f"cd Output && mkdir {url}")
    result=subprocess.run(text12,
                    shell=True,
                    capture_output=True,
                    text=True,
                    check=False
                    )
    outputTextbox.insert("end",result.stdout)
    #print(result.stdout)
    #print(result.stderr)

appPage = ctk.CTk()
appPage.title("MyApp")
appPage.geometry("1300x1000")

font1 = ("Helvatica",26)

appFrame = ctk.CTkFrame(appPage,
                        width=1100,
                        height=700)
appFrame.pack(expand=True)

instruction = "Welcome User. Please input the website name in the entry below."
textVar = tk.StringVar()
instructionLabel = ctk.CTkLabel(appFrame,
                                width=880,
                                height=200,
                                textvariable = textVar,
                                font=font1,
                                )
instructionLabel.grid(row=0,column=0,sticky="n")

instructionEntry = ctk.CTkEntry(appFrame,
                           width=500,
                           height=50,
                           font=font1,
                           )
instructionEntry.grid(row=1,column=0)

okButton = ctk.CTkButton(appFrame,
                         text="OK",
                         font=font1,
                         width=100,
                         height=20,
                         command=makeFile,
                         )
okButton.grid(row=2,column=0,padx=12,pady=12)

outputTextbox = ctk.CTkTextbox(appFrame,
                               wrap="word",
                               width=900,
                               height=500,
                               font=font1,
                               )
outputTextbox.grid(row=3,column=0)

index = 0
placeholder = ""

def typeText():
    global index
    global placeholder
    try:
        placeholder += instruction[index]
        textVar.set(placeholder)
        index += 1
        appPage.after(30,typeText)
    except IndexError:
        return

typeText()

appPage.mainloop()
