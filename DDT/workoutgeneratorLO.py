import tkinter as tk
from tkinter import messagebox

# List of different workouts
workouts = [
    "Leg Press",
    "Squats",
    "Kick Backs",
    "Calf Raises",
    "Deadlifts",
    "RDL",
    "Hip Thrusts"
]

# Function to display the next workout in the list
def show_workout():
    workout = workouts.pop(0)  # Get and remove the first workout from the list
    workouts.append(workout)    # Add the workout back to the end of the list
    workout_label.config(text=workout)  # Update the displayed workout label
    sets_label.config(text="Sets: " + str(sets_entry.get()))  # Display sets from entry
    reps_label.config(text="Reps: " + str(reps_entry.get()))  # Display reps from entry

# Function to save the current workout
def save_workout():
    workout_name = workout_label["text"]
    sets = sets_entry.get()
    reps = reps_entry.get()

    # Display a message box with the saved workout details
    messagebox.showinfo("Workout Saved", 
                        f"Workout saved:\n{workout_name}\nSets: {sets}\nReps: {reps}")

    # Display a "Good Job!" message
    good_job_frame = tk.Frame(root)
    good_job_frame.pack(pady=20)
    good_job_label = tk.Label(good_job_frame, text="Splendid!", 
                            font=("Helvetica", 16), fg="green")
    good_job_label.pack()

# Create the main application window
root = tk.Tk()
root.title("Workout Generator for Lower Body")

# Create frames to hold sets and reps information
sets_frame = tk.Frame(root)
sets_frame.pack()

sets_label = tk.Label(sets_frame, text="Sets: ", 
                    font=("Helvetica", 14))
sets_label.pack(side=tk.LEFT)

sets_entry = tk.Entry(sets_frame, font=("Helvetica", 14), width=5)
sets_entry.pack(side=tk.LEFT)

reps_frame = tk.Frame(root)
reps_frame.pack()

reps_label = tk.Label(reps_frame, text="Reps: ",
                    font=("Helvetica", 14))
reps_label.pack(side=tk.LEFT)

reps_entry = tk.Entry(reps_frame, font=("Helvetica", 14), width=5)
reps_entry.pack(side=tk.LEFT)

# Label to display the current workout
workout_label = tk.Label(root, text=
                        "Click the button to get a Lower Body Workout!",
                    font=("Helvetica", 16))
workout_label.pack(pady=20)

# Button to generate the next workout
generate_button = tk.Button(root, text="Generate Workout", 
                            command=show_workout, font=("Helvetica", 14))
generate_button.pack(pady=10)

# Button to save the current workout
save_button = tk.Button(root, text="Save Workout", 
                        command=save_workout, font=("Helvetica", 14))
save_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()




