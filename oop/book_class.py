# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize the Book object."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to print a message when the Book object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation of the Book object."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation of the Book object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
