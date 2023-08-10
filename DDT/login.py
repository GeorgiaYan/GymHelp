from tkinter import *
from tkinter import messagebox

# Function to handle the login process
def login():
      # Get the username and password 
      # Entered in the Entry widgets
   username=entry1.get()
   password=entry2.get()
   
   # Checks if both username and password are blank
   if (username=="" and password== ""):
      # Displays an information message box 
      # If both fields are blank
      messagebox.showinfo("","Blank Not Allowed")
   
   # Checks if the entered username and password
   # Match the predefined values
   elif (username=="tester" and password=="admin"):
      # Display an information message box for successful login
      messagebox.showinfo("","login success")
      
   else:
   # Displays an information message box
   # This for incorrect username or password
      messagebox.showinfo("","incorrect username or password")

# The main Tkinter window
root=Tk()
root.title("Login") 
root.geometry("925x500+300+200")

# Creates Entry widgets to get the username and password
global entry1
global entry2

img = PhotoImage(file= "gym_logo.png")
Label(root,image=img,bg="white").place(x=50,y=50)

Label(root, text="Username").place(x=570,y=70)
Label(root,text="Password").place(x=570,y=140)

entry1=Entry(root,bd=5)
entry1.place(x=700,y=70)

entry2=Entry(root,bd=5)
entry2.place(x=700,y=140)

frame=Frame(root,width=350,height=350,bg="black")

Button(root,text="Login",command=login,height=3, 
      width=13,bd=6).place(x=650, y=220)
label1=Label(frame,text="Sign Up?",fg="white",bg="black")

newaccountButton=Button(root,text="Create new one")
newaccountButton.place(x=600,y=370)

signupLabel=Label(root,text="Don't have an account?",
                  bg="black")
signupLabel.place(x=600,y=320)

root.mainloop()


