import tkinter as tk
from PIL import Image, ImageTk

def login():
    name = name_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    # Perform login validation or any other necessary processing
    result_label.config(text=f"Welcome, {name}! You have logged in successfully.")

def signup():
    # Perform sign-up functionality or open sign-up window
    signup_label.config(text="Sign up button clicked!")

# Create the main window
window = tk.Tk()
window.title("Login Widget")

# Set background color
window.configure(bg="#007BFF")  # Blue color

# Set text color
text_color = "white"
button_text_color = "black"

# Load and resize the image
image = Image.open("your_image_file.png")
image = image.resize((100, 100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

# Create image label
image_label = tk.Label(window, image=photo, bg="#007BFF")
image_label.image = photo  # Keep a reference to prevent garbage collection

# Create labels
name_label = tk.Label(window, text="Name:", bg="#007BFF", fg=text_color)  # Blue background and white text
username_label = tk.Label(window, text="Username:", bg="#007BFF", fg=text_color)
password_label = tk.Label(window, text="Password:", bg="#007BFF", fg=text_color)

# Create entry fields
name_entry = tk.Entry(window)
username_entry = tk.Entry(window)
password_entry = tk.Entry(window, show="*")

# Create login button
login_button = tk.Button(window, text="Login", command=login, bg="#0056b3", fg=button_text_color)  # Darker blue background

# Create sign-up button
signup_button = tk.Button(window, text="Sign Up", command=signup, bg="#0056b3", fg=button_text_color)  # Darker blue background

# Create result labels
result_label = tk.Label(window, bg="#007BFF", fg=text_color)
signup_label = tk.Label(window, bg="#007BFF", fg=text_color)

image_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
name_label.grid(row=1, column=0, padx=10, pady=5, sticky="E")
name_entry.grid(row=1, column=1, padx=10, pady=5)
username_label.grid(row=2, column=0, padx=10, pady=5, sticky="E")
username_entry.grid(row=2, column=1, padx=10, pady=5)
password_label.grid(row=3, column=0, padx=10, pady=5, sticky="E")
password_entry.grid(row=3, column=1, padx=10, pady=5)
login_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
signup_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
signup_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

# Start the main loop
window.mainloop()
