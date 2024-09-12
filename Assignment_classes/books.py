class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def show_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")


book = Book("ignorance is bliss", "Luqman Kyembe", 2024)
book.show_info()
