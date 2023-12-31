daftar_mahasiswa = {
    1:{"nim":"19220001", "nama_mahasiswa":"Restu Pandu"},
    2:{"nim":"19220002", "nama_mahasiswa":"e5678eiwarsdf"},
    3:{"nim":"19220002", "nama_mahasiswa":"e5678eiwarsdf"},
}

class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama_mahasiswa = nama

    def __str__(self):
        return f"{self.nim} - {self.nama_mahasiswa}"

class Node:
    def __init__(self,mahasiswa):
        self.mahasiswa = mahasiswa
        self.next = None

class LinkedListMahasiswa:
    def __init__(self):
        self.head = None

    def tambah_mahasiswa(self,mahasiswa):
        new_node = Node(mahasiswa)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def tampilkan_mahasiswas(self):
        current = self.head
        while current:
            print(current.mahasiswa)
            current = current.next

class QueueMahasiswa:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, mahasiswa):
        self.items.append(mahasiswa)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Antrian kosong")

    def size(self):
        return len(self.items)

class StackMahasiswa:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, mahasiswa):
        self.items.append(mahasiswa)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack kosong")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack kosong")

    def size(self):
        return len(self.items)

# Contoh Penggunaan
# Array
print("Array Mahasiswa :")
print("=============================================")
print(" No      NIM             Nama Mahasiswa      ")
print("=============================================")
for No, mahasiswa in daftar_mahasiswa.items():
    print(f"{No:<2} {mahasiswa['nim']:<8} {mahasiswa['nama_mahasiswa']:<41}") 

# Linked List
linked_list_mahasiswa = LinkedListMahasiswa()
linked_list_mahasiswa.tambah_mahasiswa(Mahasiswa("201", "Alice"))
linked_list_mahasiswa.tambah_mahasiswa(Mahasiswa("202", "Bob"))
linked_list_mahasiswa.tambah_mahasiswa(Mahasiswa("203", "Charlie"))
print("\nLinked List Mahasiswa:")
linked_list_mahasiswa.tampilkan_mahasiswas()

# Queue
queue_mahasiswa = QueueMahasiswa()
queue_mahasiswa.enqueue(Mahasiswa("301", "Charlie"))
queue_mahasiswa.enqueue(Mahasiswa("302", "David"))
print("\nQueue Mahasiswa, Ukuran:", queue_mahasiswa.size())
dequeued_mahasiswa = queue_mahasiswa.dequeue()
print("Mengambil dari antrian:", dequeued_mahasiswa)
print("Ukuran antrian setelah pengambilan:", queue_mahasiswa.size())

# Stack
stack_mahasiswa = StackMahasiswa()
stack_mahasiswa.push(Mahasiswa("401", "Eva"))
stack_mahasiswa.push(Mahasiswa("402", "Frank"))
print("\nStack Mahasiswa, Ukuran:", stack_mahasiswa.size())
popped_mahasiswa = stack_mahasiswa.pop()
print("Elemen yang diambil dari stack:", popped_mahasiswa)
print("Ukuran stack setelah pengambilan:", stack_mahasiswa.size())