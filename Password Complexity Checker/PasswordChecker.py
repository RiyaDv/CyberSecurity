import re
import tkinter as tk
from tkinter import messagebox

def password_strength(password):
    strength = 0
    feedback = []

    # Criteria for password strength
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Strength assessment
    if strength == 5:
        feedback.append("Password strength: Very Strong")
    elif strength == 4:
        feedback.append("Password strength: Strong")
    elif strength == 3:
        feedback.append("Password strength: Medium")
    else:
        feedback.append("Password strength: Weak")

    return feedback

def check_password():
    password = entry.get()
    feedback = password_strength(password)
    messagebox.showinfo("Password Strength", "\n".join(feedback))

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Instructions
instructions = tk.Label(root, text="To create a strong password, ensure it meets the following criteria:\n"
                                    "1. At least 8 characters long\n"
                                    "2. Contains at least one lowercase letter (a-z)\n"
                                    "3. Contains at least one uppercase letter (A-Z)\n"
                                    "4. Contains at least one number (0-9)\n"
                                    "5. Contains at least one special character (!@#$%^&*(),.?\":{}|<>)")
instructions.pack(pady=10)

# Password entry
entry_label = tk.Label(root, text="Enter a password:")
entry_label.pack(pady=5)

entry = tk.Entry(root, show="*")
entry.pack(pady=5)

# Check button
check_button = tk.Button(root, text="Check Password Strength", command=check_password)
check_button.pack(pady=10)

# Run the application
root.mainloop()
