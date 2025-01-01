class Book:
    def __init__(self, book_id, title, author, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"[ID: {self.book_id}] {self.title} by {self.author} ({self.category}) - {status}"

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"User: {self.name} (ID: {self.user_id})"

class Library:
    def __init__(self):
        self.books = {}
        self.users = {}

    def add_book(self, book):
        if book.book_id in self.books:
            print("Book ID already exists.")
        else:
            self.books[book.book_id] = book
            print(f"Book '{book.title}' added to the library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print("Book removed from the library.")
        else:
            print("Book ID not found.")

    def search_books(self, query, by="title"):
        results = [
            book for book in self.books.values()
            if query.lower() in getattr(book, by).lower()
        ]
        if results:
            for book in results:
                print(book)
        else:
            print("No books found.")

    def borrow_book(self, book_id, user_id):
        if book_id not in self.books:
            print("Book ID not found.")
            return

        if user_id not in self.users:
            print("User ID not found.")
            return

        book = self.books[book_id]
        user = self.users[user_id]

        if book.is_available:
            book.is_available = False
            user.borrowed_books.append(book)
            print(f"Book '{book.title}' issued to {user.name}.")
        else:
            print("Book is currently not available.")

    def return_book(self, book_id, user_id):
        if user_id not in self.users:
            print("User ID not found.")
            return

        user = self.users[user_id]
        book = next((b for b in user.borrowed_books if b.book_id == book_id), None)

        if book:
            book.is_available = True
            user.borrowed_books.remove(book)
            print(f"Book '{book.title}' returned by {user.name}.")
        else:
            print("This user does not have the book borrowed.")

    def view_books(self):
        if self.books:
            for book in self.books.values():
                print(book)
        else:
            print("No books available in the library.")

    def add_user(self, user):
        if user.user_id in self.users:
            print("User ID already exists.")
        else:
            self.users[user.user_id] = user
            print(f"User '{user.name}' added to the library system.")

# Example usage
if __name__ == "__main__":
    library = Library()

    # Add users
    user1 = User(1, "Alice")
    user2 = User(2, "Bob")
    library.add_user(user1)
    library.add_user(user2)

    # Add books
    book1 = Book(101, "The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
    book2 = Book(102, "1984", "George Orwell", "Dystopian")
    library.add_book(book1)
    library.add_book(book2)

    # View books
    library.view_books()

    # Search books
    library.search_books("1984", by="title")

    # Borrow a book
    library.borrow_book(101, 1)

    # Return a book
    library.return_book(101, 1)

    # Remove a book
    library.remove_book(102)

    # View books
    library.view_books()
