import tkinter as tk
from tkinter import messagebox

# Menu data
veg_menu = {
    "Paneer Masala": 230,
    "Dal-Bati": 250,
    "Masura": 190,
    "Kaju Curry": 210,
    "Veg Patiyala": 340
}

non_veg_menu = {
    "Mutton": ["Mutton Masala", "Mutton Bhakri", "Mutton Biryani"],
    "Chicken": ["Chicken Masala", "Chicken Special", "Chicken Biryani"],
    "Fish": ["Fish Gravy", "Fish Fry", "Fish Curry"]
}

# Main Application Window
root = tk.Tk()
root.title("Welcome to Our Restaurant")
root.geometry("400x400")


def show_veg_menu():
    clear_frame()
    tk.Label(root, text="Veg Menu", font=("Arial", 16)).pack(pady=10)

    for dish, price in veg_menu.items():
        btn = tk.Button(root, text=f"{dish} - ₹{price}", command=lambda d=dish: show_order(d))
        btn.pack(pady=5)


def show_nonveg_types():
    clear_frame()
    tk.Label(root, text="Select Non-Veg Type", font=("Arial", 16)).pack(pady=10)

    for category in non_veg_menu:
        btn = tk.Button(root, text=category, command=lambda c=category: show_nonveg_menu(c))
        btn.pack(pady=5)


def show_nonveg_menu(category):
    clear_frame()
    tk.Label(root, text=f"{category} Menu", font=("Arial", 16)).pack(pady=10)

    for dish in non_veg_menu[category]:
        btn = tk.Button(root, text=dish, command=lambda d=dish: show_order(d))
        btn.pack(pady=5)


def show_order(dish):
    messagebox.showinfo("Order Placed", f"Enjoy your {dish}! 🍽️")


def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()


def main_menu():
    clear_frame()
    tk.Label(root, text="Welcome to Our Restaurant", font=("Arial", 18)).pack(pady=20)

    tk.Button(root, text="Veg", width=20, command=show_veg_menu).pack(pady=10)
    tk.Button(root, text="Non-Veg", width=20, command=show_nonveg_types).pack(pady=10)


# Launch the app
main_menu()
root.mainloop()
