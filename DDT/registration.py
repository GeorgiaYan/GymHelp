from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from openpyxl import Workbook
from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox
import pathlib

background="#06283D"
framebg="3EDEDED"
framefg="#6283D"

root=Tk()
root.title("Personal Details")
root.geometry("1250x700+210+100")
root.config(bg=background)

file=pathlib.Path("Student_data.xlsx")
if file.exists(): bool
else:
    file=Workbook()
    sheet=file.active
    sheet["A1"]="Name"
    sheet["B1"]="Gender"
    sheet["C1"]="Height"
    sheet["D1"]="Weight"
    
    file.save("Student_data.xlsx")

Label(root,text="Email: tester@gmail.com",width=10,
    height=3,bg=("black"),anchor="e").pack(side=TOP,fill=X)
Label(root,text="ACCOUNT",width=10,height=2,
    bg=("light blue"),fg="black",anchor="e").pack(side=TOP,fill=X)

Search=StringVar()
Entry(root,textvariable=Search,width=15,bd=2).place(x=960,y=58)
img=PhotoImage(file= "search_key.png")
Srch=Button(root,text="Search",compound=RIGHT,
            image=img,width=60,height=50,bg="white")
Srch.place(x=90,y=70)

root.mainloop()