# Tugas OOP: Class Book

## Deskripsi Tugas
Buatlah sebuah video dengan topik:
- Merancang class sederhana
- Membuat UML (class diagram)
- Memastikan kode testable (unit testing)

Penjelasan yang ada pada video terdiri dari:
- Merancang menggunakan Python.
- Menjelaskan konsep OOP.
- Mendokumentasikan desain class menggunakan UML.
- Mengimplementasikan class.
- Menjelaskan kode yang dibuat melalui unit testing.

Tema yang dipilih: **Book (Buku)**

## Konsep OOP yang Digunakan
- **Class**: Blueprint untuk membuat objek. Di sini, `Book` adalah class yang merepresentasikan buku.
- **Object**: Instance dari class. Misalnya, buku "1984" adalah objek dari class Book.
- **Attributes**: Properti dari class, seperti title, author, dll.
- **Methods**: Fungsi yang dimiliki class, seperti `__init__`, `__str__`, dll.
- **Encapsulation**: Data disembunyikan dan diakses melalui metode.

## Desain Class Book
Class Book memiliki atribut:
- `title` (str): Judul buku
- `author` (str): Penulis buku
- `isbn` (str): ISBN buku
- `year` (int): Tahun terbit
- `genre` (str): Genre buku

Metode:
- `__init__`: Konstruktor untuk inisialisasi objek.
- `__str__`: Mengembalikan representasi string dari buku.
- `get_info`: Mengembalikan dictionary dengan semua informasi buku.
- `is_published_after`: Mengecek apakah buku diterbitkan setelah tahun tertentu.

## UML Class Diagram
```
classDiagram
    class Book {
        - title: str
        - author: str
        - isbn: str
        - year: int
        - genre: str
        + __init__(title: str, author: str, isbn: str, year: int, genre: str)
        + __str__(): str
        + get_info(): dict
        + is_published_after(year: int): bool
    }
```

## Implementasi Kode
Kode diimplementasikan dalam `book.py`. Lihat file tersebut untuk detail implementasi.

## Unit Testing
Unit testing dilakukan menggunakan `unittest` dalam `test_book.py`. Test mencakup:
- Inisialisasi objek
- Representasi string
- Metode `get_info`
- Metode `is_published_after`

Semua test berhasil: 6 tests passed.

## Cara Menjalankan
1. Pastikan Python terinstall.
2. Jalankan test: `python -m unittest test_book.py`
3. Untuk menggunakan class: `from book import Book; b = Book("Title", "Author", "ISBN", 2023, "Genre")`

## Kesimpulan
Implementasi ini menunjukkan konsep OOP dasar dengan class Book yang sederhana, didokumentasikan dengan UML, dan diuji dengan unit testing untuk memastikan kebenaran kode.