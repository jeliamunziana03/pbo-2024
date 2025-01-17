import math

def hitung_persegi():
    sisi = float(input("Masukkan panjang sisi persegi: "))
    luas = sisi ** 2
    keliling = 4 * sisi
    print(f"Luas Persegi: {luas}")
    print(f"Keliling Persegi: {keliling}")

def hitung_persegi_panjang():
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print(f"Luas Persegi Panjang: {luas}")
    print(f"Keliling Persegi Panjang: {keliling}")

def hitung_lingkaran():
    radius = float(input("Masukkan jari-jari lingkaran: "))
    luas = math.pi * radius ** 2
    keliling = 2 * math.pi * radius
    print(f"Luas Lingkaran: {luas:.2f}")
    print(f"Keliling Lingkaran: {keliling:.2f}")

def andry():
    while True:
        print("\n=== Program Hitung Geometri ===")
        print("1. Hitung Persegi")
        print("2. Hitung Persegi Panjang")
        print("3. Hitung Lingkaran")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4): ")
        
        if pilihan == "1":
            hitung_persegi()
        elif pilihan == "2":
            hitung_persegi_panjang()
        elif pilihan == "3":
            hitung_lingkaran()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
