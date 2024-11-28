class Laptop:
    def __init__(self, merk, ram, processor):
        """
        Constructor untuk menginisialisasi atribut Laptop.
        """
        self.merk = merk
        self.ram = ram  # dalam GB
        self.processor = processor
        print(f"Laptop {self.merk} dengan RAM {self.ram}GB dan prosesor {self.processor} dibuat.")

    def __del__(self):
        """
        Destructor untuk mencetak pesan ketika objek dihancurkan.
        """
        print(f"Laptop {self.merk} telah dihancurkan.")

# Contoh penggunaan
# Membuat objek Laptop
laptop1 = Laptop("Dell", 16, "Intel i7")
laptop2 = Laptop("HP", 8, "AMD Ryzen 5")

# Menghapus salah satu objek secara eksplisit
del laptop1

# Ketika skrip selesai, laptop2 akan dihapus otomatis oleh Python.
