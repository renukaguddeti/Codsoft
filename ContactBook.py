import tkinter as tk
from tkinter import messagebox

# Dictionary to store contacts
contacts = {}

# Function to add or update a contact
def save_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:  # Ensure that name and phone are provided
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        messagebox.showinfo("Success", f"Contact '{name}' saved successfully!")
        clear_fields()
        update_contact_list()
    else:
        messagebox.showwarning("Input Error", "Name and Phone are required!")

# Function to delete a contact
def delete_contact():
    selected = contact_list.curselection()
    if selected:
        name = contact_list.get(selected).split(" - ")[0]
        del contacts[name]
        messagebox.showinfo("Deleted", f"Contact '{name}' deleted successfully!")
        update_contact_list()
    else:
        messagebox.showwarning("Selection Error", "Select a contact to delete!")

# Function to search contacts
def search_contact():
    query = search_entry.get().lower()
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        if query in name.lower() or query in details['Phone']:
            contact_list.insert(tk.END, f"{name} - {details['Phone']}")

# Function to update the contact list display
def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} - {details['Phone']}")

# Function to clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

# Initialize main window
root = tk.Tk()
root.title("Contact Manager")
root.geometry("500x500")
root.configure(bg="#f0f8ff")  # Light blue background

# Title label
tk.Label(root, text="Contact Manager", font=("Helvetica", 16, "bold"), bg="#f0f8ff").pack(pady=10)

# Input fields
frame_inputs = tk.Frame(root, bg="#f0f8ff")
frame_inputs.pack(pady=10)
tk.Label(frame_inputs, text="Name:", bg="#f0f8ff").grid(row=0, column=0, padx=5, pady=5, sticky="e")
name_entry = tk.Entry(frame_inputs, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Phone:", bg="#f0f8ff").grid(row=1, column=0, padx=5, pady=5, sticky="e")
phone_entry = tk.Entry(frame_inputs, width=30)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Email:", bg="#f0f8ff").grid(row=2, column=0, padx=5, pady=5, sticky="e")
email_entry = tk.Entry(frame_inputs, width=30)
email_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Address:", bg="#f0f8ff").grid(row=3, column=0, padx=5, pady=5, sticky="e")
address_entry = tk.Entry(frame_inputs, width=30)
address_entry.grid(row=3, column=1, padx=5, pady=5)

# Buttons
frame_buttons = tk.Frame(root, bg="#f0f8ff")
frame_buttons.pack(pady=10)
tk.Button(frame_buttons, text="Save Contact", command=save_contact, width=15, bg="#32cd32", fg="white").grid(row=0, column=0, padx=10, pady=5)
tk.Button(frame_buttons, text="Delete Contact", command=delete_contact, width=15, bg="#ff6347", fg="white").grid(row=0, column=1, padx=10, pady=5)

# Search bar
tk.Label(root, text="Search by Name or Phone:", bg="#f0f8ff").pack(pady=5)
search_entry = tk.Entry(root, width=40)
search_entry.pack(pady=5)
tk.Button(root, text="Search", command=search_contact, width=10, bg="#4682b4", fg="white").pack(pady=5)

# Contact list display
tk.Label(root, text="Contact List:", font=("Helvetica", 12, "bold"), bg="#f0f8ff").pack(pady=10)
contact_list = tk.Listbox(root, width=50, height=15)
contact_list.pack(pady=10)

# Refresh the contact list
update_contact_list()

# Run the application
root.mainloop()
