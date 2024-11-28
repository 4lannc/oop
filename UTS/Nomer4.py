class AkunBank:
    def __init__(self, nomor_rekening, saldo):
        self.nomor_rekening = nomor_rekening
        self._saldo = saldo  # Atribut saldo dibuat privat

    # Getter untuk saldo
    def get_saldo(self):
        return self._saldo

    # Setter untuk saldo
    def set_saldo(self, nilai):
        if nilai < 0:
            print("Saldo tidak boleh bernilai negatif.")
        else:
            self._saldo = nilai

    # Metode untuk menambahkan saldo
    def tambah_saldo(self, jumlah):
        if jumlah > 0:
            self._saldo += jumlah
            print(f"Saldo berhasil ditambahkan. Saldo saat ini: {self._saldo}")
        else:
            print("Jumlah yang ditambahkan harus lebih dari 0.")

    # Metode untuk menarik saldo
    def tarik_saldo(self, jumlah):
        if 0 < jumlah <= self._saldo:
            self._saldo -= jumlah
            print(f"Saldo berhasil ditarik. Saldo saat ini: {self._saldo}")
        else:
            print("Jumlah tidak valid atau saldo tidak mencukupi.")

# Contoh penggunaan
akun = AkunBank("12345678", 1000.0)

# Mengakses dan mengubah saldo menggunakan getter dan setter
print("Saldo awal:", akun.get_saldo())  # Mengambil saldo
akun.set_saldo(1200.0)  # Mengubah saldo
print("Saldo setelah diubah:", akun.get_saldo())

# Menambahkan dan menarik saldo
akun.tambah_saldo(500.0)
akun.tarik_saldo(300.0)
