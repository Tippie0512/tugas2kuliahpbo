import unittest
from book import Book

class TestBook(unittest.TestCase):
    """
    Unit tests for the Book class.
    """

    def setUp(self):
        """
        Set up test fixtures before each test method.
        """
        self.book = Book("1984", "George Orwell", "978-0451524935", 1949, "Dystopian")

    def test_init(self):
        """
        Test the initialization of a Book instance.
        """
        self.assertEqual(self.book.title, "1984")
        self.assertEqual(self.book.author, "George Orwell")
        self.assertEqual(self.book.isbn, "978-0451524935")
        self.assertEqual(self.book.year, 1949)
        self.assertEqual(self.book.genre, "Dystopian")

    def test_str(self):
        """
        Test the string representation of the book.
        """
        expected = "'1984' by George Orwell (ISBN: 978-0451524935, Year: 1949, Genre: Dystopian)"
        self.assertEqual(str(self.book), expected)

    def test_get_info(self):
        """
        Test the get_info method returns correct dictionary.
        """
        info = self.book.get_info()
        expected = {
            "title": "1984",
            "author": "George Orwell",
            "isbn": "978-0451524935",
            "year": 1949,
            "genre": "Dystopian"
        }
        self.assertEqual(info, expected)

    def test_is_published_after_true(self):
        """
        Test is_published_after returns True for a year before publication.
        """
        self.assertTrue(self.book.is_published_after(1940))

    def test_is_published_after_false(self):
        """
        Test is_published_after returns False for a year after publication.
        """
        self.assertFalse(self.book.is_published_after(1960))

    def test_is_published_after_equal(self):
        """
        Test is_published_after returns False for the same year.
        """
        self.assertFalse(self.book.is_published_after(1949))

if __name__ == '__main__':
    unittest.main()