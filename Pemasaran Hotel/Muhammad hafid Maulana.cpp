#include <iostream>
#include <string>
#include <memory> // Untuk smart pointer
using namespace std;

// Abstract Class (Abstraction)
class Hotel {
public:
    virtual void pesanKamar() = 0; // Pure virtual method
    virtual void tampilkanInformasi() = 0; // Pure virtual method
    virtual ~Hotel() {} // Virtual destructor
};

// Parent Class (Encapsulation and Inheritance)
class KamarHotel : public Hotel {
private:
    string tipe;
    int harga;

protected:
    void setTipe(const string &t) { tipe = t; }
    void setHarga(int h) { harga = h; }

public:
    KamarHotel(const string &t, int h) : tipe(t), harga(h) {}

    string getTipe() const { return tipe; }
    int getHarga() const { return harga; }

    void tampilkanInformasi() override {
        cout << "Tipe Kamar: " << tipe << endl;
        cout << "Harga: Rp " << harga << endl;
    }

    virtual void pesanKamar() override {
        cout << "Kamar " << tipe << " berhasil dipesan dengan harga Rp " << harga << endl;
    }

    virtual ~KamarHotel() {}
};

// Child Class: KamarDeluxe (Inheritance and Polymorphism)
class KamarDeluxe : public KamarHotel {
private:
    string fasilitas;

public:
    KamarDeluxe(const string &f) : KamarHotel("Deluxe", 500000), fasilitas(f) {}

    void tampilkanInformasi() override {
        KamarHotel::tampilkanInformasi(); // Panggil method parent
        cout << "Fasilitas Tambahan: " << fasilitas << endl;
    }

    void pesanKamar() override {
        cout << "Kamar Deluxe dengan fasilitas " << fasilitas << " berhasil dipesan." << endl;
    }

    ~KamarDeluxe() {}
};

// Child Class: KamarSuite (Inheritance and Polymorphism)
class KamarSuite : public KamarHotel {
private:
    string fasilitas;

public:
    KamarSuite(const string &f) : KamarHotel("Suite", 1000000), fasilitas(f) {}

    void tampilkanInformasi() override {
        KamarHotel::tampilkanInformasi();
        cout << "Fasilitas Tambahan: " << fasilitas << endl;
    }

    void pesanKamar() override {
        cout << "Kamar Suite dengan fasilitas " << fasilitas << " berhasil dipesan." << endl;
    }

    ~KamarSuite() {}
};

// Fungsi untuk menampilkan detail kamar (Polymorphism)
void tampilkanDetailKamar(shared_ptr<Hotel> kamar) {
    kamar->tampilkanInformasi();
}

int main() {
    // Membuat objek (Object)
    shared_ptr<Hotel> kamar1 = make_shared<KamarDeluxe>("Kolam Renang dan Sarapan Gratis");
    shared_ptr<Hotel> kamar2 = make_shared<KamarSuite>("Kolam Renang, Spa, dan Akses Lounge Eksklusif");

    cout << "--- Informasi Kamar ---\n" << endl;
    tampilkanDetailKamar(kamar1);
    cout << endl;
    tampilkanDetailKamar(kamar2);
    cout << endl;

    cout << "--- Proses Pemesanan ---\n" << endl;
    kamar1->pesanKamar();
    kamar2->pesanKamar();

    return 0;
}
