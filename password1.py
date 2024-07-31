import tkinter as tk
import random
import string

# Function to generate a random password with letters and numbers

def generate_password():
    try:
        password_length = int(length_entry.get())
        # Only use letters and digits for character selection
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(password_length))
        password_entry.delete(0, tk.END)
        password_entry.insert(tk.END, password)
    except ValueError:
        password_entry.delete(0, tk.END)
        password_entry.insert(tk.END, "Invalid Length")

# Create the main window

root = tk.Tk()
root.title("Password Generator")


# Entry field for password display

password_entry = tk.Entry(root, width=20, font=("Arial", 16))
password_entry.grid(row=0, column=0, columnspan=2)


# Label for password length

length_label = tk.Label(root, text="Password Length:", font=("Arial", 14))
length_label.grid(row=1, column=0)


# Entry field for user input of password length

length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.grid(row=1, column=1)


# Button to generate password

generate_button = tk.Button(root, text="Generate Password", padx=20, pady=10, font=("Arial", 12), command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2)


# Run the main event loop

root.mainloop()
