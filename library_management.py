import json
import os

DATA_FILE = "library_data.json"


class Library:
    def __init__(self):
        self.books = []
        self.load_data()

    # ---------------- File Handling ----------------
    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                self.books = json.load(file)
        else:
            self.books = []

    def save_data(self):
        with open(DATA_FILE, "w") as file:
            json.dump(self.books, file, indent=4)

    # ---------------- Core Functions ----------------
    def add_book(self, book_id, title, author):
        for book in self.books:
            if book["book_id"] == book_id:
                print("Book ID already exists!")
                return

        self.books.append({
            "book_id": book_id,
            "title": title,
            "author": author,
            "issued_to": None
        })
        self.save_data()
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\nAvailable Books:")
        print("-" * 60)
        for book in self.books:
            status = "Available" if book["issued_to"] is None else f"Issued to {book['issued_to']}"
            print(f"ID: {book['book_id']} | Title: {book['title']} | Author: {book['author']} | Status: {status}")
        print("-" * 60)

    def issue_book(self, book_id, user_name):
        for book in self.books:
            if book["book_id"] == book_id:
                if book["issued_to"] is None:
                    book["issued_to"] = user_name
                    self.save_data()
                    print("Book issued successfully!")
                else:
                    print("Book is already issued.")
                return
        print("Book not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book["book_id"] == book_id:
                if book["issued_to"] is not None:
                    book["issued_to"] = None
                    self.save_data()
                    print("Book returned successfully!")
                else:
                    print("Book was not issued.")
                return
        print("Book not found.")


# ---------------- Main Menu ----------------
def main():
    library = Library()

    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            library.add_book(book_id, title, author)

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            book_id = input("Enter Book ID to issue: ")
            user_name = input("Enter User Name: ")
            library.issue_book(book_id, user_name)

        elif choice == "4":
            book_id = input("Enter Book ID to return: ")
            library.return_book(book_id)

        elif choice == "5":
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
