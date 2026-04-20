import tkinter as tk
from tkinter import messagebox

# ---------- DATA ----------
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

products = []

# ---------- FUNCTIONS ----------
def add_product():
    try:
        product = Product(
            entry_id.get(),
            entry_name.get(),
            float(entry_price.get()),
            int(entry_stock.get())
        )
        products.append(product)
        messagebox.showinfo("Success", "Product added")
        clear_entries()
    except:
        messagebox.showerror("Error", "Invalid input")

def show_inventory():
    text_output.delete("1.0", tk.END)

    if not products:
        text_output.insert(tk.END, "Inventory is empty\n")
        return

    for p in products:
        text_output.insert(tk.END,
            f"{p.product_id} | {p.name} | {p.price}€ | Stock: {p.stock}\n"
        )

def search_product():
    keyword = entry_search.get().lower()
    text_output.delete("1.0", tk.END)

    results = [p for p in products if keyword in p.name.lower() or keyword in p.product_id.lower()]

    if not results:
        text_output.insert(tk.END, "No products found\n")
        return

    for p in results:
        text_output.insert(tk.END,
            f"{p.product_id} | {p.name} | {p.price}€ | Stock: {p.stock}\n"
        )

def update_stock():
    pid = entry_id.get()
    amount = int(entry_stock.get())

    for p in products:
        if p.product_id == pid:
            p.stock += amount
            messagebox.showinfo("Updated", f"New stock: {p.stock}")
            return

    messagebox.showerror("Error", "Product not found")

def remove_product():
    pid = entry_id.get()

    for p in products:
        if p.product_id == pid:
            products.remove(p)
            messagebox.showinfo("Removed", p.name)
            return

    messagebox.showerror("Error", "Product not found")

def clear_entries():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_stock.delete(0, tk.END)

# ---------- GUI ----------
root = tk.Tk()
root.title("Inventory System")
root.geometry("500x500")

# Inputs
tk.Label(root, text="Product ID").pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Price").pack()
entry_price = tk.Entry(root)
entry_price.pack()

tk.Label(root, text="Stock").pack()
entry_stock = tk.Entry(root)
entry_stock.pack()

tk.Label(root, text="Search").pack()
entry_search = tk.Entry(root)
entry_search.pack()

# Buttons
tk.Button(root, text="Add Product", command=add_product).pack(pady=5)
tk.Button(root, text="Show Inventory", command=show_inventory).pack(pady=5)
tk.Button(root, text="Search", command=search_product).pack(pady=5)
tk.Button(root, text="Update Stock (+)", command=update_stock).pack(pady=5)
tk.Button(root, text="Remove Product", command=remove_product).pack(pady=5)

# Output area
text_output = tk.Text(root, height=10)
text_output.pack()

root.mainloop()