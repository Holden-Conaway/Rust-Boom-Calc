import tkinter as tk
from tkinter import messagebox

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
    # Get the selected explosive type and quantity
    explosive_type = explosive_type_var.get()
    try:
        quantity = int(quantity_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for quantity.")
        return

    if explosive_type not in craftingRecipes:
        messagebox.showerror("Invalid Explosive", "Please select a valid explosive type.")
        return

    # Calculate the resources required and display the result
    result = calcResources(explosive_type, quantity)
    result_text.delete(1.0, tk.END)  # Clear the result box
    result_text.insert(tk.END, result)

# Set up the main window
root = tk.Tk()
root.title("Rust Boom Calculator")

# Set up the explosive type selection (dropdown)
explosive_type_label = tk.Label(root, text="Select Explosive Type:")
explosive_type_label.pack(pady=5)

explosive_type_var = tk.StringVar()
explosive_type_var.set("Satchel Charge")  # Default value
explosive_type_dropdown = tk.OptionMenu(root, explosive_type_var, *craftingRecipes.keys())
explosive_type_dropdown.pack(pady=5)

# Set up the quantity input
quantity_label = tk.Label(root, text="Enter Quantity:")
quantity_label.pack(pady=5)

quantity_entry = tk.Entry(root)
quantity_entry.pack(pady=5)

# Set up the calculate button
calculate_button = tk.Button(root, text="Calculate Resources", command=on_calculate)
calculate_button.pack(pady=10)

# Set up the result text box
result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=10)

# Run the application
root.mainloop()
