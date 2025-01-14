class ClothingItem:
    def __init__(self, item_id: int, name: str, category: str, size: str, color: str, price: float, stock: int):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.size = size
        self.color = color
        self.price = price
        self.stock = stock

    def display_info(self) -> str:
        return (f"ID: {self.item_id}\n"
                f"Name: {self.name}\n"
                f"Category: {self.category}\n"
                f"Size: {self.size}\n"
                f"Color: {self.color}\n"
                f"Price: ${self.price:.2f}\n"
                f"Stock: {self.stock} available\n")

    def update_stock(self, quantity: int):
        if self.stock + quantity < 0:
            raise ValueError(f"Insufficient stock to remove {abs(quantity)} items.")
        self.stock += quantity

    def apply_discount(self, discount_percentage: float):
        if not 0 <= discount_percentage <= 100:
            raise ValueError("Discount percentage must be between 0 and 100.")
        self.price -= self.price * (discount_percentage / 100)


class Catalog:
    def __init__(self):
        self.items = {}

    def add_item(self, clothing_item: ClothingItem):
        if clothing_item.item_id in self.items:
            raise ValueError("Item ID already exists in the catalog.")
        self.items[clothing_item.item_id] = clothing_item

    def remove_item(self, item_id: int):
        if item_id not in self.items:
            raise KeyError("Item ID not found in the catalog.")
        del self.items[item_id]

    def search_items(self, category: str = None, size: str = None) -> list:
        results = self.items.values()
        if category:
            results = [item for item in results if item.category.lower() == category.lower()]
        if size:
            results = [item for item in results if item.size.lower() == size.lower()]
        return results

    def display_catalog(self) -> str:
        if not self.items:
            return "The catalog is empty."
        return "\n".join([item.display_info() for item in self.items.values()])

    def summary(self) -> str:
        total_stock = sum(item.stock for item in self.items.values())
        total_value = sum(item.price * item.stock for item in self.items.values())
        return (f"Total Items in Stock: {total_stock}\n"
                f"Total Catalog Value: ${total_value:.2f}")


class Customer:
    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance
        self.cart = []
        self.order_history = []

    def add_to_cart(self, item: ClothingItem, quantity: int):
        if item.stock < quantity:
            raise ValueError(f"Insufficient stock for item '{item.name}'.")
        self.cart.append((item, quantity))

    def checkout(self) -> str:
        total_cost = sum(item.price * quantity for item, quantity in self.cart)
        if self.balance < total_cost:
            raise ValueError("Insufficient balance for this purchase.")
        for item, quantity in self.cart:
            item.update_stock(-quantity)
        self.balance -= total_cost
        self.order_history.append(self.cart.copy())
        self.cart.clear()
        return f"Purchase successful! Remaining balance: ${self.balance:.2f}"

    def view_cart(self) -> str:
        if not self.cart:
            return "Your cart is empty."
        return "\n".join([f"{item.name} (x{quantity}): ${item.price * quantity:.2f}"
                          for item, quantity in self.cart])

    def view_order_history(self) -> str:
        if not self.order_history:
            return "No past purchases."
        history = []
        for i, order in enumerate(self.order_history, 1):
            history.append(f"Order {i}:\n" + "\n".join(
                [f"{item.name} (x{quantity}): ${item.price * quantity:.2f}" for item, quantity in order]))
        return "\n\n".join(history)


# Main Program
if __name__ == "__main__":
    catalog = Catalog()

    # Add items to catalog
    catalog.add_item(ClothingItem(1, "T-Shirt", "Top", "M", "Blue", 19.99, 50))
    catalog.add_item(ClothingItem(2, "Jeans", "Bottom", "L", "Black", 49.99, 30))
    catalog.add_item(ClothingItem(3, "Jacket", "Outerwear", "M", "Green", 89.99, 10))

    # Customer creation
    customer = Customer("Alice", 150.00)

    # Display catalog
    print("=== Catalog ===")
    print(catalog.display_catalog())

    # Search by category
    print("\n=== Search Results for 'Top' ===")
    for item in catalog.search_items(category="Top"):
        print(item.display_info())

    # Customer adds to cart
    customer.add_to_cart(catalog.items[1], 2)
    customer.add_to_cart(catalog.items[3], 1)

    # View cart
    print("\n=== Customer's Cart ===")
    print(customer.view_cart())

    # Checkout
    print("\n=== Checkout ===")
    try:
        print(customer.checkout())
    except ValueError as e:
        print(f"Error: {e}")

    # View updated catalog
    print("\n=== Updated Catalog ===")
    print(catalog.display_catalog())

    # Display order history
    print("\n=== Order History ===")
    print(customer.view_order_history())

    # Catalog summary
    print("\n=== Catalog Summary ===")
    print(catalog.summary())
