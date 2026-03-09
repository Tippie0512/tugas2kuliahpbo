from book import Book

book1 = Book("1984", "George Orwell", "978-0451524935", 1949, "Dystopian")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084", 1960, "Fiction")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", 1925, "Classic")

print("Buku 1:")
print("Representasi string:", str(book1))
print("Info:", book1.get_info())
print("Diterbitkan setelah 1950?", book1.is_published_after(1950))
print()

print("Buku 2:")
print("Representasi string:", str(book2))
print("Info:", book2.get_info())
print("Diterbitkan setelah 1950?", book2.is_published_after(1950))
print()

print("Buku 3:")
print("Representasi string:", str(book3))
print("Info:", book3.get_info())
print("Diterbitkan setelah 1950?", book3.is_published_after(1950))