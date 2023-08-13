import tkinter as tk
from tkinter import messagebox

# List of available workouts
workouts = [
    "Push-ups",
    "Squats",
    "Plank",
    "Jumping Jacks",
    "Mountain Climbers",
    "Burpees", 
    "Leg Press",
    "Squats",
    "Kick Backs",
    "Calf Raises",
    "Deadlifts",
    "RDL",
    "Hip Thrusts",
    "Bench Press",
    "Tricep Dips",
    "Push Ups",
    "Bicep Curl",
    "Hammer Curls",
    "Incline Dumbbell Press",
    "Other"
]

# Calories burned per minute for different workouts
calorie_burn_per_minute = {
    "Push-ups": 7,
    "Squats": 5,
    "Plank": 3,
    "Jumping Jacks": 8,
    "Mountain Climbers": 10,
    "Burpees": 12,
    "Other": 0
}

# Data dictionaries for workout progress and calorie tracking
workout_progress = {}
calorie_tracker = {}

# Function to add a workout to progress and calorie tracker
def add_workout():
    selected_workout = workout_listbox.get(tk.ACTIVE)
    reps = reps_entry.get()
    sets = sets_entry.get()

    try:
        reps = int(reps)
        sets = int(sets)
    except ValueError:
        messagebox.showerror("Invalid Input", 
                            "Reps and sets must be integers.")
        return

    if selected_workout == "Other":
        custom_workout = custom_entry.get()
        if not custom_workout:
            messagebox.showwarning("Missing Input", 
                                "Please enter a custom workout.")
            return
        selected_workout = custom_workout

    if selected_workout not in workout_progress:
        workout_progress[selected_workout] = {"Reps": reps, "Sets": sets}
    else:
        workout_progress[selected_workout]["Reps"] = reps
        workout_progress[selected_workout]["Sets"] = sets

    # Calculate calories burned per set and update calorie tracker
    calorie_burn_per_set = calorie_burn_per_minute[selected_workout]
    calorie_burn_per_minute_total = calorie_burn_per_set * sets
    calorie_tracker[selected_workout] = calorie_burn_per_minute_total

    messagebox.showinfo("Workout Added",
                    f"Added {selected_workout} to your workout progress!")

# Function to display workout progress and calorie tracking
def show_progress():
    progress_message = "Workout Progress:\n\n"
    if not workout_progress:
        progress_message += "No workouts recorded yet!"
    else:
        for workout, data in workout_progress.items():
            reps = data["Reps"]
            sets = data["Sets"]
            progress_message += f"{workout}: {sets} set(s), {reps} rep(s)\n"

    progress_message += "\nCalorie Tracker:\n\n"
    if not calorie_tracker:
        progress_message += "No calorie data recorded yet!"
    else:
        for workout, calorie in calorie_tracker.items():
            progress_message += f"{workout}: {calorie} calories\n"
    
    messagebox.showinfo("Workout Progress", progress_message)

# Create the main application window
root = tk.Tk()
root.title("Workout Tracker")

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

# Create labels and entry fields for reps, sets, custom workout, and calories
reps_label = tk.Label(root, text="Reps:", font=("Helvetica", 14))
reps_label.pack()

reps_entry = tk.Entry(root, font=("Helvetica", 14))
reps_entry.pack()

sets_label = tk.Label(root, text="Sets:", font=("Helvetica", 14))
sets_label.pack()

sets_entry = tk.Entry(root, font=("Helvetica", 14))
sets_entry.pack()

custom_label = tk.Label(root, text="Custom Workout:", 
                    font=("Helvetica", 14))
custom_label.pack()

custom_entry = tk.Entry(root, font=("Helvetica", 14))
custom_entry.pack()

calorie_label = tk.Label(root, text="Calories Burned:", 
                        font=("Helvetica", 14))
calorie_label.pack()

calorie_entry = tk.Entry(root, font=("Helvetica", 14))
calorie_entry.pack()

# Create buttons to add a workout and show progress
add_button = tk.Button(root, text="Add Workout", 
                    command=add_workout, font=("Helvetica", 14))
add_button.pack(pady=10)

show_progress_button = tk.Button(root, text="Show Progress",
                                command=show_progress, font=("Helvetica", 14))
show_progress_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()





