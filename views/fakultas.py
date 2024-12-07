import os
from core.controllers.fakultas import FakultasController

class FakultasView:
    @staticmethod
    def menu():
        while True:
            print("\n=== Menu Fakultas ===")
            print("1. Lihat Fakultas")
            print("2. Cari Fakultas")
            print("3. Tambah Fakultas")
            print("4. Perbarui Fakultas")
            print("5. Hapus Fakultas")
            print("0. Back to Admin Menu")

            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                fakultas = FakultasController.list_fakultas()
                for m in fakultas:
                    print(m)
            elif pilihan == "2":
                ID_fakultas = input("Masukkan ID fakultas: ")
                fakultas = FakultasController.find_fakultas(ID_fakultas)
                print(fakultas)
            elif pilihan == "3":
                NAMA_FAKULTAS = input("Masukkan Fakultas: ")
                FakultasController.add_fakultas(NAMA_FAKULTAS)
            elif pilihan == "4":
                ID_fakultas = input("Masukkan ID: ")
                NAMA_FAKULTAS = input("Masukkan Fakultas baru: ")
                FakultasController.update_fakultas(ID_fakultas, NAMA_FAKULTAS)
            elif pilihan == "5":
                ID_fakultas = input("Masukkan ID fakultas: ")
                FakultasController.delete_fakultas(ID_fakultas)
            elif pilihan == "0":
                break
            else:
                print("Pilihan tidak valid.")
