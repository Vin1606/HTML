# Program Aplikasi Apotek
import os
import sys
import colorama
import queue
from datetime import datetime
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

# -------------------- Array --------------------

class array:
    @staticmethod
    def manggil_array():
        os.system('cls')
        print(Fore.YELLOW+ Style.BRIGHT+"\nData Karyawan")
        print(Fore.GREEN+"----------------------------------------------------------------------------")
        print(Style.BRIGHT+'Nama Karyawan        Alamat         Nomor Telpon     Username     Password')
        print(Fore.GREEN+"----------------------------------------------------------------------------")

        nama_karyawan=["Mutiara Aisyah", "Muhammad Rico", "Rizky Fajar", "Cornelius Kevin"]
        alamat=["Jakarta", "Cibitung", "Bekasi", "Tambun"]
        telpon=["08961234", "08965678", "08961112", "08961314"]
        username=["mutiara", "rico", "rizky", "kevin"]
        password=["mutiara123", "rico123", "rizky123", "kevin123"]
        for i in range(len(nama_karyawan)):
            print(f'{nama_karyawan[i]:<20} {alamat[i]:<10} {telpon[i]:^20} {username[i]:<10} {password[i]:>12}')
        print(Fore.GREEN+"----------------------------------------------------------------------------\n")


    def login():
        print("\nProgram Apotek Sejahtera")
        print("------------------------")
        print("Silahkan Login Terlebih Dahulu")
        while True:
            input_username = str(input("Username : "))
            input_password = str(input("Password : "))
            if input_username.upper() == ("KEVIN"):
                if input_password.upper() == ("KEVIN123"):
                    print(Fore.BLUE+"Login Berhasil")
                    break
                else:
                    print(Fore.RED+"Username dan Kata Sandi Tidak Sesuai\n")

            elif input_username.upper() == ("RIZKY"):
                if input_password.upper() == ("RIZKY123"):
                    print(Fore.BLUE+"Login Berhasil")
                    break
                else:
                    print(Fore.RED+"Username dan Kata Sandi Tidak Sesuai\n")

            elif input_username.upper() == ("RICO"):
                if input_password.upper() == ("RICO123"):
                    print(Fore.BLUE+"Login Berhasil")
                    break
                else:
                    print(Fore.RED+"Username dan Kata Sandi Tidak Sesuai\n")

            elif input_username.upper() == ("MUTIARA"):
                if input_password.upper() == ("MUTIARA123"):
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
                print("Terima Kasih Telah Menggunakan Program Ini")
                sys.exit()
            else:
                print("Kalimat Salah")




# Node

class Node:
    def __init__(self, nama_obat, stok):
        self.nama_obat = nama_obat
        self.stok = stok
        self.next_node = None

# -------------------- Stack --------------------
        
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        print("\nHistori Pembelian Obat")
        print(f"{Fore.CYAN}{'-' * 85}")
        print(f"|{'Nama Customer':^20}|{'Nama Obat':^20}|{'Jumlah':^10}|{'Tanggal Pembelian':^30}|")
        print(f"{Fore.CYAN}{'-' * 85}")
        for i, (customer, obat, jumlah, tanggal_pembelian) in enumerate(reversed(self.items)):
            tanggal_pembelian_str = tanggal_pembelian.strftime("%Y-%m-%d %H:%M:%S")
            print(f"|{customer:^20}|{obat:^20}|{jumlah:^10}|{tanggal_pembelian_str:^30}|")
        print(f"{Fore.CYAN}{'-' * 85}")
    
histori_pembelian = Stack()

# -------------------- Linked List --------------------

class LinkedList:
    def __init__(self):
        self.start_node = None
        self.length = 0

    def is_empty(self):
        return self.start_node is None
    
    def nambah(self, nama_obat, stok):
        new_node = Node(nama_obat, stok)
        if self.is_empty():
            self.start_node = new_node
        else:
            last_node = self.start_node
            while last_node.next_node:
                last_node = last_node.next_node
            last_node.next_node = new_node
        self.length += 1  
    
    def _len_(self):
        return self.length

    def display_reduced(self):
        if self.is_empty():
            print("Tidak ada obat di stok.")
        else:
            print("\nStok Obat yang Sudah Berkurang")
            print(f"{Fore.CYAN}{'-' * 35}")
            print(f"{'Nama Obat':<20}{'Stok Obat':>5}")
            print(f"{Fore.CYAN}{'-' * 35}")
            current_node = self.start_node
            while current_node:
                if current_node.stok < 10:  # asumsikan jumlah awal adalah 20
                    print(f"{current_node.nama_obat:<20}{current_node.stok:>5}")
                current_node = current_node.next_node
            print(f"{Fore.CYAN}{'-' * 35}")

    def beli_obat(self, nama_obat, nama_customer, jumlah):
        current_node = self.start_node
        while current_node is not None:
            if current_node.nama_obat == nama_obat:
                if current_node.stok >= jumlah:
                    current_node.stok -= jumlah
                    tanggal_pembelian = datetime.now()  # ini harus menjadi objek datetime
                    print("\nCatatan Transaksi")
                    print("-------------------")
                    print(f"Keterangan: {nama_customer} membeli obat {nama_obat} sebanyak {jumlah} piece")
                    print(f"Sisa stok obat: {current_node.stok}")
                    histori_pembelian.push((nama_customer, nama_obat, jumlah, tanggal_pembelian))  # tambahkan tuple ke dalam stack histori_pembelian
                    return True
                else:
                    print(f"Stok obat {nama_obat} tidak cukup.")
                    return False
            current_node = current_node.next_node
        print(f"Obat {nama_obat} tidak ditemukan.")
    
    def make_new_list(self, jumlahdata):
        for i in range(jumlahdata):
            print(Fore.GREEN+"-----------------------------")
            nama_obat=input(str("Masukkan Nama Obat: "))
            stok=int(input("Masukkan Stok Obat: "))
            print(Fore.GREEN+"-----------------------------")
            self.nambah(nama_obat, stok)

    def tambah_stok(self, nama_obat, jumlah):
        current_node = self.start_node
        while current_node is not None:
            if current_node.nama_obat == nama_obat:
                current_node.stok += jumlah
                print(f"Stok obat {nama_obat} telah ditambah. Stok sekarang: {current_node.stok}")
                return True
            current_node = current_node.next_node
        print(f"Obat {nama_obat} tidak ditemukan.")
        return False
    
    def tambah_obat(self, nama_obat, stok):
        new_obat = Node(nama_obat, stok)
        if self.is_empty():
            self.start_node = new_obat
        else:
            last_node = self.start_node
            while last_node.next_node:
                last_node = last_node.next_node
            last_node.next_node = new_obat
        print(f"Obat baru {nama_obat} dengan stok {stok} telah ditambahkan.")
        
    def display(self):
        if self.is_empty():
            print("Tidak ada obat di stok.")
        else:
            print("\nDaftar Obat")
            print(f"{Fore.CYAN}{'-' * 34}")
            print(f"|{'Nama Obat':^20}|{'Stok Obat':^11}|")
            print(f"{Fore.CYAN}{'-' * 34}")
            current_node = self.start_node
            while current_node:
                print(f"|{current_node.nama_obat:<20}|{current_node.stok:^10} |")
                current_node = current_node.next_node
            print(f"{Fore.CYAN}{'-' * 34}")

# -------------------- Queue --------------------
            
class myQueue:
    def __init__(self):
        self.items = queue.Queue()
        self.linked_list = LinkedList()  # inisialisasi linked_list di sini
        self.linked_list.nambah("Paracetamol", 20)
        self.linked_list.nambah("Metylphenidate", 20)
        self.linked_list.nambah("Sukralfat", 20)
        self.linked_list.nambah("Fibrinogen", 20)
        self.linked_list.nambah("Calcium Carbonate", 20)

    def antrian_kosong(self):
        return self.items.empty()
    
    def antrian_masuk(self, item):
        self.items.put(item)

    def antrian_keluar(self):
        if not self.items.empty():
            return self.items.get()
        else:
            print("Data Antrian Kosong")
    
    def size(self):
        return self.items.qsize()

    def main_menu(self):
        pilih = "y"
        while(pilih == "y"):
            os.system('cls')
            print("\n--------------------------------------------------")
            print("|",Fore.GREEN+"Selamat Datang Di Apotek Sejahtera".center(46),"|")
            print("--------------------------------------------------")
            print("\n==============================================")
            print('Program Pembelian Obat'.center(45))
            print("==============================================")
            print(" 1. Daftar")
            print(" 2. Bayar")
            print(" 3. Check Antrian")
            print(" 4. Banyak Antrian")
            print(" 5. Check Data Obat Terkini")
            print(" 6. Check Data Obat Yang Stoknya Mau Habis")
            print(" 7. Menambahkan Stok Produk Obat Awal")
            print(" 8. Menambahkan Stok Dan Produk Obat Baru")
            print(" 9. Histori Pembelian Customer")
            print("10. Kembali Ke Menu Login")
            print("==============================================")
            pilihan = str(input("\nMasukan Pilihan Anda: "))

            if pilihan == "1":
                os.system('cls')
                print("\nForm Pendaftaran")
                print("----------------")
                obj = str(input("Masukkan Nama Customer : "))
                obat = str(input("Masukkan Nama Obat : "))
                jumlah = int(input("Masukkan jumlah obat yang ingin dibeli: "))
                self.antrian_masuk(obj)
                if self.linked_list.beli_obat(obat, obj, jumlah):
                    print(Fore.GREEN+"\nPendaftaran Berhasil")  # kurangi stok obat
                    print("\n--------------------------------------")
                    print(Fore.RED+"Tekan Enter Untuk Kembali Ke Menu Awal")
                    print("--------------------------------------")
                else:
                    print("\nTransaksi Gagal")
                    print("============================")
                    print("Silahkan Mulai Ulang Program")
                    sys.exit()
                x = input("")
                    
            elif pilihan == "2":
                os.system('cls')
                print("Silahkan Masukkan Data Pembayaran")
                print("---------------------------------")

                harga = 20000
                ppn = round(harga) * 0.10
                total_bayar = round(harga) * round(jumlah) + round(ppn)

                print("Total Yang Harus Dibayar :",total_bayar)
                bayar = int(input("Masukkan Nominal Uang Pembayaran : "))
                kembalian = round(bayar) - round(total_bayar)

                print("\nRincian Transaksi")
                print("-----------------")
                print("Harga Satuan : Rp.",harga)
                print("PPN 10% : Rp.",ppn)
                print("Total Harga : Rp.",total_bayar)
                print("Yang Dibayarkan :",bayar)
                print("Kembalian :",kembalian)

                temp = self.antrian_keluar()
                if temp != (obj,"Telah Melakukan Pembelian"):
                    print("\nCustomer bernama",temp,"Telah Selesai Melakukan Transaksi Pembelian")
                    print("\n--------------------------------------")
                    print(Fore.RED+"Tekan Enter Untuk Kembali Ke Menu Awal")
                    print("--------------------------------------")
                    x = input("")
                else:
                    print("Tidak Ada Transaksi Berlangsung")

            elif pilihan == "3":
                os.system('cls')
                print("Apakah Antrian Customer Sudah Kosong:",self.antrian_kosong())
                print("\n--------------------------------------")
                print(Fore.RED+"Tekan Enter Untuk Kembali Ke Menu Awal")
                print("--------------------------------------")
                x = input("")

            elif pilihan == "4":
                os.system('cls')
                if self.size() > 0:
                    print("Antrian Obat: ",str(self.size()),"orang")
                    for i in list(self.items.queue):
                        print('Nama Customer dalam Antrian: ', i)
                    print("\n--------------------------------------")
                    print(Fore.RED+"Tekan Enter Untuk Kembali Ke Menu Awal")
                    print("--------------------------------------")
                else:
                    print("Tidak ada antrian.")
                    print("\n--------------------------------------")
                    print(Fore.RED+"Tekan Enter Untuk Kembali Ke Menu Awal")
                    print("--------------------------------------")
                x = input("")
            
            elif pilihan == "5":
                os.system('cls')
                # cetak semua obat di dalam stack histori_pembelian
                self.linked_list.display()   
                print("\n--------------------------------------")
                print(Fore.RED+"Tekan Enter Untuk Kembali Ke Menu Awal")
                print("--------------------------------------")
                x = input("")

            elif pilihan == "6":  # atau nomor lain yang belum digunakan
                os.system('cls')
                self.linked_list.display_reduced()
                print("\n--------------------------------------")
                print(Fore.RED+"Tekan Enter Untuk Kembali Ke Menu Awal")
                print("--------------------------------------")
                x = input("")

            elif pilihan == "7":  # atau nomor lain yang belum digunakan
                os.system('cls')
                nama_obat = input("Masukkan nama obat yang ingin ditambah stoknya: ")
                jumlah = int(input("Masukkan jumlah yang ingin ditambahkan: "))
                self.linked_list.tambah_stok(nama_obat, jumlah)
                self.linked_list.display()
                print("\n--------------------------------------")
                print(Fore.RED+"Tekan Enter Untuk Kembali Ke Menu Awal")
                print("--------------------------------------")
                x = input("")

            elif pilihan == "8":  # atau nomor lain yang belum digunakan
                os.system('cls')
                nama_obat = input("Masukkan nama obat baru: ")
                stok = int(input("Masukkan stok obat baru: "))
                self.linked_list.tambah_obat(nama_obat, stok)
                print("\n--------------------------------------")
                print(Fore.RED+"Tekan Enter Untuk Kembali Ke Menu Awal")
                print("--------------------------------------")
                x = input("")

            elif pilihan == "9":  # atau nomor lain yang belum digunakan
                os.system('cls')
                histori_pembelian.display()
                print("\n--------------------------------------")
                print(Fore.RED+"Tekan Enter Untuk Kembali Ke Menu Awal")
                print("--------------------------------------")
                x = input("")
            
            elif pilihan == "10":
                os.system('cls')
                array.manggil_array()
                array.login()
                x = input("")



if __name__ == "__main__":
    array.manggil_array()
    array.login()  # Memanggil method manggil_array() terlebih dahulu

    q = myQueue()
    q.main_menu()  # Kemudian memanggil method main_menu()

















