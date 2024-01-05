import os
import queue
import sys
from datetime import datetime

siswa=["RESTU", "IQBAL", "SERLINA", "NABILA", "MELANI"]
alamat=["Bekasi", "Jakarta", "Kranji", "Bekasi", "Jati Asih"]
telpon=["08961234", "08965678", "08961111", "08962222", "08963333"]

class Node:
    def __init__(self, siswa, alamat, telpon):
        self.siswa = siswa
        self.alamat = alamat
        self.telpon = telpon
        self.tanggal_pendaftaran = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Ubah datetime menjadi string
        self.next = None
        self.hasil_tes = None
        self.tanggal_diterima = None

    def set_hasil_tes(self, hasil):
        self.hasil_tes = hasil
        if hasil == "Lulus":
            self.tanggal_diterima = datetime.now()

    def __str__(self):
        return f"{self.siswa} - {self.alamat} - {self.telpon} - {self.hasil_tes} - {self.tanggal_diterima}"


class LinkedListMahasiswa:
    def __init__(self):
        self.head = None
        self.length = 0

    def kosong(self):
        return self.head is None

    def mahasiswa_baru(self, siswa, alamat, telpon):
        siswa_baru = Node(siswa, alamat, telpon)
        if self.kosong():
            self.head = siswa_baru
        else:
            node_akhir = self.head
            while node_akhir.next:
                node_akhir = node_akhir.next
            node_akhir.next = siswa_baru
        print("\nPendaftaran Berhasil")
        return siswa_baru 

    def display(self):
        if self.kosong():
            print("Tidak Ada Mahasiswa Yang Mendaftar")
        else:
            print("\nDaftar Mahasiswa Yang Diterima")
            print(f"{'-' * 80}")
            print(f"|{'Nama Mahasiswa':^20}|{'Alamat':^10}|{'Telpon':^10}|{'Status':^15}|{'Tanggal Pendaftaran':^20}|")
            print(f"{'-' * 80}")
            current_node = self.head
            while current_node:
                if current_node.hasil_tes == "Lulus":
                    print(f"|{current_node.siswa:<20}|{current_node.alamat:^10}|{current_node.telpon:^10}|{'Diterima':^15}|{current_node.tanggal_pendaftaran:^20}|")
                else:
                    print(f"|{current_node.siswa:<20}|{current_node.alamat:^10}|{current_node.telpon:^10}|{'Tidak Diterima':^15}|{current_node.tanggal_pendaftaran:^20}|")
                current_node = current_node.next
            print(f"{'-' * 80}")

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items = queue.Queue()
        self.linked_list = LinkedListMahasiswa()
        self.stack_hasil_tes = Stack()

    def antrian_kosong(self):
        return self.items.empty()
    
    def antrian_masuk(self, mahasiswa):
        self.items.put(mahasiswa)

    def antrian_keluar(self):
        if not self.items.empty():
            return self.items.get()
        else:
            print("Data Antrian Kosong")
    
    def size(self):
        return self.items.qsize()

    def tes_masuk_kampus(self):
        if self.linked_list.kosong():
            print("Tidak ada mahasiswa dalam antrian.")
        else:
            while not self.antrian_kosong():  # Ganti mahasiswa dengan antrian
                mahasiswa = self.antrian_keluar()  # Ambil mahasiswa dari antrian
                if mahasiswa is not None:
                    print(f"\nPeserta {mahasiswa.siswa} sedang melakukan tes.")

                    jawaban1 = input("Pertanyaan 1: Siapakah presiden Indonesia pertama? ")
                    jawaban2 = input("Pertanyaan 2: Sebutkan ibukota Indonesia? ")

                    if jawaban1.lower() == "soekarno" and jawaban2.lower() == "jakarta":
                        mahasiswa.set_hasil_tes("Lulus")
                        self.stack_hasil_tes.push((mahasiswa.siswa, "Lulus"))  # Push tuple ke dalam stack
                        print("Silahkan Check hasilnya Di Halaman Menu")
                    else:
                        mahasiswa.set_hasil_tes("Tidak lulus")
                        self.stack_hasil_tes.push((mahasiswa.siswa, "Tidak lulus"))  # Push tuple ke dalam stack
                        print("Silahkan Check hasilnya Di Halaman Menu")

    def tampilkan_hasil_terakhir(self):
        hasil_terakhir = self.stack_hasil_tes.peek()
        if hasil_terakhir is not None:
            nama_siswa, hasil = hasil_terakhir  # Unpack tuple
            print(f"Nama Peserta : {nama_siswa}")
            print(f"Status : Selamat Anda Dinyatakan {hasil}")
        else:
            print("Belum ada hasil tes.")

    def menu(self):
        pilih = "y"
        while(pilih == "y"):
            print("\n=============================")
            print('Program Pendaftaran Mahasiswa')
            print("=============================")
            print(" 1. Daftar")
            print(" 2. Tes Masuk Kampus")
            print(" 3. Hasil Tes")
            print(" 4. Daftar Mahasiswa Yang Mendaftar")
            print(" 5. Keluar")
            print("=============================")
            pilihan = str(input("\nMasukan Pilihan Anda: "))

            if pilihan == "1":
                os.system('cls')
                print("Isi Data Dengan Baik Dan Benar")
                siswa = input("Nama Lengkap : ")
                alamat = input("Alamat : ")
                telpon = input("Nomor Telpon :")
                mahasiswa_baru = self.linked_list.mahasiswa_baru(siswa, alamat, telpon)
                self.antrian_masuk(mahasiswa_baru)
                x = input("")

            elif pilihan == "2":
                os.system('cls')
                self.tes_masuk_kampus()
                x = input("")

            elif pilihan == "3":
                self.tampilkan_hasil_terakhir()
                x = input("")

            elif pilihan == "4":
                self.linked_list.display()
                x = input("")

            elif pilihan == "5":
                print("Terima Kasih Sudah Mendaftar Di Kampus Kami")
                sys.exit()
              
if __name__ == "__main__":
    q = Queue()
    q.menu() 


