import os
import sys
import colorama
from random import randint
from colorama import init, Fore, Back, Style
colorama.init(autoreset=True)

# essential for Windows environment
init()
# all available foreground colors
FORES = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW,
         Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
# all available background colors
BACKS = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW,
         Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]
# brightness values
BRIGHTNESS = [Style.DIM, Style.NORMAL, Style.BRIGHT]

# -------------- DEF FUNGSI ------------


def lanjutan():
    os.system('cls')
    print(Fore.RED+Style.BRIGHT+"Silahkan Isi Data Kembali\n")
    print("Masukkan Data Pasien Dengan Baik Dan Benar")
    print("-----------------------------------")
    nama_pasien = str(input("Masukkan Nama : "))
    jenis_kelamin = str(input("Jenis Kelamin : "))
    umur = int(input("Umur          : "))
    telp = int(input("Nomor Telpon  : "))


def logout():
    os.system('cls')
    print(Style.BRIGHT+Fore.RED+"Anda Telah Logout Dari Program")
    print("------------------------------")
    print("Silahkan Jalankan Ulang Program untuk Menjalankan Program Kembali.")
    sys.exit()

# -------------------------- LOGIN ------------------------------
print(Style.BRIGHT+Fore.GREEN+"\nAdministrasi Puskesmas Sungkai")
print("------------------------------\n")
print("Masuk Dengan Username dan kata sandi Anda")

while True:
    Username = str(input(Style.BRIGHT+Fore.CYAN+"Username   : "))
    Kata_sandi = str(input("Kata Sandi : "))
    if Username.upper() == ("KEVIN"):
        if Kata_sandi.upper() == ("KEVIN123"):
            print(Fore.BLUE+"Login Berhasil")
            break
        else:
            print(Fore.RED+"Username dan Kata Sandi Tidak Sesuai\n")

    elif Username.upper() == ("FAJAR"):
        if Kata_sandi.upper() == ("FAJAR123"):
            print(Fore.BLUE+"Login Berhasil")
            break
        else:
            print(Fore.RED+"Username dan Kata Sandi Tidak Sesuai\n")

    elif Username.upper() == ("IQBAL"):
        if Kata_sandi.upper() == ("IQBAL123"):
            print(Fore.BLUE+"Login Berhasil")
            break
        else:
            print(Fore.RED+"Username dan Kata Sandi Tidak Sesuai\n")

    elif Username.upper() == ("GADING"):
        if Kata_sandi.upper() == ("GADING123"):
            print(Fore.BLUE+"Login Berhasil")
            break
        else:
            print(Fore.RED+"Username dan Kata Sandi Tidak Sesuai\n")

    elif Username.upper() == ("MELANI"):
        if Kata_sandi.upper() == ("MELANI123"):
            print(Fore.BLUE+"Login Berhasil")
            break
        else:
            print(Fore.RED+"Username dan Kata Sandi Tidak Sesuai\n")

    elif Username.upper() == ("DESTI"):
        if Kata_sandi.upper() == ("DESTI123"):
            print(Fore.BLUE+"Login Berhasil")
            break
        else:
            print(Fore.RED+"Username dan Kata Sandi Tidak Sesuai\n")
    else:
        print(Fore.RED+"Username dan Kata Sandi Tidak Sesuai\n")


while True:
    lanjut = str(input("\nApakah Anda Ingin Melanjutkan [Ya/Tidak]: "))
    if lanjut.upper() == ("YA"):
        break
    elif lanjut.upper() == ("TIDAK"):
        logout()
        continue
    else:
        print("Kalimat Salah")

# ----------------- Data Pasien -------------------
os.system('cls')
print(Style.BRIGHT+Fore.GREEN+"\nMasukkan Data Pasien Dengan Baik Dan Benar")
print("------------------------------------------\n")
nama_pasien = str(input("Masukkan Nama : "))
jenis_kelamin = str(input("Jenis Kelamin : "))
umur = int(input("Umur          : "))
telp = int(input("Nomor Telpon  : "))

while True:
    lanjut = str(input("\nApakah Data Yang Anda Isi Sudah Benar [Ya/Tidak]: "))
    if lanjut.upper() == ("YA"):
        break
    elif lanjut.upper() == ("TIDAK"):
        lanjutan()
    else:
        print("Kalimat Salah")

# ------------------------ Daftar Menu ----------------------------
Pilihan = {
    1: {"nama": "Medical Check-Up", "Harga": 100000},
    2: {"nama": "Pelayanan Konsultasi Terpadu", "Harga": 100000},
    3: {"nama": "Pelayanan Umum", "Harga": 150000},
    4: {"nama": "Pelayanan Kesehatan Gigi", "Harga": 200000},
    5: {"nama": "Pelayanan Kesehatan Ibu Anak & KB", "Harga": 500000},
    6: {"nama": "Pelayanan Gizi", "Harga": 300000},
    7: {"nama": "Pelayanan Pencegahan Penyakit", "Harga": 800000},
    8: {"nama": "Pelayanan Kesehatan Mata", "Harga": 900000},
    9: {"nama": "Pelayanan Kefarmasian", "Harga": 200000},
}


# ------------------------- Data Transaksi --------------------------
os.system('cls')
print('\n------------- MENU PELAYANAN PUSKESMAS SUNGKAI -------------')
print('------------------------------------------------------------')
print('Kode     Pelayanan                                 Harga    ')
print('------------------------------------------------------------')
for kode, jenis in Pilihan.items():
    print(f"{kode: <8} {jenis['nama']: <41} Rp.{jenis['Harga']: >5}")
print('------------------------------------------------------------')

print(Fore.GREEN+Style.DIM+"\nIsi Data Pelayanan Sesuai Yang Diharapkan Pasien\n")
banyakpelayanan = int(input("Banyak Pelayanan: "))
pilihan = []
for i in range(5):
    bil = randint(0, 100)
for i in range(banyakpelayanan):
    print('\nPelayanan ke - ', i+1)
    while True:
        kodepelayanan = int(input("Pilih kode pelayanan[1 - 9]: "))
        if kodepelayanan in Pilihan:
            break
        else:
            print("Kalimat Salah")
    pilihan.append({'kode': kodepelayanan})

# -------------------- Pembayaran ----------------------
total=0
for i, pilih in enumerate(pilihan):
    jenispelayanan = Pilihan[pilih['kode']]['nama']
    nominaltransaksi = Pilihan[pilih['kode']]['Harga']
    total += nominaltransaksi
    print(f"\nPelayanan Ke-{i+1: <5}")
    print(f"Jenis Pelayanan: {jenispelayanan: <5}")
    print(f"Harga Pelayanan: Rp.{nominaltransaksi: >5}\n")
jumlahbayar = total
print(f'Total Transaksi: Rp.{jumlahbayar: >5}')
while True:
    pembayaran = int(input("Masukkan Nominal Pembayaran: "))
    kembalian = pembayaran - total
    print("Kembalian: ",kembalian)
    if pembayaran < total:
        print(Fore.RED+Style.BRIGHT+"\nPembayaran Anda Kurang")
    else:
        print("Pembayaran Lunas")
        break


while True:
    lanjut = str(input("\nApakah Anda Ingin Cetak Bukti Transaksi [Ya/Tidak]: "))
    if lanjut.upper() == ("YA"):
        break
    elif lanjut.upper() == ("TIDAK"):
        ("Terima Kasih Telah Memilih Menu Pelayanan Kami")
        sys.exit()
    else:
        print("Kalimat Salah")

print("\n----------------------------------------------------------------")
print("""                       Rincian Transaksi                        
                       Puskesmas Sungkai""")
print("----------------------------------------------------------------")
print("Nama Pasien:", nama_pasien)
print("Nomor Antrian:", bil)
print('----------------------------------------------------------------')
print('No.   Jenis Pelayanan                          Nominal Transaksi')
print('----------------------------------------------------------------')
total = 0
for i, pilih in enumerate(pilihan):
    jenispelayanan = Pilihan[pilih['kode']]['nama']
    nominaltransaksi = Pilihan[pilih['kode']]['Harga']
    total += nominaltransaksi
    print(f"{i+1: <5} {jenispelayanan: <48} Rp.{nominaltransaksi: >5}")
print('----------------------------------------------------------------')
jumlahbayar = total
print(f'Total Transaksi.                                       Rp.{jumlahbayar: >5}')
print(f'Total Pembayaran.                                      Rp.{pembayaran: >4}')
print(f'Total Kembalian.                                       Rp.{kembalian: >5}')
print('----------------------------------------------------------------')
print('   ~ Semoga Hari Anda Menyenangkan dan Semoga Lekas Sembuh ~    ')

