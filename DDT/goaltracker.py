import tkinter as tk
import random
from tkinter import messagebox
from PIL import ImageTk, Image

# Function to save the user's entered goals 
# Display a message box with the goals
def save_goals():
        # Retrieve user input from the entry widgets
    goal1 = goal1_entry.get()
    goal2 = goal2_entry.get()
    goal3 = goal3_entry.get()

    # Display a message box with the saved goals
    messagebox.showinfo("Goals Saved", 
                        f"Goals saved:\n\n1. {goal1}\n2. {goal2}\n3. {goal3}")

# Read the contents of "text.txt" and print it
f = open("text.txt", "r")
print(f.read())

# Function to display a random quote from the list of quotes
def show_quote():
        # List of quotes
    quotes = [
    "The only way to do great work is to love what you do.",
    "Believe you can and you're halfway there.",
    "The future belongs to those who believe in the beauty of their dreams",
    "In the middle of every difficulty lies opportunity."
    ]
    
    # Choose a random quote from the list
    quote = random.choice(quotes)
        # Update the label with the chosen quote
    quote_label.config(text=quote)

# Created the main Tkinter window
root = tk.Tk()
root.title("Goal Tracker")

# Created a frame for the goals section 
# Place it in the window with padding
goal_frame = tk.Frame(root)
goal_frame.pack(pady=20)

# Created labels and entry widgets for three goals 
# Packed them side by side in the goal frame
goal1_label = tk.Label(goal_frame, text="Goal 1:", font=("Helvetica", 14))
goal1_label.pack(side=tk.LEFT)

goal1_entry = tk.Entry(goal_frame, font=("Helvetica", 14), width=30)
goal1_entry.pack(side=tk.LEFT)

goal2_label = tk.Label(goal_frame, text="Goal 2:", font=("Helvetica", 14))
goal2_label.pack(side=tk.LEFT)

goal2_entry = tk.Entry(goal_frame, font=("Helvetica", 14), width=30)
goal2_entry.pack(side=tk.LEFT)

goal3_label = tk.Label(goal_frame, text="Goal 3:", font=("Helvetica", 14))
goal3_label.pack(side=tk.LEFT)

goal3_entry = tk.Entry(goal_frame, font=("Helvetica", 14), width=30)
goal3_entry.pack(side=tk.LEFT)

# Created a button to save the goals 
# Packed it with padding
save_button = tk.Button(root, text="Save Goals", command=save_goals, 
                        font=("Helvetica", 14))
save_button.pack(pady=10)

# Created a frame for the quote section 
# Then place it in the window with padding
quote_frame = tk.Frame(root)
quote_frame.pack(pady=20)

# Created a label to display the random quote 
# Then pack it in the quote frame
quote_label = tk.Label(quote_frame, text="", font=("Helvetica", 14), 
                    wraplength=400)
quote_label.pack()

# Created a button to show a random quote 
# When clicked and pack it with padding
quote_button = tk.Button(root, text="Show Quote of the Day", 
                        command=show_quote, font=("Helvetica", 14))
quote_button.pack(pady=10)

# Created a frame for the image section 
# Placed it in the window with padding
image_frame = tk.Frame(root)
image_frame.pack(pady=20)

# Path to the image file
image_path = "goal.png"

# Open and resize the image
image = Image.open(image_path)
image = image.resize((200, 200), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

# Created a label to display the image 
# Packed it in the image frame
image_label = tk.Label(image_frame, image=photo)
image_label.pack()

root.mainloop()


