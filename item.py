class Item:
    def calculate_total_price(self, x, y):
        return x * y

item_1 = Item()
item_1.name = "luqman"
item_1.price = 20000
item_1.quantity = 5
print(item_1.calculate_total_price(item_1.price, item_1.quantity))

item_2 = Item()
item_2.name = "kyembe"
item_2.price = 500000
item_2.quantity = 10
print(item_2.calculate_total_price(item_2.price, item_2.quantity))
