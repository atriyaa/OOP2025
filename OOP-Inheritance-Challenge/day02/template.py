class Kendaraan:
    def __init__(self, merk, kecepatan_maksimal):
        self.merk = merk
        self.kecepatan_maksimal = kecepatan_maksimal

class Mobil(Kendaraan):
    def __init__(self, merk, kecepatan_maksimal, jumlah_kursi):
        super().__init__(merk, kecepatan_maksimal)
        self.jumlah_kursi = jumlah_kursi
    def berjalan(self):
        print(f"mobil {self.merk} dengan jumlah kursi {self.jumlah_kursi} bisa berjalan dengan kecepatan maksimal {self.kecepatan_maksimal} km/jam")

class Motor(Kendaraan):
    def __init__(self, merk, kecepatan_maksimal, tipe_motor):
        super().__init__(merk, kecepatan_maksimal)
        self.tipe_motor = tipe_motor
    def berjalan(self):
        print(f"motor {self.merk} dengan tipe {self.tipe_motor} bisa berjalan dengan kecepatan maksimal {self.kecepatan_maksimal} km/jam")

mtr1 = Motor("Honda", 150, "Matic")
mtr1.berjalan()
mbl1 = Mobil("Toyota", 180, 8)
mbl1.berjalan()

if __name__ == "__main__":
    pass
