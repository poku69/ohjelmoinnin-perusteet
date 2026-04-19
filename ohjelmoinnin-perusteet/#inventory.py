#inventory
def update_stock(self, product_id, amount, action):
        """
        Päivittää varastosaldoa.
        action voi olla joko 'restock' (lisäys) tai 'sell' (myynti).
        """
        # 1. Tarkistetaan, onko tuote olemassa
        if product_id not in self.inventory:
            print(f"Error: Product ID '{product_id}' not found.")
            return

        # 2. Varaston täydennys (Restock)
        if action == 'restock':
            self.inventory[product_id]['stock'] += amount
            new_stock = self.inventory[product_id]['stock']
            name = self.inventory[product_id]['name']
            print(f"Success: Restocked {amount} units. New stock for '{name}' is {new_stock}.")
        
        # 3. Tuotteen myynti (Sell)
        elif action == 'sell':
            current_stock = self.inventory[product_id]['stock']
            name = self.inventory[product_id]['name']
            
            # Tarkistetaan, ettei saldo mene miinukselle
            if current_stock >= amount:
                self.inventory[product_id]['stock'] -= amount
                print(f"Success: Sold {amount} units. Remaining stock for '{name}' is {current_stock - amount}.")
            else:
                print(f"Error: Not enough stock to sell {amount} units. Current stock is {current_stock}.")
        else:
            print("Error: Invalid action. Use 'restock' or 'sell'.")

    def search_product_by_name(self, search_term):
        """
        Etsii tuotetta sen nimen perusteella.
        """
        found_products = False
        print(f"\n--- Search Results for '{search_term}' ---")
        
        for prod_id, details in self.inventory.items():
            # Muutetaan sekä hakusana että tuotteen nimi pieniksi kirjaimiksi,
            # jotta haku toimii riippumatta isoista/pienistä kirjaimista.
            if search_term.lower() in details['name'].lower():
                print(f"ID: {prod_id} | Name: {details['name']} | Price: ${details['price']:.2f} | Stock: {details['stock']}")
                found_products = True
        
        if not found_products:
            print("No products found matching that name.")

    def remove_product(self, product_id):
        """
        Poistaa tuotteen kokonaan varastosta ID:n perusteella.
        """
        if product_id in self.inventory:
            removed_name = self.inventory[product_id]['name']
            del self.inventory[product_id] # Poistaa avaimen ja sen tiedot sanakirjasta
            print(f"Success: Product '{removed_name}' (ID: {product_id}) was removed from the inventory.")
        else:
            print(f"Error: Product ID '{product_id}' not found.")