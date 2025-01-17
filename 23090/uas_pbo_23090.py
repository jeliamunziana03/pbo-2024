def hitung_pajak(gaji):
    if gaji <= 5000000:
        pajak = 0
    elif gaji <= 10000000:
        pajak = 0.05 * (gaji - 5000000)
    else:
        pajak = (0.05 * 5000000) + (0.1 * (gaji - 10000000))
    return pajak

def syafril():
    print("=== Penghitung Pajak Penghasilan ===")
    try:
        gaji = float(input("Masukkan gaji bulanan Anda (Rp): "))
        pajak = hitung_pajak(gaji)
        print(f"Pajak yang harus dibayar: Rp{pajak:.2f}")
    except ValueError:
        print("Harap masukkan angka yang valid.")
