# 📚 Class Book - Tugas PBO

Implementasi konsep OOP dasar (Class, Object, Encapsulation) dengan tema **Book**.

## 📊 UML Class Diagram

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