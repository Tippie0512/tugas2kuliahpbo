class Book:
    """
    A simple Book class representing a book with basic attributes.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN of the book.
        year (int): The publication year of the book.
        genre (str): The genre of the book.
    """

    def __init__(self, title: str, author: str, isbn: str, year: int, genre: str):
        """
        Initializes a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            year (int): The publication year of the book.
            genre (str): The genre of the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.genre = genre

    def __str__(self) -> str:
        """
        Returns a string representation of the book.

        Returns:
            str: A formatted string with book details.
        """
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}, Year: {self.year}, Genre: {self.genre})"

    def get_info(self) -> dict:
        """
        Returns a dictionary with all book information.

        Returns:
            dict: A dictionary containing title, author, isbn, year, and genre.
        """
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "year": self.year,
            "genre": self.genre
        }

    def is_published_after(self, year: int) -> bool:
        """
        Checks if the book was published after a given year.

        Args:
            year (int): The year to compare against.

        Returns:
            bool: True if published after the given year, False otherwise.
        """
        return self.year > year