class ClothingItem:
    def __init__(self, item_id, name, category, size, color, price, stock):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.size = size
        self.color = color
        self.price = price
        self.stock = stock

    def display_info(self):
        return (f"ID: {self.item_id}\n"
                f"Name: {self.name}\n"
                f"Category: {self.category}\n"
                f"Size: {self.size}\n"
                f"Color: {self.color}\n"
                f"Price: UgX{self.price:.2f}\n"
                f"Stock: {self.stock} available\n")

    def update_stock(self, quantity):
        if self.stock + quantity < 0:
            raise ValueError("Insufficient stock to remove that quantity.")
        self.stock += quantity

    def apply_discount(self, discount_percentage):
        if 0 <= discount_percentage <= 100:
            self.price -= self.price * (discount_percentage / 100)
        else:
            raise ValueError("Discount percentage must be between 0 and 100.")


class Catalog:
    def __init__(self):
        self.items = {}

    def add_item(self, clothing_item):
        if clothing_item.item_id in self.items:
            raise ValueError("Item ID already exists in the catalog.")
        self.items[clothing_item.item_id] = clothing_item

    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
        else:
            raise KeyError("Item ID not found in the catalog.")

    def search_by_category(self, category):
        return [item for item in self.items.values() if item.category.lower() == category.lower()]

    def search_by_size(self, size):
        return [item for item in self.items.values() if item.size.lower() == size.lower()]

    def display_catalog(self):
        return "\n".join([item.display_info() for item in self.items.values()])


class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.cart = []

    def add_to_cart(self, item, quantity):
        if item.stock >= quantity:
            self.cart.append((item, quantity))
        else:
            raise ValueError(f"Insufficient stock for item {item.name}.")

    def checkout(self):
        total_cost = sum(item.price * quantity for item, quantity in self.cart)
        if self.balance >= total_cost:
            for item, quantity in self.cart:
                item.update_stock(-quantity)
            self.balance -= total_cost
            self.cart.clear()
            return f"Purchase successful! Remaining balance: UgX{self.balance:.2f}"
        else:
            raise ValueError("Insufficient balance for this purchase.")

    def view_cart(self):
        return "\n".join([f"{item.name} (x{quantity}): UgX{item.price * quantity:.2f}" 
                          for item, quantity in self.cart]) or "Your cart is empty."


# Example usage
if __name__ == "__main__":
    # Create catalog
    catalog = Catalog()
    
    # Add items
    catalog.add_item(ClothingItem(1, "T-Shirt", "Top", "M", "Blue", 19.99, 50))
    catalog.add_item(ClothingItem(2, "Jeans", "Bottom", "L", "Black", 49.99, 30))
    catalog.add_item(ClothingItem(3, "Jacket", "Outerwear", "M", "Green", 89.99, 10))
    
    # Display catalog
    print("Catalog:\n", catalog.display_catalog())
    
    # Search items
    print("\nSearch for 'Top':")
    for item in catalog.search_by_category("Top"):
        print(item.display_info())

    # Customer interactions
    customer = Customer("Alice", 150.00)
    tshirt = catalog.items[1]
    jacket = catalog.items[3]
    
    # Add to cart and checkout
    customer.add_to_cart(tshirt, 2)
    customer.add_to_cart(jacket, 1)
    print("\nCustomer's Cart:")
    print(customer.view_cart())
    
    print("\nCheckout:")
    print(customer.checkout())
    
    # Updated catalog
    print("\nUpdated Catalog:\n", catalog.display_catalog())
