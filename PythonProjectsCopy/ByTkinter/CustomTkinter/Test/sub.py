import subprocess
import tkinter as tk

def run():
    text1 = entry.get()
    result = subprocess.run(text1,
                            capture_output=True,
                            text=True,
                            check=True)
    text.insert(tk.END,result.stdout)
    print(result.stdout)
    print(result.stderr)

root = tk.Tk()
root.title("Test")
root.geometry("1000x800")

label =tk.Label(root,
                text="Write the command please")
label.grid(row=0,column=0)

entry = tk.Entry(root,
                 width=100)
entry.grid(row=0,column=1)

button = tk.Button(root,
                   text="ok",
                   command=run)

button.grid(row=1,column=0)

text = tk.Text(root)
text.grid(row=2,column=0)

root.mainloop()
