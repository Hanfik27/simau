import os
from core.controllers.lab import LabController

class LabView:
    @staticmethod
    def menu():
        while True:
            print("\n=== Menu Laboratorium ===")
            print("1. Lihat Laboratorium")
            print("2. Cari Laboratorium")
            print("3. Tambah Laboratorium")
            print("4. Perbarui Laboratorium")
            print("5. Hapus Laboratorium")
            print("0. Back to Admin Menu")

            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                lab = LabController.list_lab()
                for m in lab:
                    print(m)
            elif pilihan == "2":
                ID_LAB = input("Masukkan ID lab: ")
                lab = LabController.find_lab(ID_LAB)
                print(lab)
            elif pilihan == "3":
                NAMA_LAB = input("Masukkan lab: ")
                LabController.add_lab(NAMA_LAB)
            elif pilihan == "4":
                ID_LAB = input("Masukkan ID: ")
                NAMA_LAB = input("Masukkan lab baru: ")
                LabController.update_lab(ID_LAB, NAMA_LAB)
            elif pilihan == "5":
                ID_LAB = input("Masukkan ID lab: ")
                LabController.delete_lab(ID_LAB)
            elif pilihan == "0":
                break
            else:
                print("Pilihan tidak valid.")
