import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    """Generate a random password based on user input."""
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return

        # Define character pools
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        special = string.punctuation

        # Ensure the password includes at least one of each character type
        all_characters = lower + upper + digits + special
        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
            random.choice(special),
        ]

        # Fill the rest of the password length with random choices from all characters
        password += random.choices(all_characters, k=length - 4)

        # Shuffle to ensure randomness
        random.shuffle(password)

        # Convert list to string and display the password
        generated_password = ''.join(password)
        password_display.config(state="normal")
        password_display.delete(0, tk.END)
        password_display.insert(0, generated_password)
        password_display.config(state="readonly")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")


# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.configure(bg="#1e272e")

# Title Label
title_label = tk.Label(
    root, text="Password Generator", font=("Helvetica", 20, "bold"), bg="#1e272e", fg="#f5f6fa"
)
title_label.pack(pady=20)

# Length Input
length_label = tk.Label(
    root, text="Enter Password Length:", font=("Helvetica", 14), bg="#1e272e", fg="#d2dae2"
)
length_label.pack(pady=5)
length_entry = tk.Entry(root, font=("Helvetica", 14), bd=2, relief="solid", justify="center")
length_entry.pack(pady=10)

# Generate Button
generate_button = tk.Button(
    root,
    text="Generate Password",
    font=("Helvetica", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    relief="flat",
    command=generate_password,
)
generate_button.pack(pady=15)

# Password Display
password_display_label = tk.Label(
    root, text="Generated Password:", font=("Helvetica", 14), bg="#1e272e", fg="#d2dae2"
)
password_display_label.pack(pady=5)
password_display = tk.Entry(
    root, font=("Helvetica", 14), bd=2, relief="solid", state="readonly", justify="center"
)
password_display.pack(pady=10)

# Footer
footer_label = tk.Label(
    root, text="© 2024 PasswordGen Inc.", font=("Helvetica", 10), bg="#1e272e", fg="#57606f"
)
footer_label.pack(side="bottom", pady=10)

# Run the Tkinter event loop
root.mainloop()
