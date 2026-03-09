# Class Diagram - Book

```mermaid
classDiagram
    class Book {
        -String title
        -String author
        -String isbn
        -int year
        -String genre
        +__init__(title, author, isbn, year, genre)
        +__str__() String
        +get_info() Dict
        +is_published_after(year) Boolean
    }
    
    note for Book "Tugas PBO - Class Book"
