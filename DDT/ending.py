import tkinter as tk
from tkinter import ttk

# Function to handle finishing the workout
def finish_workout():
        # Hide the 'ending_frame' from the window
    ending_frame.grid_forget()  
        # Display the 'sign_out_frame' at row=0, column=0 with padding
    sign_out_frame.grid(row=0, column=0, padx=50, pady=50)

# Function to handle signing out and closing the application
def sign_out():
        # Destroy the main Tkinter window, 
        # closing the application
    root.destroy() 

# Created the main Tkinter window
root = tk.Tk()
root.title("Workout App")
root.geometry("400x200")

# Created the 'ending_frame' 
# Placed it with padding and sticky to all sides
ending_frame = ttk.Frame(root, padding="20")
ending_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Created a label in the 'ending_frame' to display a congratulatory message
finish_label = ttk.Label(ending_frame, text=
                        "Congratulations! Workout Finished!", 
                        font=("Helvetica", 16))
finish_label.pack()

# Created a button in the 'ending_frame' 
# This too trigger the 'finish_workout()' 
# function when clicked
finish_button = ttk.Button(ending_frame, text="Sign Out", 
                        command=finish_workout)
finish_button.pack(pady=20)

# Created the 'sign_out_frame' and place it in row=0, column=0, with padding
sign_out_frame = ttk.Frame(root, padding="20")

# Created a label in the 'sign_out_frame' 
# This too display a farewell message
sign_out_label = ttk.Label(sign_out_frame, text="Thank you for using the Workout App!", 
                        font=("Helvetica", 16))
sign_out_label.pack()

# Create a button in the 'sign_out_frame' 
# This to trigger the 'sign_out()' function when clicked
sign_out_button = ttk.Button(sign_out_frame, text="Sign Out", 
                            command=sign_out)
sign_out_button.pack(pady=20)

# Call the 'finish_workout()' function to show 
# the 'ending_frame' at the start
finish_workout()

root.mainloop()
