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

    print("Product added")


def inventory():
    if not products:
        print("Inventory is empty")
        return

    print("Inventory:")
    print(f"{'ID':<10}{'Name':<20}{'Price':<10}{'Stock':<10}")

    print("-" * 50)

    for product in products:
        print(f"{product.product_id:<10}{product.name:<20}{product.price:<10}{product.stock:<10}")

    print()

#sampan koodi tuotteiden etsimiseen

def search():
    search = input("Enter product nameor ID: ").lower() 
    
    results = [p for p in products if search in p.name.lower()or search in p.product_id.lower()]  #etsii tuotteita
    
    if not results:
        print("No products found")                  #jos ei löydy tuotetta
        return                                      #palaa takaisin
    
    print(f"{'ID':<10}{'Name':<20}{'Price':<10}{'Stock':<10}")              #otsikko rivi kohdalleen
    print("-" * 50)                                                         #muutama viiva erottamaan
    
    for product in results:
          print(f"{product.product_id:<10}{product.name:<20}{product.price:<10}{product.stock:<10}")        #tulostaa tuotteet kohdalleen
    print()



def UI():
    while True:
        print("1. Add Product")
        print("2. Inventory")
        print("3. Search Product")
        print("4. Update Stock")  #lisätty valikkoon kohta varaston päivittämiseen


        choice = input("Choose: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            inventory()
        elif choice == "3":
            search()                #alkuvalikossa tapa etsiä tuotteita
        elif choice == "4":
            update_stock()          #lisätty valikkoon kohta varaston päivittämiseen
        else:
            print("Invalid choice")


if __name__ == "__main__":

#kristianin koodia
    def update_stock():
        #kysytään päivitettävän tuotteen ID
        product_id = input("Enter product ID to update: ")
        target_product = None
        for product in products:
            #tarkistetaan täsmääkö id jo olemassa olevan id:n kanssa
            if product.product_id == product_id:
                target_product = product
                break

            if not target_products: 
                print(f"no product found with that ID{product_id}")
                return
            #jos tuotetta ei löydy palataan alkuun¨
            action = input("Type "restock" to add inventory or "sell" to remocve from inventory:").lower()
            #kysytään halutaanko lisätä vai poistaa varastosta
            # .lower() muuttaa pieniksi kirjaimiksi
            if action in ["restock", "sell"]:
                amount = int(input("Enter amount: "))
                if action == "restock":
                    target_product.stock += amount
                    print(f"Restocked {amount} units. New stock for '{target_product.name}' is {target_product.stock}.")
                elif action == "sell":
                    if target_product.stock >= amount:
                        target_product.stock -= amount
                        print(f"Sold {amount} units. Remaining stock for '{target_product.name}' is {target_product.stock}.")
                    else:
                        print(f"Not enough stock to sell {amount} units. Current stock is {target_product.stock}.")


