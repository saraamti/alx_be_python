# library_management.py

class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        """Initialize the book with title, author, and availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned."""
        self._is_checked_out = False

    def is_available(self):
        """Check if the book is available (i.e., not checked out)."""
        return not self._is_checked_out


class Library:
    """A class representing a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title if it is available."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    print(f"Checked out '{title}'.")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"'{title}' not found in the library.")

    def return_book(self, title):
        """Return a book to the library by its title."""
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    print(f"Returned '{title}'.")
                    return
                else:
                    print(f"'{title}' is already in the library.")
                    return
        print(f"'{title}' not found in the library.")

    def list_available_books(self):
        """List all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
