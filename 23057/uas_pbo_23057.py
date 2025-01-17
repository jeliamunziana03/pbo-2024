class novi:
    def __init__(self,nama,kelas,jurusan,npm):
        self.nama=nama
        self.kelas=kelas
        self.jurusan=jurusan
        self.npm=npm
        
    def novi0(self):
        print(f"Nama\t\t:{self.nama} \nKelas\t\t:{self.kelas} \nJurusan\t\t:{self.jurusan} \nNpm\t\t:{self.npm}")

def novi1():
    n1=novi(f"{str(input("Masukan Nama Anda : "))}",f"{str(input("Masukan Kelas Anda : "))}",f"{str(input("Masukan Jurusan Anda : "))}",f"{str(input("Masukan Npm Anda : "))}")
    n1.novi0()

    return loop(str(input("Apkah Anda Ingin Mengulangi Program (Y/T): ")))

def loop(masukan):
    if masukan=="Y":
        return novi1()
    elif masukan=="y":
        return novi1()
    else:
        print("Terimakasih Telah Menggunakan Program Novi")

