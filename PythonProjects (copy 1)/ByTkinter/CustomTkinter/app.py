import customtkinter as ctk

def add_todo():
    todo = entry.get()
    label = ctk.CTkLabel(scrollableFrame, text=todo,font = ctk.CTkFont(size=40,weight="bold"))
    label.pack()
    entry.delete(0,ctk.END)

def enter_todo(event):
    todo = entry.get()
    label = ctk.CTkLabel(scrollableFrame, text=todo,font = ctk.CTkFont(size=40,weight="bold"))
    label.pack()
    entry.delete(0,ctk.END)

def clear_todo():
    pass

root = ctk.CTk()
root.geometry("1200x900")
root.title("Todo App")
titleLabel = ctk.CTkLabel(root,text="Daily Task",font=ctk.CTkFont(size=60,weight="bold"))
titleLabel.pack(padx=10,pady=(40,20))

scrollableFrame = ctk.CTkScrollableFrame(root,width=800,height=500)
scrollableFrame.pack()

entry = ctk.CTkEntry(scrollableFrame,width=900,height=50, placeholder_text ="Add to do",font = ctk.CTkFont(size=40,weight="bold"))
entry.pack()

addButton = ctk.CTkButton(root,text="Add",width=900,command=add_todo,font=ctk.CTkFont(size=40,weight="bold"))
addButton.pack(pady=20)

clearButton = ctk.CTkButton(root,text="Clear",width=900,command=clear_todo,font=ctk.CTkFont(size=40,weight="bold"))
clearButton.pack(pady=20)


root.bind("<Return>",enter_todo)

root.mainloop()
