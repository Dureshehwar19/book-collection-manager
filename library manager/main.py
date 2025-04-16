import json

class BookCollection:
    """This class helps you manage a list of books — add, update, search, or delete books."""

    def __init__(self):
        """Start with an empty list of books and load any saved books from a file."""
        self.book_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()

    def read_from_file(self):
        """Try to load books from a file. If the file doesn't exist or is broken, start fresh."""
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        """Save the book list to a file so it doesn’t get lost when the program closes."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self):
        """Ask the user to enter a new book and add it to the list."""
        book_title = input("Enter the book title: ")
        book_author = input("Enter the author's name: ")
        publication_year = input("Enter the year it was published: ")
        book_genre = input("Enter the genre: ")
        is_book_read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read,
        }

        self.book_list.append(new_book)
        self.save_to_file()
        print("✅ Book added successfully!\n")

    def delete_book(self):
        """Ask for a title and delete that book if found."""
        book_title = input("Enter the title of the book you want to delete: ")

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print("🗑️ Book deleted successfully!\n")
                return
        print("⚠️ Book not found.\n")

    def find_book(self):
        """Search for books by title or author."""
        input("Search by:\n1. Title\n2. Author\nPress Enter to continue...")  # simplified
        search_text = input("Enter what you want to search for: ").lower()

        found_books = [
            book for book in self.book_list
            if search_text in book["title"].lower() or search_text in book["author"].lower()
        ]

        if found_books:
            print("\n📚 Books found:")
            for index, book in enumerate(found_books, 1):
                status = "Read" if book["read"] else "Unread"
                print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
            print()
        else:
            print("❌ No books matched your search.\n")

    def update_book(self):
        """Change the details of a book."""
        book_title = input("Enter the title of the book you want to update: ")

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("Leave any input blank if you don't want to change it.")
                book["title"] = input(f"New title ({book['title']}): ") or book["title"]
                book["author"] = input(f"New author ({book['author']}): ") or book["author"]
                book["year"] = input(f"New year ({book['year']}): ") or book["year"]
                book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]
                book["read"] = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

                self.save_to_file()
                print("✏️ Book updated successfully!\n")
                return
        print("⚠️ Book not found.\n")

    def show_all_books(self):
        """Show all books saved in your collection."""
        if not self.book_list:
            print("📭 No books in your collection yet.\n")
            return

        print("📚 Your Book Collection:")
        for index, book in enumerate(self.book_list, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        print()

    def show_reading_progress(self):
        """Show how many books you've read out of your total collection."""
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        progress = (completed_books / total_books * 100) if total_books > 0 else 0

        print(f"📖 Total books: {total_books}")
        print(f"✅ Books read: {completed_books}")
        print(f"📊 Reading progress: {progress:.2f}%\n")

    def start_application(self):
        """Show the menu and let the user choose what to do."""
        while True:
            print("📘 Welcome to Book Collection Manager")
            print("1. Add a new book")
            print("2. Delete a book")
            print("3. Search for books")
            print("4. Update a book")
            print("5. Show all books")
            print("6. Show reading progress")
            print("7. Exit")
            user_choice = input("Choose an option (1–7): ")

            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                self.update_book()
            elif user_choice == "5":
                self.show_all_books()
            elif user_choice == "6":
                self.show_reading_progress()
            elif user_choice == "7":
                self.save_to_file()
                print("👋 Thanks for using Book Collection Manager. Goodbye!")
                break
            else:
                print("❗ Please enter a number from 1 to 7.\n")


if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.start_application()
