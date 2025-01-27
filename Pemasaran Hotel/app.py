from flask import Flask, render_template, request

app = Flask(__name__)

# Abstraksi
class Hotel:
    def pesan_kamar(self):
        pass

    def tampilkan_informasi(self):
        pass

# Enkapsulasi: Parent Class / induk class
class KamarHotel(Hotel):
    def __init__(self, tipe, harga):
        self.__tipe = tipe
        self.__harga = harga

    def get_tipe(self):
        return self.__tipe

    def get_harga(self):
        return self.__harga

    def pesan_kamar(self):
        return f"Kamar tipe '{self.__tipe}' berhasil dipesan."

    def tampilkan_informasi(self):
        return f"Tipe Kamar: {self.__tipe}, Harga: Rp{self.__harga:,}"

class KamarDeluxe(KamarHotel):
    def __init__(self, fasilitas):
        super().__init__("Deluxe", 500000)
        self.fasilitas = fasilitas

    def tampilkan_informasi(self):
        return f"{super().tampilkan_informasi()}, Fasilitas: {self.fasilitas}"

class KamarSuite(KamarHotel):
    def __init__(self, fasilitas):
        super().__init__("Suite", 1000000)
        self.fasilitas = fasilitas

    def tampilkan_informasi(self):
        return f"{super().tampilkan_informasi()}, Fasilitas: {self.fasilitas}"

# Objek Kamar
kamar1 = KamarDeluxe("Kolam Renang dan Sarapan Gratis 1 malam")
kamar2 = KamarSuite("Kolam Renang, Spa, Akses premium dan Eksklusif fasilitas hotel 1 malam")

@app.route("/")
def home():
    return render_template("index.html", kamar1=kamar1.tampilkan_informasi(), kamar2=kamar2.tampilkan_informasi())

@app.route("/pesan", methods=["POST"])
def pesan():
    tipe = request.form.get("tipe")
    if tipe == "Deluxe":
        pesan_kamar = kamar1.pesan_kamar()
    elif tipe == "Suite":
        pesan_kamar = kamar2.pesan_kamar()
    else:
        pesan_kamar = "Kamar tidak ditemukan."

    return render_template("pesan.html", pesan_kamar=pesan_kamar)

if __name__ == "__main__":
    app.run(debug=True)
