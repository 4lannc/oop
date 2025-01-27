from abc import ABC, abstractmethod

# Abstraksi class Hotel
class Hotel(ABC):
    @abstractmethod
    def pesan_kamar(self):
        pass

    @abstractmethod
    def tampilkan_informasi(self):
        pass

# Class Pelanggan
class Pelanggan:
    def __init__(self, nama, alamat, kamar, jumlah_bayar, klas):
        self.nama = nama
        self.alamat = alamat
        self.kamar = kamar
        self.jumlah_bayar = jumlah_bayar
        self.klas = klas

    def tampilkan_pelanggan(self):
        return (f"Nama: {self.nama}, Alamat: {self.alamat}, Kamar: {self.kamar}, "
                f"Jumlah Bayar: Rp{self.jumlah_bayar:,}, Kelas: {self.klas}")

# Manajemen Pelanggan dengan fitur CRUD
class ManajemenPelanggan:
    def __init__(self):
        self.pelanggan_list = []

    def create_pelanggan(self):
        nama = input("Masukkan nama pelanggan: ")
        alamat = input("Masukkan alamat pelanggan: ")
        kamar = input("Masukkan tipe kamar (Deluxe/VIP): ")
        jumlah_bayar = int(input("Masukkan jumlah bayar: "))
        klas = input("Masukkan kelas pelanggan (Reguler/VIP): ")
        pelanggan = Pelanggan(nama, alamat, kamar, jumlah_bayar, klas)
        self.pelanggan_list.append(pelanggan)
        print(f"Pelanggan {pelanggan.nama} berhasil ditambahkan.")

    def list_pelanggan(self):
        if not self.pelanggan_list:
            print("Tidak ada data pelanggan.")
        for pelanggan in self.pelanggan_list:
            print(pelanggan.tampilkan_pelanggan())

    def update_pelanggan(self):
        nama = input("Masukkan nama pelanggan yang akan diperbarui: ")
        for pelanggan in self.pelanggan_list:
            if pelanggan.nama == nama:
                pelanggan.nama = input("Masukkan nama baru: ") or pelanggan.nama
                pelanggan.alamat = input("Masukkan alamat baru: ") or pelanggan.alamat
                pelanggan.kamar = input("Masukkan tipe kamar baru: ") or pelanggan.kamar
                pelanggan.jumlah_bayar = int(input("Masukkan jumlah bayar baru: ") or pelanggan.jumlah_bayar)
                pelanggan.klas = input("Masukkan kelas baru: ") or pelanggan.klas
                print(f"Data pelanggan {nama} berhasil diperbarui.")
                return
        print(f"Pelanggan dengan nama {nama} tidak ditemukan.")

    def delete_pelanggan(self):
        nama = input("Masukkan nama pelanggan yang akan dihapus: ")
        for pelanggan in self.pelanggan_list:
            if pelanggan.nama == nama:
                self.pelanggan_list.remove(pelanggan)
                print(f"Pelanggan {nama} berhasil dihapus.")
                return
        print(f"Pelanggan dengan nama {nama} tidak ditemukan.")

# Sistem Login Manual
class LoginSystem:
    def __init__(self):
        self.users = {"admin": "admin123", "user": "user123", "manager": "manager123", "owner": "owner123", "staff": "staff123"}  # Contoh data login
        self.is_logged_in = False
        self.current_user = None

    def login(self):
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if username in self.users and self.users[username] == password:
            self.is_logged_in = True
            self.current_user = username
            print(f"Login berhasil. Selamat datang, {username}!")
        else:
            print("Username atau password salah.")

    def logout(self):
        self.is_logged_in = False
        self.current_user = None
        print("Logout berhasil.")

# Program Utama
if __name__ == "__main__":
    login_system = LoginSystem()
    manajemen = ManajemenPelanggan()

    while True:
        if not login_system.is_logged_in:
            print("\n=== Sistem Login ===")
            print("1. Login")
            print("2. Keluar")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                login_system.login()
            elif pilihan == "2":
                print("Terima kasih telah menggunakan sistem!")
                break
            else:
                print("Pilihan tidak valid.")
        else:
            print("\n=== Sistem Pemesanan Hotel ===")
            print("1. Tambah Pelanggan")
            print("2. Tampilkan Semua Pelanggan")
            print("3. Update Pelanggan")
            print("4. Hapus Pelanggan")
            print("5. Logout")

            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                manajemen.create_pelanggan()
            elif pilihan == "2":
                manajemen.list_pelanggan()
            elif pilihan == "3":
                manajemen.update_pelanggan()
            elif pilihan == "4":
                manajemen.delete_pelanggan()
            elif pilihan == "5":
                login_system.logout()
            else:
                print("Pilihan tidak valid.")
