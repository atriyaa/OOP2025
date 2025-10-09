class BankAccount:
    def __init__(self, namaPemilik, namaBank, saldo):
        self.namaPemilik = namaPemilik
        self.namaBank = namaBank
        self.saldo = saldo
    
    def deposit(self, jumlah):
        self.saldo += jumlah
        return self.saldo

class SavingsAccount(BankAccount):
    def __init__(self, namaPemilik, namaBank, saldo, bunga=0.02):
        super().__init__(namaPemilik, namaBank, saldo)
        self.bunga = bunga
    def tambahBunga(self):
        totalBunga = self.saldo * self.bunga
        self.saldo += totalBunga
        print(f"{self.namaPemilik} mendapatkan bunga sebesar : {totalBunga} %, saldo akhir : {self.saldo}")

class CheckingAccount(BankAccount):
    def __init__(self, namaPemilik, namaBank, saldo, biayaAdmin=3000):
        super().__init__(namaPemilik, namaBank, saldo)
        self.biayaAdmin = biayaAdmin
    def potongBiayaAdmin(self):
        self.saldo -= self.biayaAdmin
        print(f"{self.namaPemilik} dikenakan biaya admin sebesar : {self.biayaAdmin}. sisa saldo : {self.saldo}")

triya = SavingsAccount("Triya", "Mandiri", 1750000)
anis = CheckingAccount("Anis", "Mandiri", 2500000)
triya.deposit(500000)
triya.tambahBunga()
anis.deposit(1300000)
anis.potongBiayaAdmin()



if __name__ == "__main__":
    pass