import tkinter as tk
from tkinter import messagebox

class PasswordComplexityChecker:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Password Complexity Checker")

        self.password_label = tk.Label(self.window, text="Enter a password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.window, show="*")
        self.password_entry.pack()

        self.check_button = tk.Button(self.window, text="Check Password", command=self.check_password)
        self.check_button.pack()

        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

    def check_password(self):
        password = self.password_entry.get()
        strength = 0
        feedback = ""

        if len(password) < 8:
            feedback += "Password is too short. It should be at least 8 characters long.\n"
        else:
            strength += 1

        if not any(char.isupper() for char in password):
            feedback += "Password should contain at least one uppercase letter.\n"
        else:
            strength += 1

        if not any(char.islower() for char in password):
            feedback += "Password should contain at least one lowercase letter.\n"
        else:
            strength += 1

        if not any(char.isdigit() for char in password):
            feedback += "Password should contain at least one number.\n"
        else:
            strength += 1

        if not any(not char.isalnum() for char in password):
            feedback += "Password should contain at least one special character.\n"
        else:
            strength += 1

        if strength < 3:
            password_strength = "Weak"
        elif strength == 3:
            password_strength = "Medium"
        else:
            password_strength = "Strong"

        self.result_label.config(text=f"Password strength: {password_strength}\n{feedback}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    checker = PasswordComplexityChecker()
    checker.run()
