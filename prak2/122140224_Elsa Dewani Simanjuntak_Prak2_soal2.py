class Book:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang

    def __del__(self):
        print(f"Buku '{self.judul}' karya {self.pengarang} telah dihapus dari perpustakaan.")

    @staticmethod
    def check_book(func):
        def wrapper(self):
            if self.judul and self.pengarang:
                print(f"Buku '{self.judul}' karya {self.pengarang} telah tersedia.")
                return func(self)
            else:
                print("Buku tidak tersedia.")
        return wrapper

    @check_book
    def display(self):
        print(f"Judul : {self.judul}")
        print(f"Pengarang: {self.pengarang}")


# Inisiasi objek buku
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

# Memanggil method display dengan decorator
book1.display()
print()

# Hapus referensi objek buku
del book2