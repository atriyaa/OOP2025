class LivingBeing:
    def __init__(self, jenis, habitat):
        self.jenis = jenis
        self.habitat = habitat
    def bernapas(self):
        print(f"{self.jenis} bisa bernapas")

class Animal(LivingBeing):
    def __init__(self, jenis, habitat, nama):
        super().__init__(jenis, habitat)
        self.nama = nama
    def bergerak(self):
        print(f"{self.nama} bisa bergerak ")

class Bird(Animal):
    def __init__(self, jenis, habitat, nama, warna):
        super().__init__(jenis, habitat, nama)
        self.warna = warna
    def terbang(self):
        print(f"Burung {self.nama} dengan warna {self.warna} bisa terbang")

lv = Bird("Burung", "Hutan", "LoveBird", "Hijau")
lv.terbang()
if __name__ == "__main__":
    pass