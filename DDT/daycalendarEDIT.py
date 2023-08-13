import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class WorkoutTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Workout Tracker")
        self.root.geometry("800x600")

        # Created workout entry form
        self.workout_frame = ttk.Frame(root)
        self.workout_frame.pack()

        self.date_label = ttk.Label(self.workout_frame, text="Date (dd/mm/yyyy):",
                                    font=("Helvetica", 12))
        self.date_label.grid(row=0, column=0, padx=10)

        self.date_entry = ttk.Entry(self.workout_frame, width=15)
        self.date_entry.grid(row=0, column=1, padx=10)

        self.workout_label = ttk.Label(self.workout_frame, text="Workout:", 
                                    font=("Helvetica", 12))
        self.workout_label.grid(row=0, column=2, padx=10)

        self.workout_entry = ttk.Entry(self.workout_frame, width=30)
        self.workout_entry.grid(row=0, column=3, padx=10)

        self.add_button = ttk.Button(self.workout_frame, text="Add Workout", 
                                    command=self.add_workout)
        self.add_button.grid(row=0, column=4, padx=10)

        # Creates a progress display area
        self.progress_text = tk.Text(root, height=10, width=60)
        self.progress_text.pack()

        # This is for Data storage
        self.workouts = {}

    def add_workout(self):
        date = self.date_entry.get()
        workout = self.workout_entry.get()

        if not date or not workout:
            messagebox.showwarning("Missing Information", 
                                "Please enter both date and workout.")
            return

        # Converted input date to dd/mm/yyyy format
        try:
            datetime_object = datetime.strptime(date, "%d/%m/%Y")
            formatted_date = datetime_object.strftime("%d/%m/%Y")
        except ValueError:
            messagebox.showwarning("Invalid Date Format", 
                                "Please enter a valid date in dd/mm/yyyy format.")
            return

        if formatted_date in self.workouts:
            self.workouts[formatted_date].append(workout)
        else:
            self.workouts[formatted_date] = [workout]

        self.date_entry.delete(0, tk.END)
        self.workout_entry.delete(0, tk.END)

    def show_progress(self):
        self.progress_text.delete(1.0, tk.END)
        self.progress_text.insert(tk.END, "Workout Progress:\n\n")
        for date, workouts in self.workouts.items():
            self.progress_text.insert(tk.END, f"Date: {date}\n")
            self.progress_text.insert(tk.END, "Workouts:\n")
            for workout in workouts:
                self.progress_text.insert(tk.END, f"  - {workout}\n")
            self.progress_text.insert(tk.END, "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = WorkoutTrackerApp(root)

    progress_button = ttk.Button(root, text="Show Progress", 
                                command=app.show_progress)
    progress_button.pack(pady=10)

    root.mainloop()







