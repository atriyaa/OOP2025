# === Mulai kode di bawah ini ===

class Binatang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

class Mamalia(Binatang):
    def __init__(self, nama, umur, peliharaan=False):
        super().__init__(nama, umur)
        self.peliharaan = peliharaan
    
    def deskripsi(self):
        print(f"Nama = {self.nama}, Umur = {self.umur} tahun, Peliharaan = {self.peliharaan}")

kucing = Mamalia("Kucing", 4, True)
kucing.deskripsi()

# === Contoh penggunaan ===
if __name__ == "__main__":
    # TODO 3: Buat objek Mamalia dan tampilkan hasilnya
    pass
