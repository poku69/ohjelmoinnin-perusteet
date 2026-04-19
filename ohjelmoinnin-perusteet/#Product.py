products = []
product_counter = 0

class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock


def add_product():
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock: "))

    product = Product(product_id, name, price, stock)
    products.append(product)

    print("Product added successfully!")

if __name__ == "__main__":
    main()

def inventory():
    if not products:
        print("Inventory is empty.")
        return
    
    print("Inventory:")
    print(f"{'ID':<10}{'Name':<20}{'Price':<10}{'Stock':<10}")
    print("-" * 50)
        
    for product in products:
        print(f"{product.product_id:<10}{product.name:<20}{product.price:<10}{product.stock:<10}")

    print()