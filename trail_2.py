class Phone:
    def __init__(self, brand, model, price, storage):
        # Initialize the attributes for the phone
        self.brand = brand
        self.model = model
        self.price = price
        self.storage = storage

    # Method to show phone details
    def show_info(self):
        print("Phone Details:")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price: UGX", self.price)
        print("Storage:", self.storage, "GB")

    # Method to simulate making a call
    def make_call(self, phone_number):
        print(f"Calling {phone_number} using {self.model}...")

    # Method to simulate sending a message
    def send_message(self, phone_number, message):
        print(f"Sending message to {phone_number}: {message}")

my_phone = Phone("Apple", "iPhone 14", 1.500 , 128)
phone2 = Phone("Samsung", "Galaxy S23", 899.000, 256)

my_phone.show_info()            
my_phone.make_call("123-456-7890") 
my_phone.send_message("987-654-3210", "Hello, how are you?")
