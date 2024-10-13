# book_class.py

class Book:
    """A class representing a book with title, author, and publication year."""

    def __init__(self, title, author, year):
        """Initialize a Book instance with title, author, and publication year."""
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.")

    def __del__(self):
        """Destructor that prints a message when a Book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a string representation in the format 'title by author, published in year'."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return an official string representation that can be used to recreate the instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
