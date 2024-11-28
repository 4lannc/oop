# Kelas induk
class Hewan:
    def suara(self):
        return "Hewan mengeluarkan suara."

# Kelas turunan
class Kucing(Hewan):
    def suara(self):
        return "Miauww..!"

class Anjing(Hewan):
    def suara(self):
        return "Haug Haug..!"

# Contoh penggunaan
hewan1 = Hewan()
kucing = Kucing()
anjing = Anjing()

print(hewan1.suara())  # Output: Hewan mengeluarkan suara.
print(kucing.suara())  # Output: Meong!
print(anjing.suara())  # Output: Guk guk!
