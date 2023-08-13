import tkinter as tk
from tkinter import messagebox

# List of available workouts
workouts = [
    "Upper Body: Shoulders, Biceps, Triceps, Arms",
    "Lower Body: Legs, Glutes, Hamstrings, Thighs"
]

# Function to handle workout selection
def select_workout():
    selected_workout = workout_listbox.get(tk.ACTIVE)  # Get the selected workout
    messagebox.showinfo("Workout Selected", 
                        f"You Selected: {selected_workout}")  # Display selected workout

# Create the main application window
root = tk.Tk()
root.title("Workout Selection")

# Create label to prompt user to select a workout
workout_label = tk.Label(root, text="Select a Workout:",
                        font=("Helvetica", 16))
workout_label.pack(pady=20)

# Create a listbox to display available workouts
workout_listbox = tk.Listbox(root, font=("Helvetica", 14),
                            selectmode=tk.SINGLE, width=30)
workout_listbox.pack()

# Insert each workout from the list into the listbox
for workout in workouts:
    workout_listbox.insert(tk.END, workout)

# Create a button to select a workout
select_button = tk.Button(root, text="Select Workout",
                        command=select_workout, font=("Helvetica", 14))
select_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()


