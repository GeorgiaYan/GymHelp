import tkinter as tk
from tkinter import messagebox

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
    "Hip Thrusts"
    "Bench Press",
    "Tricep Dips",
    "Push Ups",
    "Bicep Curl",
    "Hammer Curls",
    "Incline Dumbbell Press",
    "Other"
]

calorie_burn_per_minute = {
    "Push-ups": 7,
    "Squats": 5,
    "Plank": 3,
    "Jumping Jacks": 8,
    "Mountain Climbers": 10,
    "Burpees": 12,
    "Other": 0
}

workout_progress = {}
calorie_tracker = {}

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

    calorie_entry_val = calorie_entry.get()
    try:
        calorie_entry_val = int(calorie_entry_val)
    except ValueError:
        messagebox.showerror("Invalid Input", 
                            "Calories burned must be an integer.")
        return

        
    calorie_burn_per_set = calorie_burn_per_minute
    [selected_workout] * int(reps)
    calorie_burn_per_minute_total = calorie_burn_per_set * int(sets)
    calorie_tracker[selected_workout] = calorie_burn_per_minute_total

    messagebox.showinfo("Workout Added",
                    f"Added {selected_workout} to your workout progress!")

def show_progress():
    progress_message = "Workout Progress:\n\n"
    if not workout_progress:
        progress_message += "No workouts recorded yet!"
    else:
        for workout, data in workout_progress.items():
            reps = data["Reps"]
            sets = data["Sets"]
            progress_message += f"{workout}:{sets} set(s), {reps} rep(s)\n"

    progress_message += "\nCalorie Tracker:\n\n"
    if not calorie_tracker:
        progress_message += "No calorie data recorded yet!"
    else:
        for workout, calorie in calorie_tracker.items():
            progress_message += f"{workout}: {calorie} calories\n"
    
    messagebox.showinfo("Workout Progress", progress_message)

root = tk.Tk()
root.title("Workout Tracker")

workout_label = tk.Label(root, text="Select a Workout:", 
                        font=("Helvetica", 16))
workout_label.pack(pady=20)

workout_listbox = tk.Listbox(root, font=("Helvetica", 14), 
                            selectmode=tk.SINGLE, width=30)
workout_listbox.pack()

for workout in workouts:
    workout_listbox.insert(tk.END, workout)

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

add_button = tk.Button(root, text="Add Workout", 
                    command=add_workout, font=("Helvetica", 14))
add_button.pack(pady=10)

show_progress_button = tk.Button(root, text="Show Progress",
                                command=show_progress, font=("Helvetica", 14))
show_progress_button.pack(pady=10)

root.mainloop()




