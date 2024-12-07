from core.controllers.jadwal import JadwalController

class JadwalView:
    def menu():
        """Menu for managing schedules."""
        while True:
            print("\nJadwal Menu")
            print("1. Add Schedule")
            print("2. View Schedules")
            print("3. Update Schedule")
            print("4. Delete Schedule")
            print("0. Back to Main Menu")
            pilihan = input("Choose an option: ").strip()
            
            if pilihan == "1":
                NAMA_JADWAL = input("Masukkan Nama Jadwal: ").strip()
                HARI = input("Masukkan Hari: ").strip()
                JAM = input("Masukkan Jam: ").strip()
                NAMA_KELAS = input("Masukkan Nama Kelas: ").strip()
                NAMA_LAB = input("Masukkan Nama Lab: ").strip()
                NAMA_MATKUL = input("Masukkan Nama Mata Kuliah: ").strip()
                JadwalController.add_jadwal(NAMA_JADWAL, HARI, JAM, NAMA_KELAS, NAMA_LAB, NAMA_MATKUL)
            elif pilihan == "2":
                JadwalController.lihat_jadwal()
            elif pilihan == "3":
                ID_JADWAL = input("Masukkan ID Jadwal yang ingin diupdate: ")
                print("Kosongkan field jika tidak ingin diupdate.")
                NAMA_JADWAL = input("Masukkan Nama Jadwal Baru: ")
                HARI = input("Masukkan Hari Baru: ")
                JAM = input("Masukkan Jam Baru: ")
                NAMA_KELAS = input("Masukkan Nama Kelas Baru: ")
                NAMA_LAB = input("Masukkan Nama Lab Baru: ")
                NAMA_MATKUL = input("Masukkan Nama Mata Kuliah Baru: ")
                JadwalController.ubah_jadwal(ID_JADWAL, NAMA_JADWAL, HARI, JAM, NAMA_KELAS, NAMA_LAB, NAMA_MATKUL)
            elif pilihan == "4":
                JadwalController.hapus_jadwal()
            elif pilihan == "0":
                break
            else:
                print("Invalid option. Please try again.")
