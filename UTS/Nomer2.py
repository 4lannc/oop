# Definisi kelas Mahasiswa
class Mahasiswa:
    def __init__(self, nama, nim, programStudi):
        self.nama = nama
        self.nim = nim
        self.programStudi = programStudi

    def tampilkanInfo(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Program Studi: {self.programStudi}")

# Input data dari pengguna
nama = input("Masukkan nama mahasiswa: ")
nim = input("Masukkan NIM mahasiswa: ")
programStudi = input("Masukkan program studi mahasiswa: ")

# Membuat objek Mahasiswa
mahasiswa1 = Mahasiswa(nama, nim, programStudi)

# Menampilkan informasi mahasiswa
print("\nInformasi Mahasiswa:")
mahasiswa1.tampilkanInfo()
