import unittest
from book import Book

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book("1984", "George Orwell", "978-0451524935", 1949, "Dystopian")

    def test_init(self):
        self.assertEqual(self.book.judul, "1984")
        self.assertEqual(self.book.penulis, "George Orwell")
        self.assertEqual(self.book.isbn, "978-0451524935")
        self.assertEqual(self.book.tahun, 1949)
        self.assertEqual(self.book.jenis, "Dystopian")

    def test_str(self):
        expected = "'1984' oleh George Orwell (ISBN: 978-0451524935, Tahun: 1949, Jenis: Dystopian)"
        self.assertEqual(str(self.book), expected)

    def test_get_info(self):
        info = self.book.get_info()
        expected = {
            "judul": "1984",
            "penulis": "George Orwell",
            "isbn": "978-0451524935",
            "tahun": 1949,
            "jenis": "Dystopian"
        }
        self.assertEqual(info, expected)

    def test_is_published_after_true(self):
        self.assertTrue(self.book.is_published_after(1940))

    def test_is_published_after_false(self):
        self.assertFalse(self.book.is_published_after(1960))

    def test_is_published_after_equal(self):
        self.assertFalse(self.book.is_published_after(1949))

if __name__ == '__main__':
    unittest.main()