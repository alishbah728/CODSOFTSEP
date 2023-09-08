import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    if password_length <= 0:
        password_display.config(text="Invalid Length")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(password_length))
    password_display.config(text=password)

root = tk.Tk()
root.title("Password Generator")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="Password Length:")
label.pack()

length_entry = tk.Entry(frame)
length_entry.pack()

generate_button = tk.Button(frame, text="Generate Password", command=generate_password)
generate_button.pack()

password_display = tk.Label(frame, text="", pady=10)
password_display.pack()

root.mainloop()
