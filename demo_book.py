from book import Book

# Membuat 3 objek Book
book1 = Book("1984", "George Orwell", "978-0451524935", 1949, "Dystopian")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084", 1960, "Fiction")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", 1925, "Classic")

# Memanggil fungsi untuk book1
print("Book 1:")
print("String representation:", str(book1))
print("Info:", book1.get_info())
print("Published after 1950?", book1.is_published_after(1950))
print()

# Memanggil fungsi untuk book2
print("Book 2:")
print("String representation:", str(book2))
print("Info:", book2.get_info())
print("Published after 1950?", book2.is_published_after(1950))
print()

# Memanggil fungsi untuk book3
print("Book 3:")
print("String representation:", str(book3))
print("Info:", book3.get_info())
print("Published after 1950?", book3.is_published_after(1950))