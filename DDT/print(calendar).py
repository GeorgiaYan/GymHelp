from tkinter import *


root=Tk()
root.resizable(0,0)
root.config(bg="black")

monthLabel=Label(root,text="Month",font=("arial",15),bg="black")
monthLabel.grid()

yearLabel=Label(root,text="Year",font=("arial",15),bg="black")
yearLabel.grid(row=0,column=1)

monthspinBox=Spinbox(root,from_=1, to=12)
monthspinBox.grid(row=1,column=0,padx=10)

yearspinBox=Spinbox(root,from_=2010, to=2500)
yearspinBox.grid(row=1,column=1,padx=10)

goButton=Button(root,text="Go")
goButton.grid(row=1,column=2,padx=10)

textfield=Text(root,width=30,height=10,fg="white")
textfield.grid(row=2,column=0,columnspan=3)

root.mainloop()