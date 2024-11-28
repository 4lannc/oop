from abc import ABC, abstractmethod
from typing import List, Union

class MasakanNasi(ABC):
    def __init__(self, nama: str, porsi: int = 1):
        """
        Konstruktor dasar untuk masakan nasi
        
        :param nama: Nama hidangan nasi
        :param porsi: Jumlah porsi (default 1)
        """
        self.nama = nama
        self.porsi = porsi
        self.bahan_dasar = "Nasi putih"
        self.bumbu = []
    
    @abstractmethod
    def siapkan_bumbu(self):
        """
        Metode abstrak untuk menyiapkan bumbu
        Setiap jenis nasi harus mengimplementasikan metode ini
        """
        pass
    
    def hitung_kalori(self) -> int:
        """
        Metode default untuk menghitung kalori dasar
        
        :return: Jumlah kalori berdasarkan porsi
        """
        return 200 * self.porsi
    
    def tambah_bumbu(self, bumbu: Union[str, List[str]] = None):
        """
        Metode untuk menambah bumbu
        
        :param bumbu: Bumbu tambahan (bisa string tunggal atau list)
        """
        if bumbu is None:
            print("Tidak ada bumbu tambahan")
            return
        
        if isinstance(bumbu, str):
            self.bumbu.append(bumbu)
        elif isinstance(bumbu, list):
            self.bumbu.extend(bumbu)
    
    def __str__(self):
        """
        Representasi string dari masakan nasi
        
        :return: Deskripsi hidangan
        """
        return f"{self.nama} (Porsi: {self.porsi})"

class NasiGoreng(MasakanNasi):
    def __init__(self, porsi: int = 1, jenis: str = "Biasa"):
        """
        Konstruktor Nasi Goreng dengan jenis pilihan
        
        :param porsi: Jumlah porsi
        :param jenis: Jenis nasi goreng (default: Biasa)
        """
        super().__init__("Nasi Goreng " + jenis, porsi)
        self.jenis = jenis
    
    def siapkan_bumbu(self):
        """
        Implementasi metode siapkan_bumbu untuk Nasi Goreng
        """
        bumbu_dasar = ["Bawang Merah", "Bawang Putih", "Kecap"]
        self.bumbu.extend(bumbu_dasar)
        
        if self.jenis == "Seafood":
            self.bumbu.append("Udang")
        elif self.jenis == "Spesial":
            self.bumbu.extend(["Bakso", "Sosis"])
    
    def hitung_kalori(self) -> int:
        """
        Override metode hitung_kalori
        """
        kalori_dasar = super().hitung_kalori()
        tambahan_kalori = 50 * self.porsi  # Tambahan kalori karena digoreng
        return kalori_dasar + tambahan_kalori

class NasiGandul(MasakanNasi):
    def __init__(self, porsi: int = 1, lauk: str = None):
        """
        Konstruktor Nasi Gandul dengan pilihan lauk
        
        :param porsi: Jumlah porsi
        :param lauk: Lauk tambahan
        """
        super().__init__("Nasi Gandul", porsi)
        self.lauk = lauk
        self.bahan_dasar = "Nasi putih dengan kuah santan"
    
    def siapkan_bumbu(self):
        """
        Implementasi metode siapkan_bumbu untuk Nasi Gandul
        """
        bumbu_dasar = ["Garam", "Daun Salam", "Serai", "Santai"]
        self.bumbu.extend(bumbu_dasar)
    
    def tambah_lauk(self, lauk: Union[str, List[str]] = None):
        """
        Metode khusus untuk menambah lauk
        
        :param lauk: Lauk tambahan
        """
        if lauk is None:
            print("Tidak ada lauk tambahan")
            return
        
        if isinstance(lauk, str):
            self.lauk = lauk
        elif isinstance(lauk, list):
            self.lauk = ", ".join(lauk)

# Demonstrasi Polymorphisme
def sajikan_masakan(masakan: List[MasakanNasi]):
    """
    Fungsi untuk menyajikan berbagai masakan nasi
    
    :param masakan: Daftar masakan nasi
    """
    for hidangan in masakan:
        print(f"\n--- Menyajikan {hidangan.nama} ---")
        hidangan.siapkan_bumbu()
        print(f"Bumbu: {hidangan.bumbu}")
        print(f"Total Kalori: {hidangan.hitung_kalori()} kalori")

# Contoh penggunaan
def main():
    # Membuat berbagai hidangan nasi
    nasi_goreng_biasa = NasiGoreng()
    nasi_goreng_spesial = NasiGoreng(porsi=2, jenis="Spesial")
    nasi_gandul = NasiGandul(porsi=1)
    
    # Menambah bumbu dan lauk
    nasi_goreng_biasa.tambah_bumbu("Cabai")
    nasi_goreng_spesial.tambah_bumbu(["Daun Bawang", "Bawang Goreng"])
    nasi_gandul.tambah_lauk(["Daging Sapi", "Telur Rebus"])
    
    # Sajikan masakan dengan polymorphisme
    sajikan_masakan([nasi_goreng_biasa, nasi_goreng_spesial, nasi_gandul])

if __name__ == "__main__":
    main()
