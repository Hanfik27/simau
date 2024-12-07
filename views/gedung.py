import os
from core.controllers.gedung import GedungController

class GedungView:
    @staticmethod
    def menu():
        while True:
            os.system("cls")
            print("\n=== Manage Gedung ===")
            print("1. Tambah Gedung")
            print("2. Lihat Semua Gedung")
            print("3. Cari Gedung")
            print("4. Update Gedung")
            print("5. Hapus Gedung")
            print("0. Keluar")

            choice = input("Pilih menu: ")
            if choice == "1":
                GedungView.tambah_gedung()
            elif choice == "2":
                GedungView.lihat_semua_gedung()
            elif choice == "3":
                GedungView.cari_gedung()
            elif choice == "4":
                GedungView.update_gedung()
            elif choice == "5":
                GedungView.hapus_gedung()
            elif choice == "0":
                break
            else:
                print("Pilihan tidak valid.")
            input("Tekan Enter untuk melanjutkan...")

    @staticmethod
    def tambah_gedung():
        nama = input("Nama Gedung: ")
        lokasi = input("Lokasi (contoh: Ketintang, Surabaya): ")
        fakultas = input("Fakultas: ")
        jumlah_ruangan = int(input("Jumlah Ruangan: "))

        # Ambil koordinat berdasarkan lokasi
        lat, lon = GedungController.geocode_maps(lokasi)
        if lat is not None and lon is not None:
            kode = GedungController.create_gedung(
                nama_gedung=nama,
                lokasi=lokasi,
                koordinat=[lon, lat],
                fakultas=fakultas,
                jumlah_ruangan=jumlah_ruangan
            )
            print(f"Gedung {kode} berhasil ditambahkan dengan koordinat {lat}, {lon}.")
        else:
            print("Gagal menambahkan gedung. Koordinat tidak ditemukan.")


    @staticmethod
    def lihat_semua_gedung():
        gedung_list = GedungController.list_gedung()
        for gedung in gedung_list:
            print(gedung)

    @staticmethod
    def cari_gedung():
        kode = input("Kode Gedung: ")
        gedung = GedungController.find_gedung(kode)
        if gedung:
            print(gedung)
        else:
            print("Gedung tidak ditemukan.")

    @staticmethod
    def update_gedung():
        kode = input("Kode Gedung: ")
        nama = input("Nama Gedung (kosongkan jika tidak diubah): ")
        lokasi = input("Lokasi (kosongkan jika tidak diubah): ")
        fakultas = input("Fakultas (kosongkan jika tidak diubah): ")
        jumlah_ruangan = input("Jumlah Ruangan (kosongkan jika tidak diubah): ")

        data = {}
        if nama:
            data["NAMA_GEDUNG"] = nama
        if lokasi:
            data["LOKASI"] = lokasi
        if fakultas:
            data["FAKULTAS"] = fakultas
        if jumlah_ruangan:
            data["JUMLAH_RUANGAN"] = int(jumlah_ruangan)

        GedungController.update_gedung(kode, **data)
        print("Gedung berhasil diperbarui.")

    @staticmethod
    def hapus_gedung():
        kode = input("Kode Gedung: ")
        GedungController.delete_gedung(kode)
        print("Gedung berhasil dihapus.")
