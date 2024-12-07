import os
from core.controllers.jurusan import JurusanController

class JurusanView:
    @staticmethod
    def menu():
        while True:
            print("\n=== Menu Jurusan ===")
            print("1. Lihat Jurusan")
            print("2. Cari Jurusan")
            print("3. Tambah Jurusan")
            print("4. Perbarui Jurusan")
            print("5. Hapus Jurusan")
            print("0. Back to Admin Menu")

            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                jurusan = JurusanController.list_jurusan()
                for m in jurusan:
                    print(m)
            elif pilihan == "2":
                ID_JURUSAN = input("Masukkan ID jurusan: ")
                jurusan = JurusanController.find_jurusan(ID_JURUSAN)
                print(jurusan)
            elif pilihan == "3":
                NAMA_Jurusan = input("Masukkan jurusan: ")
                JurusanController.add_jurusan(NAMA_Jurusan)
            elif pilihan == "4":
                ID_JURUSAN = input("Masukkan ID: ")
                NAMA_Jurusan = input("Masukkan jurusan baru: ")
                JurusanController.update_jurusan(ID_JURUSAN, NAMA_Jurusan)
            elif pilihan == "5":
                ID_JURUSAN = input("Masukkan ID jurusan: ")
                JurusanController.delete_jurusan(ID_JURUSAN)
            elif pilihan == "0":
                break
            else:
                print("Pilihan tidak valid.")
