from core.controllers.absensi import AbsensiController
import os

class AbsensiView:
    @staticmethod
    def menu():
        while True:
            os.system("cls")
            print("\n=== Menu Absensi ===")
            print("1. Tambah Absensi")
            print("2. Lihat Semua Absensi")
            print("3. Lihat Absensi Mahasiswa")
            print("4. Perbarui Absensi")
            print("5. Hapus Absensi")
            print("0. Back")

            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                AbsensiView.tambah_absensi()
            elif pilihan == "2":
                AbsensiView.lihat_semua_absensi()
            elif pilihan == "3":
                AbsensiView.lihat_absensi_mahasiswa()
            elif pilihan == "4":
                AbsensiView.perbarui_absensi()
            elif pilihan == "5":
                AbsensiView.hapus_absensi()
            elif pilihan == "0":
                break
            else:
                print("Pilihan tidak valid.")
            input("Tekan Enter untuk melanjutkan...")

    @staticmethod
    def tambah_absensi():
        try:
            ID_MAHASISWA = input("Masukkan ID Mahasiswa: ").strip()
            STATUS_ABSEN = input("Masukkan Status Absen (Hadir/Izin/Sakit): ").strip()
            result = AbsensiController.tambah_absensi(ID_MAHASISWA, STATUS_ABSEN)
            if result:
                print(f"Absensi berhasil ditambahkan: {result}")
            else:
                print("Gagal menambahkan absensi.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

    @staticmethod
    def lihat_semua_absensi():
        data = AbsensiController.lihat_semua_absensi()
        for absensi in data:
            print(absensi)

    @staticmethod
    def lihat_absensi_mahasiswa():
        ID_MAHASISWA = input("Masukkan ID Mahasiswa: ").strip()
        data = AbsensiController.lihat_absensi_mahasiswa(ID_MAHASISWA)
        for absensi in data:
            print(absensi)

    @staticmethod
    def perbarui_absensi():
        try:
            ID_ABSENSI = input("Masukkan ID Absensi: ").strip()
            TGL_ABSENSI = input("Masukkan Tanggal Absensi Baru (YYYY-MM-DD, kosongkan jika tidak diubah): ").strip()
            STATUS_ABSEN = input("Masukkan Status Absen Baru (kosongkan jika tidak diubah): ").strip()
            updated = AbsensiController.perbarui_absensi(ID_ABSENSI, TGL_ABSENSI or None, STATUS_ABSEN or None)
            if updated:
                print(f"Absensi dengan ID {ID_ABSENSI} berhasil diperbarui.")
            else:
                print("Tidak ada perubahan atau ID Absensi tidak ditemukan.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

    @staticmethod
    def hapus_absensi():
        ID_ABSENSI = input("Masukkan ID Absensi yang ingin dihapus: ").strip()
        deleted = AbsensiController.hapus_absensi(ID_ABSENSI)
        if deleted:
            print(f"Absensi dengan ID {ID_ABSENSI} berhasil dihapus.")
        else:
            print("ID Absensi tidak ditemukan.")
