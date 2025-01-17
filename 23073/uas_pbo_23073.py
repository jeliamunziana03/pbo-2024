
class Supermi:
    def __init__(self):
        # Daftar varian Supermi dan harga per bungkus
        self.menu = {
            "Supermi Original": 3000,
            "Supermi Rasa Ayam Bakar": 3500,
            "Supermi Rasa Soto": 4000,
            "Supermi Rasa Mie Goreng": 4000
        }

    def tampilkan_menu(self):
        """Menampilkan daftar menu Supermi"""
        print("---- Menu Supermi ----")
        for nomor, (nama, harga) in enumerate(self.menu.items(), start=1):
            print(f"{nomor}. {nama} - Rp {harga}")

    def hitung_total_harga(self, pilihan, jumlah_pesanan):
        """Menghitung total harga berdasarkan pilihan dan jumlah"""
        varian_pilihan = list(self.menu.keys())[int(pilihan) - 1]
        harga = self.menu[varian_pilihan]
        return harga * jumlah_pesanan
