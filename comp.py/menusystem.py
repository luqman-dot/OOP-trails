# Restaurant Ordering System

class RestaurantOrderingSystem:
    def __init__(self):
        # Predefined menu (can be extended to use a database)
        self.menu = {
            1: {"name": "Burger", "price": 5000},
            2: {"name": "Pizza", "price": 8000},
            3: {"name": "Pasta", "price": 7000},
            4: {"name": "Salad", "price": 4000},
            5: {"name": "Soda", "price": 1000},
        }
        self.order = []

    def display_menu(self):
        print("\n--- Menu ---")
        for item_id, item in self.menu.items():
            print(f"{item_id}. {item['name']} - UgX {item['price']:.1f}")
        print("-------------------")

    def add_to_order(self):
        try:
            item_id = int(input("Enter the item number to order (or 0 to stop): "))
            if item_id == 0:
                return False
            if item_id in self.menu:
                quantity = int(input(f"Enter quantity for {self.menu[item_id]['name']}: "))
                if quantity > 0:
                    self.order.append({"item": self.menu[item_id], "quantity": quantity})
                    print(f"Added {quantity} x {self.menu[item_id]['name']} to the order.")
                else:
                    print("Quantity must be greater than 0.")
            else:
                print("Invalid item number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
        return True

    def calculate_bill(self):
        print("\n--- Your Order ---")
        total = 0
        for order_item in self.order:
            item_name = order_item["item"]["name"]
            item_price = order_item["item"]["price"]
            quantity = order_item["quantity"]
            cost = item_price * quantity
            total += cost
            print(f"{item_name} x {quantity} = UgX {cost:.2f}")
        print(f"Total Bill: UgX {total:.1f}")
        print("-------------------")

    def run(self):
        print("Welcome to the Restaurant Ordering System!")
        while True:
            print("\n1. View Menu")
            print("2. Place Order")
            print("3. View Bill")
            print("4. Exit")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.display_menu()
                elif choice == 2:
                    while self.add_to_order():
                        pass
                elif choice == 3:
                    self.calculate_bill()
                elif choice == 4:
                    print("Thank you for visiting! Goodbye.")
                    break
                else:
                    print("Invalid choice. Please select from the menu.")
            except ValueError:
                print("Please enter a valid choice.")


# Run the system
if __name__ == "__main__":
    system = RestaurantOrderingSystem()
    system.run()
