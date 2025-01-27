from abc import ABC, abstractmethod

# Abstraksi
class Hotel(ABC): # Class Hotel method abstrak pesan_kamar dan tampilkan_informasi.
    @abstractmethod
    def pesan_kamar(self): #metod abstrak
        pass

    @abstractmethod
    def tampilkan_informasi(self): #metod
        pass

# Enkapsulasi: Parent Class / induk class
class KamarHotel(Hotel): # Parent Class/induk class
    def __init__(self, tipe, harga): #Atribut dua garis bawah (__) untuk menjadikannya privat.
        self.__tipe = tipe  # Enkapsulasi: Atribut privat diakses melalui metode getter get_tipe dan get_harga
        self.__harga = harga

    # Getter untuk akses atribut privat
    def get_tipe(self):# Metode getter
        return self.__tipe

    def get_harga(self): # Metode getter
        return self.__harga

    # Method untuk pemesanan kamar
    def pesan_kamar(self):
        print(f"Kamar tipe '{self.__tipe}' berhasil dipesan.")
    
    # Menampilkan detail kamar
    def tampilkan_informasi(self):
        print(f"Tipe Kamar: {self.__tipe}, Harga: Rp{self.__harga:,}")

# Child Class # Pewarisan (inharitance) Parent Class
class KamarDeluxe(KamarHotel): #child class yang mewarisi KamarHotel (parent class).
    def __init__(self, fasilitas):
        super().__init__("Deluxe", 500000) # Memanggil konstruktor parent (atribut saat objek dibuat)
        self.fasilitas = fasilitas  # Atribut tambahan untuk kelas anak
    
    # Override method tampilkan_informasi
    def tampilkan_informasi(self):
        super().tampilkan_informasi()
        print(f"Fasilitas Tambahan: {self.fasilitas}")

class KamarSuite(KamarHotel): #child class yang mewarisi KamarHotel (parent class).
    def __init__(self, fasilitas):
        super().__init__("Suite", 1000000)
        self.fasilitas = fasilitas

    # Override method tampilkan_informasi
    def tampilkan_informasi(self):
        super().tampilkan_informasi()
        print(f"Fasilitas Tambahan: {self.fasilitas}")

# Polimorfisme: Fungsi yang sama dengan perilaku berbeda, fungsi tampilkan_detail_kamar
def tampilkan_detail_kamar(kamar: Hotel):
    kamar.tampilkan_informasi()

# Program Utama
if __name__ == "__main__":
    print("=== Sistem Pemesanan Hotel JAVANESIA===")

    # Membuat objek dari kelas anak
    kamar1 = KamarDeluxe("Kolam Renang dan Sarapan Gratis 1 malam")
    kamar2 = KamarSuite("Kolam Renang, Spa, Akses premium dan Eksklusif fasilitas hotel 1 malam")

    # Menampilkan informasi kamar
    print("\nInformasi Kamar:")
    tampilkan_detail_kamar(kamar1)
    tampilkan_detail_kamar(kamar2)

    # Memesan kamar
    print("\nProses Pemesanan:")
    kamar1.pesan_kamar()
    kamar2.pesan_kamar()

    print("\nTerima kasih telah memesan di hotel JAVANESIA!")
# TEST CODE SISTEM PEMESANAN
# Informasi Kamar:
# Tipe Kamar: Deluxe, Harga: Rp500,000
# Fasilitas Tambahan: Kolam Renang dan Sarapan Gratis 1 malam
# Tipe Kamar: Suite, Harga: Rp1,000,000
# Fasilitas Tambahan: Kolam Renang, Spa, Akses premium dan Eksklusif fasilitas hotel 1 malam
# Proses Pemesanan:
# Kamar tipe 'Deluxe' berhasil dipesan.
# Kamar tipe 'Suite' berhasil dipesan.
# Terima kasih telah memesan di hotel JAVANESIA!