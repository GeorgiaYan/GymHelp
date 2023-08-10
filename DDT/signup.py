from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

def login_page():
    landing_window.destroy()

def validate_password():
    password = passwordEntry.get()
    if len(password) < 8:
        messagebox.showerror("Invalid Password", 
                            "Password must have at least 8 characters.")
    else:
        
        print("Signup successful!")
        

root = Tk()
root.title("SignUp")
root.geometry("925x500+300+200")

img = PhotoImage(file="welcome_image.png")
Label(root, image=img, bg="white").place(x=50, y=70)

frame = Frame(root, width=400, height=360, bg="gray")
frame.place(x=500, y=100)

heading = Label(frame, text="Create an Account", bg="light blue")
heading.grid(row=0, column=0, padx=10, pady=10)

emailLabel = Label(frame, text="Email Address", bg="light blue")
emailLabel.grid(row=1, column=0, sticky="w", padx=25)

emailEntry = Entry(frame, width=25)
emailEntry.grid(row=2, column=0, sticky="w", padx=25)

usernameLabel = Label(frame, text="Username", bg="light blue")
usernameLabel.grid(row=3, column=0, sticky="w", padx=25)

usernameEntry = Entry(frame, width=25)
usernameEntry.grid(row=4, column=0, sticky="w", padx=25)

passwordLabel = Label(frame, text="Password", bg="light blue")
passwordLabel.grid(row=5, column=0, sticky="w", padx=25)

passwordEntry = Entry(frame, width=25, show="*")
passwordEntry.grid(row=6, column=0, sticky="w", padx=25)

confirmLabel = Label(frame, text="Confirm Password", bg="light blue")
confirmLabel.grid(row=7, column=0, sticky="w", padx=25)

confirmEntry = Entry(frame, width=25, show="*")
confirmEntry.grid(row=8, column=0, sticky="w", padx=25)

termsandconditions = Checkbutton(frame, text=
                                "Agree to Terms and Conditions", 
                                bg="light blue")
termsandconditions.grid(row=9, column=0, padx=15)

signupButton = Button(frame, text="Sign Up", bg="light blue", 
                    command=validate_password)
signupButton.grid(row=10, column=0, padx=25)

alreadyaccount = Label(frame, text="Already Have an Account?",
                    bg="light blue")
alreadyaccount.grid(row=11, column=0, sticky="w", padx=25, pady=10)

loginButton = Button(frame, text="Log In", bg="light blue", 
                    command=login_page)
loginButton.grid(row=11, column=1)

root.mainloop()
