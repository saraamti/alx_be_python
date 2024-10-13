# library_system.py

class Book:
    """A base class representing a generic book."""
    
    def __init__(self, title, author):
        """Initialize the book with a title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """A class representing an electronic book."""
    
    def __init__(self, title, author, file_size):
        """Initialize the eBook with title, author, and file size in KB."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the eBook with file size."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """A class representing a printed book."""
    
    def __init__(self, title, author, page_count):
        """Initialize the print book with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the print book with page count."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """A class representing a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def list_books(self):
        """List all books in the library, printing their details."""
        for book in self.books:
            print(book)
