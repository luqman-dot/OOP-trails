from datetime import datetime

class Product:
    """Base class for products in an inventory."""
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def purchase(self, amount=1):
        if amount > self.quantity:
            raise ValueError(f"Not enough stock for '{self.name}'. Available: {self.quantity}")
        self.quantity -= amount
        print(f"Purchased {amount} of '{self.name}'. Remaining stock: {self.quantity}")

    def restock(self, amount):
        if amount <= 0:
            raise ValueError("Restock amount must be greater than zero.")
        self.quantity += amount
        print(f"Restocked {amount} of '{self.name}'. Total stock: {self.quantity}")

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}, Stock: {self.quantity}"

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"


class Food(Product):
    """Represents food items in the inventory."""
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date

    def is_expired(self):
        return datetime.now().date() > self.expiration_date

    def __str__(self):
        return f"Food: {super().__str__()}, Expires: {self.expiration_date}"


class Electronics(Product):
    """Represents electronic items in the inventory."""
    def __init__(self, name, price, quantity, warranty_years):
        super().__init__(name, price, quantity)
        self.warranty_years = warranty_years

    def warranty_expiration(self):
        purchase_year = datetime.now().year
        return purchase_year + self.warranty_years

    def __str__(self):
        return f"Electronics: {super().__str__()}, Warranty: {self.warranty_years} years"


class Inventory:
    """Represents the store's inventory system."""
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added.")
        self.products.append(product)
        print(f"Added '{product.name}' to inventory.")

    def search(self, keyword):
        return [product for product in self.products if keyword.lower() in product.name.lower()]

    def list_inventory(self):
        if not self.products:
            print("The inventory is empty.")
        else:
            for product in self.products:
                print(product)

    def __len__(self):
        return len(self.products)


# Example Usage
store_inventory = Inventory()

# Add some products
apple = Food("Apple", 0.50, 100, datetime(2025, 1, 15).date())
laptop = Electronics("Laptop", 999.99, 5, 2)

store_inventory.add_product(apple)
store_inventory.add_product(laptop)

# List all products
store_inventory.list_inventory()

# Search for a product
search_results = store_inventory.search("Laptop")
print("Search Results:", search_results)

# Purchase products
apple.purchase(10)
laptop.purchase(1)

# Restock products
apple.restock(50)

# Check expiration and warranty
print(f"Is '{apple.name}' expired? {'Yes' if apple.is_expired() else 'No'}")
print(f"'{laptop.name}' warranty expires in the year {laptop.warranty_expiration()}")
