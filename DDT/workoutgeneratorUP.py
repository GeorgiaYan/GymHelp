import tkinter as tk
from tkinter import messagebox

workouts = [
    "Bench Press",
    "Tricep Dips",
    "Push Ups",
    "Bicep Curl",
    "Hammer Curls",
    "Incline Dumbbell Press"
    ]

def show_workout():
    workout = workouts.pop(0)
    workouts.append(workout)
    workout_label.config(text=workout)
    sets_label.config(text="Sets: " + str(sets_entry.get()))
    reps_label.config(text="Reps: " + str(reps_entry.get()))

def save_workout():
    workout_name = workout_label["text"]
    sets = sets_entry.get()
    reps = reps_entry.get()

    messagebox.showinfo("Workout Saved", 
                        f"Workout saved:\n{workout_name}\nSets: {sets}\nReps: {reps}")

    good_job_frame = tk.Frame(root)
    good_job_frame.pack(pady=20)
    good_job_label = tk.Label(good_job_frame, text="Good Job!", 
                            font=("Helvetica", 16), fg="green")
    good_job_label.pack()

root = tk.Tk()
root.title("Workout Generator for UpperBody")

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

workout_label = tk.Label(root, text=
                        "Click the button to get an UpperBody Workout!", 
                        font=("Helvetica", 16))
workout_label.pack(pady=20)

generate_button = tk.Button(root, text="Generate Workout", command=show_workout, 
                        font=("Helvetica", 14))
generate_button.pack(pady=10)

save_button = tk.Button(root, text="Save Workout", command=save_workout, 
                    font=("Helvetica", 14))
save_button.pack(pady=10)

root.mainloop()



