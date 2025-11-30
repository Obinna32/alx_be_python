class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

        def check_out(self):
            """Marks the book as checked out if available."""
            if not self._is_checked_out:
                self._is_checked_out = True
                return True
            return False

    def return_book(self):
        """Marks the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is not checked out."""
        return not self._is_checked_out
    

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out the book with the given title if available."""
        for book in self._books:
            if book.title == title:
                book.check_out()
                return

    def return_book(self, title):
        """Returns (makes available) the book with the given title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return

    def list_available_books(self):
        """Prints all books that are not checked out."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")