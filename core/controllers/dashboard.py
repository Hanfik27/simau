from views.absensi import AbsensiView
from views.dashboard import DashboardView
from views.dosen import DosenView
from views.fakultas import FakultasView
from views.gedung import GedungView
from views.jadwal import JadwalView
from core.controllers.jadwal import JadwalController
from views.jurusan import JurusanView
from views.kelas import KelasView
from views.lab import LabView
from views.mahasiswa import MahasiswaView
from views.matkul import MatkulView
from views.nilai import NilaiView
from views.user import UserView

class DashboardController:

    @staticmethod
    def show_dashboard(role):
        while True:
            choice = DashboardView.show_menu(role)

            if choice == "0":
                DashboardView.show_logout_message()
                break

            if role == "admin":
                if choice == "1":
                    AbsensiView.menu()
                elif choice == "2":
                    DosenView.menu()
                elif choice == "3":
                    FakultasView.menu()
                elif choice == "4":
                    GedungView.menu()
                elif choice == "5":
                    JadwalView.menu()
                elif choice == "6":
                    JurusanView.menu()
                elif choice == "7":
                    KelasView.menu()
                elif choice == "8":
                    LabView.menu()
                elif choice == "9":
                    MahasiswaView.menu()
                elif choice == "10":
                    MatkulView.menu()
                elif choice == "11":
                    NilaiView.menu()
                elif choice == "12":
                    UserView.menu()
                else:
                    print("Pilihan tidak valid.")
            elif role == "mahasiswa":
                if choice == "1":
                    JadwalController.lihat_jadwal()
                elif choice == "2":
                    NilaiView.lihat_nilai_mahasiswa()
                else:
                    print("Pilihan tidak valid.")
            elif role == "dosen":
                if choice == "1":
                    JadwalController.lihat_jadwal()
                elif choice == "2":
                    NilaiView.menu()
                elif choice == "3":
                    AbsensiView.menu()
                else:
                    print("Pilihan tidak valid.")
            else:
                print("Role tidak dikenali.")
                break
