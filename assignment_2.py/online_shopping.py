class Product:
    def __init__(self, product_name, price, available_in_stock):  #initializes a product 
        self.product_name = product_name  
        self.price = price  
        self.available_in_stock = available_in_stock  

    def display_product_info(self):  #display product information
        print("Product:", self.product_name)
        print("Price:", self.price)
        print("Stock:", self.available_in_stock)

class ShoppingCart:   #initializes an empty list to hold the items added to the cart
    def __init__(self):
        self.items = [] 

    # stock checking fun
    def add_to_cart(self, product, quantity):  #add specific items and quantity  to the shopping cart
        if product.available_in_stock >= quantity: # Adds the product and its quantity to the cart if enough stock is available
            self.items.append([product, quantity]) 
            product.available_in_stock -= quantity # Reduces the available stock of the product 
            print(f"Added {quantity} {product.product_name}(s) to the cart.")
        else: # Notifies the user if there is insufficient stock
            print("Not enough stock.")

    def display_cart(self):
        print("Cart contains:")
        for item in self.items:
            product, quantity = item
            print(f"{product.product_name}: {quantity} unit(s)")

    def calculate_total(self): #calc total cost in the cart
        total = 0
        for item in self.items:
            product, quantity = item
            total += product.price * quantity #total cost
        return total

product1 = Product("Laptop", 1000, 15)
product2 = Product("Phone", 500, 6)
product3 = Product("books", 1000, 0)

cart = ShoppingCart()
cart.add_to_cart(product1, 10)
cart.add_to_cart(product2, 2)
cart.add_to_cart(product3,1)

cart.display_cart()

# total cost
total = cart.calculate_total()
print("Total cost:", total)
