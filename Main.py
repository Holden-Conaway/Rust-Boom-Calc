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

# Apply a non-macOS theme for `ttk`
style = ttk.Style()
style.theme_use("clam")  # Use a theme that supports background colors

# Create a frame with background color
main_frame = tk.Frame(root, bg="#2c3e50")
main_frame.pack(fill="both", expand=True)

# Use `tk.Label` instead of `ttk.Label` for background color support
explosive_type_label = tk.Label(main_frame, text="Select Explosive Type:", background="#2c3e50", foreground="white", font=("Arial", 12))
explosive_type_label.pack(pady=5)

explosive_type_var = tk.StringVar()
explosive_type_var.set("Satchel Charge")
explosive_type_dropdown = ttk.Combobox(main_frame, textvariable=explosive_type_var, values=list(craftingRecipes.keys()), state="readonly")
explosive_type_dropdown.pack(pady=5)

# Quantity Input
quantity_label = tk.Label(main_frame, text="Enter Quantity:", background="#2c3e50", foreground="white", font=("Arial", 12))
quantity_label.pack(pady=5)

quantity_entry = tk.Entry(main_frame, font=("Arial", 14), justify="center")
quantity_entry.pack(pady=5, ipadx=5, ipady=5)

# Calculate Button
calculate_button = ttk.Button(main_frame, text="Calculate Resources", command=on_calculate)
calculate_button.pack(pady=10)

# Result Text Box
result_text = tk.Text(main_frame, height=10, width=50, state=tk.DISABLED, font=("Arial", 12), wrap=tk.WORD, bg="#ecf0f1")
result_text.pack(pady=10, padx=10)

# Run the application
root.mainloop()
