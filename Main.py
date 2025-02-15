import tkinter as tk
from tkinter import messagebox, ttk

# Crafting recipes dictionary
craftingRecipes = {
    "Satchel Charge": {
        "sulfur": 480,
        "charcoal": 480,
        "metal frags": 80,
        "rope": 1,
        "small stash": 1
    },
    "Explo Ammo": {
        "metal frag": 5,
        "gunpowder": 10,
        "sulfur": 5
    },
    "Rocket": {
        "metal frags": 100,
        "low grade": 30,
        "sulfur": 1400,
        "charcoal": 1400,
        "metal pipe": 2
    },
    "C4": {
        "charcoal": 2000,
        "metal frags": 200,
        "low grade": 60,
        "sulfur": 2200,
        "cloth": 5,
        "tech trash": 2
    }
}

def calcResources(exploType, quantity):
    if exploType not in craftingRecipes:
        return f"Error: That isn't a valid explosive type."

    recipe = craftingRecipes[exploType]
    totalResources = {resource: amount * quantity for resource, amount in recipe.items()}

    result = f"To craft {quantity} {exploType}(s), you need:\n"
    for resource, amount in totalResources.items():
        result += f"- {amount} {resource}\n"

    return result

def on_calculate():
    explosive_type = explosive_type_var.get()
    try:
        quantity = int(quantity_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for quantity.")
        return

    if explosive_type not in craftingRecipes:
        messagebox.showerror("Invalid Explosive", "Please select a valid explosive type.")
        return

    result = calcResources(explosive_type, quantity)
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)
    result_text.config(state=tk.DISABLED)

# Set up the main window
root = tk.Tk()
root.title("Rust Boom Calculator")
root.geometry("400x400")
root.configure(bg="#2c3e50")

style = ttk.Style()
style.configure("TLabel", foreground="white", background="#2c3e50", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TEntry", font=("Arial", 12))
style.configure("TCombobox", font=("Arial", 12))

# Explosive Type Selection
explosive_type_label = ttk.Label(root, text="Select Explosive Type:")
explosive_type_label.pack(pady=5)

explosive_type_var = tk.StringVar()
explosive_type_var.set("Satchel Charge")
explosive_type_dropdown = ttk.Combobox(root, textvariable=explosive_type_var, values=list(craftingRecipes.keys()), state="readonly")
explosive_type_dropdown.pack(pady=5)

# Quantity Input
quantity_label = ttk.Label(root, text="Enter Quantity:")
quantity_label.pack(pady=5)

quantity_entry = ttk.Entry(root, font=("Arial", 14), justify="center")
quantity_entry.pack(pady=5, ipadx=5, ipady=5)

# Calculate Button
calculate_button = ttk.Button(root, text="Calculate Resources", command=on_calculate)
calculate_button.pack(pady=10)

# Result Text Box
result_text = tk.Text(root, height=10, width=50, state=tk.DISABLED, font=("Arial", 12), wrap=tk.WORD, bg="#ecf0f1")
result_text.pack(pady=10, padx=10)

# Run the application
root.mainloop()
