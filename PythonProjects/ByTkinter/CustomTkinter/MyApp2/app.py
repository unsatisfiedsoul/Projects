import customtkinter as ctk


root = ctk.CTk()
root.title("My App")
root.geometry("500x400")
rootFrame = ctk.CTkFrame(root)
rootFrame.pack(expand="Yes")

appFrame = ctk.CTkFrame(root,width=600,height=600)
appFrame.pack(expand="Yes")
operatorScrollableFrame = ctk.CTkScrollableFrame(appFrame,width=200,height=100)
operatorScrollableFrame.grid(row=0,column=0)

root.mainloop()