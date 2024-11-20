import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero."
        else:
            result = "Invalid operation!"

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Simple Calculator")
window_width = 400
window_height = 300
root.geometry(f"{window_width}x{window_height}")
root.configure(bg='#f0f0f0') 

tk.Label(root, text="Enter first number:", bg='#f0f0f0', font=("Arial", 14)).pack(pady=5)
entry_num1 = tk.Entry(root, font=("Arial", 14), bd=5, relief="solid")
entry_num1.pack(pady=5)

tk.Label(root, text="Enter second number:", bg='#f0f0f0', font=("Arial", 14)).pack(pady=5)
entry_num2 = tk.Entry(root, font=("Arial", 14), bd=5, relief="solid")
entry_num2.pack(pady=5)

tk.Label(root, text="Select operation:", bg='#f0f0f0', font=("Arial", 14)).pack(pady=5)
operation_var = tk.StringVar(root)
operation_var.set('+') 
operation_menu = tk.OptionMenu(root, operation_var, '+', '-', '*', '/')
operation_menu.config(font=("Arial", 14), bg='#e0e0e0', relief="solid")
operation_menu.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate", font=("Arial", 14), bg='#4CAF50', fg='white', bd=0, relief="solid", command=calculate)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="Result: ", bg='#f0f0f0', font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
