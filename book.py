class Book:
    def __init__(self, judul: str, penulis: str, isbn: str, tahun: int, jenis: str):
        self.judul = judul
        self.penulis = penulis
        self.isbn = isbn
        self.tahun = tahun
        self.jenis = jenis

    def __str__(self) -> str:
        return f"'{self.judul}' oleh {self.penulis} (ISBN: {self.isbn}, Tahun: {self.tahun}, Jenis: {self.jenis})"

    def get_info(self) -> dict:
        return {
            "judul": self.judul,
            "penulis": self.penulis,
            "isbn": self.isbn,
            "tahun": self.tahun,
            "jenis": self.jenis
        }

    def is_published_after(self, tahun: int) -> bool:
        return self.tahun > tahun