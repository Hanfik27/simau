import os
from core.controllers.kelas import KelasController

class KelasView:
    @staticmethod
    def menu():
        while True:
            print("\n=== Menu Kelas ===")
            print("1. Lihat Kelas")
            print("2. Cari Kelas")
            print("3. Tambah Kelas")
            print("4. Perbarui Kelas")
            print("5. Hapus Kelas")
            print("0. Back to Admin Menu")

            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                kelas = KelasController.list_kelas()
                for m in kelas:
                    print(m)
            elif pilihan == "2":
                ID_kelas = input("Masukkan ID kelas: ")
                kelas = KelasController.find_kelas(ID_kelas)
                print(kelas)
            elif pilihan == "3":
                NAMA_kelas = input("Masukkan kelas: ")
                KelasController.add_kelas(NAMA_kelas)
            elif pilihan == "4":
                ID_kelas = input("Masukkan ID: ")
                NAMA_kelas = input("Masukkan kelas baru: ")
                KelasController.update_kelas(ID_kelas, NAMA_kelas)
            elif pilihan == "5":
                ID_kelas = input("Masukkan ID kelas: ")
                KelasController.delete_kelas(ID_kelas)
            elif pilihan == "0":
                break
            else:
                print("Pilihan tidak valid.")
