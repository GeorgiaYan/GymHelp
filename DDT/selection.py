import tkinter as tk
from tkinter import messagebox

workouts = [
    "Upper Body: Shoulders, Biceps, Triceps, Arms",
    "Lower Body: Legs, Glutes, Hamstrings, Thighs"
]

def select_workout():
    selected_workout = workout_listbox.get(tk.ACTIVE)
    messagebox.showinfo("Workout Selected", 
    f"You Selected: {selected_workout}")

root = tk.Tk()
root.title("Workout Selection")

workout_label = tk.Label(root, text="Select a Workout:",
font=("Helvetica", 16))
workout_label.pack(pady=20)

workout_listbox = tk.Listbox(root, font=("Helvetica", 14),
selectmode=tk.SINGLE, width=30)
workout_listbox.pack()

for workout in workouts:
    workout_listbox.insert(tk.END, workout)

select_button = tk.Button(root, text="Select Workout",
command=select_workout, font=("Helvetica", 14))
select_button.pack(pady=10)

root.mainloop()

