import json

def save_products():
    with open("products.json", "w") as file:
        json.dump([p.__dict__ for p in products], file)

def load_products():
    try:
        with open("products.json", "r") as file:
            data = json.load(file)
            return [Product(**d) for d in data]
    except FileNotFoundError:
        return []                                         #Tuotteiden tallennus ja lataus ^

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

    save_products()

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




#kristianin koodia
def update_stock():
    product_id = input("Enter product ID: ").strip()

    
    product = None
    #oletaan aluksi ettei tuotetta löydy
    for p in products:
        if p.product_id == product_id:
            product = p
            break
#etsitään tuote Id:n avulla, jos ei löydy palataan alkuun
#koodi käy läpi product listan ja hakee listalta saman id:n jos sellaine on

    
    if product is None:
        print("Product not found")
        return
    #jos tuotetta ei ole palataan alkuun

    print(f"Product: {product.name} | Current stock: {product.stock}")
    print("1. Restock (add items)")
    print("2. Sell (remove items)")
    #kysytään lisätäänkö vai vähennetäänkö varastosta

    choice = input("Choose: ").strip()

    # Tarkistetaan onko tuotetta tarpeaksi ja ettei pyyntö ole negatiivinen
    try:
        amount = int(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be positive")
            return
    except ValueError:
        print("Invalid amount")
        return
#jos ei hyväksytty luku palataan alkuun

    if choice == "1":
        # Lisätään varastoon
        product.stock += amount
        print(f"Restocked {amount} units. New stock: {product.stock}")

    elif choice == "2":
        # Tarkistetaan onko tuotetta tarpeaksi
        if amount > product.stock:
            print(f"Not enough stock! Available: {product.stock}")
            return
        
        # Vähennetään tuote varastosta ja lasketaan myyntitulo
        product.stock -= amount
        total = amount * product.price
        print(f"Sold {amount} units. New stock: {product.stock} | Total sale: {total:.2f}€")
#total:.2f muuttaa hinnan kahden desimaalin tarkuuteen
    else:
        print("Invalid choice")
        #jos ei hyväksytty vaihtoehto palataan alkuun
    



def UI():
    while True:
        print("1. Add Product")
        print("2. Inventory")
        print("3. Search Product")
        print("4. Update Stock")  #lisätty valikkoon kohta varaston päivittämiseen
        print("5. Remove Product")  #lisätty valikkoon kohta tuotteen poistamiseen
        print("6. Exit")
        
        choice = input("Choose: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            inventory()
        elif choice == "3":
            search()                #alkuvalikossa tapa etsiä tuotteita
        elif choice == "4":
            update_stock()   #lisätty valikkoon kohta varaston päivittämiseen
        elif choice == "5":
            remove_product()
        elif choice =="6":
            exit()  
        else:
            print("Invalid choice")

def remove_product ():
    product_id = input("Enter product ID to remove: ").strip()
    for i, p in enumerate (products):
        if p.product_id == product_id:
            print(f"Removed: {p.name}")
            products.pop(i)
            return
        
print ("Product not found")

if __name__ == "__main__":
    products = load_products()                                         
    UI()



