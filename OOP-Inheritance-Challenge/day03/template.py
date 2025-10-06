class Pegawai:
    def __init__(self, nama, gaji_dasar):
        self.nama = nama
        self.gaji_dasar = gaji_dasar 
    def hitungGaji(self):
        return self.gaji_dasar

class Manager(Pegawai):
    def __init__(self, nama, gaji_dasar, tunjangan):
        super().__init__(nama, gaji_dasar)
        self.tunjangan = tunjangan

    def hitungGaji(self):
        gaji_dasar = super().hitungGaji()
        print(f"Gaji {self.nama} adalah {gaji_dasar + self.tunjangan}")

org1 = Manager("Andi", 3700000, 550000)
org1.hitungGaji()
if __name__ == "__main__":
    pass
