import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#Function to validate height input
def validate_height():
    try:
        height = float(height_entry.get())
        if height < 50 or height > 250:
            messagebox.showerror("Invalid Height", 
                                "Height must be between 50 and 250 cm.")
        else:
            print("Height:", height)
    except ValueError:
        messagebox.showerror("Invalid Input", 
                            "Please enter a valid numeric height.")

#Function to validate age input 
def validate_age():
    try:
        age = int(age_entry.get())
        if age < 12 or age > 100:
            messagebox.showerror("Invalid Age", 
                                "Age must be between 12 and 80.")
        else:
            print("Age:", age)
    except ValueError:
        messagebox.showerror("Invalid Input", 
                            "Please enter a valid numeric age.")

# Function to submit the user's information
def submit_info():
    name = name_entry.get()
    weight = weight_entry.get()
    gender = gender_var.get()

    print("Name:", name)
    print("Weight:", weight)
    print("Gender:", gender)

root = tk.Tk()
root.title("Personal Information")
root.geometry("400x300")

# Created the main frame
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Labels and Entry widgets for:
# Name, Age, Height, Weight, and Gender
name_label = ttk.Label(frame, text="Name:")
name_label.grid(row=0, column=0, sticky=tk.W)

name_entry = ttk.Entry(frame, width=30)
name_entry.grid(row=0, column=1, sticky=tk.W)

age_label = ttk.Label(frame, text="Age:")
age_label.grid(row=1, column=0, sticky=tk.W)

age_entry = ttk.Entry(frame, width=10)
age_entry.grid(row=1, column=1, sticky=tk.W)

height_label = ttk.Label(frame, text="Height (cm):")
height_label.grid(row=2, column=0, sticky=tk.W)

height_entry = ttk.Entry(frame, width=10)
height_entry.grid(row=2, column=1, sticky=tk.W)

weight_label = ttk.Label(frame, text="Weight:")
weight_label.grid(row=3, column=0, sticky=tk.W)

weight_entry = ttk.Entry(frame, width=10)
weight_entry.grid(row=3, column=1, sticky=tk.W)

gender_label = ttk.Label(frame, text="Gender:")
gender_label.grid(row=4, column=0, sticky=tk.W)

gender_var = tk.StringVar()
gender_var.set("Male")
gender_radio_male = ttk.Radiobutton(frame, text="Male", 
                                variable=gender_var, value="Male")
gender_radio_male.grid(row=4, column=1, sticky=tk.W)

gender_radio_female = ttk.Radiobutton(frame, text="Female", 
                                    variable=gender_var, value="Female")
gender_radio_female.grid(row=5, column=1, sticky=tk.W)

gender_radio_other = ttk.Radiobutton(frame, text="Other", 
                                    variable=gender_var, value="Other")
gender_radio_other.grid(row=6, column=1, sticky=tk.W)

submit_button = ttk.Button(frame, text="Submit", command=submit_info)
submit_button.grid(row=7, column=0, columnspan=2, pady=10)

# Add validation for height 
# And age using the `validate command` attribute
validate_height_cmd = root.register(validate_height)
height_entry.config(validate="key", 
                    validatecommand=(validate_height_cmd, "%P"))

validate_age_cmd = root.register(validate_age)
age_entry.config(validate="key",
                validatecommand=(validate_age_cmd, "%P"))

# Start the main event loop
root.mainloop()
