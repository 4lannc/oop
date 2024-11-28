from abc import ABC, abstractmethod

# Kelas abstract
class Kendaraan(ABC):

    @abstractmethod
    def bergerak(self):
        pass

    @abstractmethod
    def jenis_suara(self):
        pass

    def info(self):
        print("Saya adalah kendaraan.")

class Mobil(Kendaraan):
    def bergerak(self):
        print("Mobil bergerak dengan menggerakkan roda dengan mesin.")

    def jenis_suara(self):
        print("Suara mobil: Mesin yang berdengung.")

class Sepeda(Kendaraan):
    def bergerak(self):
        print("Sepeda bergerak dengan mengayuh pedal.")

    def jenis_suara(self):
        print("Suara sepeda: Bunyi roda di jalan.")

class Motor(Kendaraan):
    def bergerak(self):
        print("Motor bergerak dengan memutar roda dengan mesin.")

    def jenis_suara(self):
        print("Suara motor: Suara knalpot yang brong.")

mobil = Mobil()
mobil.info()
mobil.bergerak()
mobil.jenis_suara()

print()  

sepeda = Sepeda()
sepeda.info()
sepeda.bergerak()
sepeda.jenis_suara()

print() 

motor = Motor()
motor.info()
motor.bergerak()
motor.jenis_suara()