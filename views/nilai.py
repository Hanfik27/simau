import os
from core.controllers.nilai import NilaiController

class NilaiView:
    @staticmethod
    def menu():
        while True:
            os.system("cls")
            print("\n=== Manage Grades ===")
            print("1. Add Grade")
            print("2. Update Grade")
            print("3. Delete Course")
            print("4. Delete Grade")
            print("5. View All Grades")
            print("6. View Student Grades")
            print("0. Back")

            choice = input("Select menu: ")
            if choice == "1":
                NilaiView.tambah_nilai()
            elif choice == "2":
                NilaiView.perbarui_nilai()
            elif choice == "3":
                NilaiView.delete_ipk()
            elif choice == "4":
                NilaiView.delete_nilai()
            elif choice == "5":
                NilaiView.lihat_semua_nilai()
            elif choice == "6":
                NilaiView.lihat_nilai_mahasiswa()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
            input("Press Enter to continue...")

    @staticmethod
    def tambah_nilai():
        try:
            ID_MAHASISWA = input("Enter Student ID: ").strip()
            NAMA_MAHASISWA = input("Enter Student Name: ").strip()
            NAMA_MATKUL = input("Enter Course name: ").strip()
            GRADE = input("Enter Grade (A, B+, etc.): ").strip().upper()
            INDEKS = input("Enter Index (4.0, 3.5, etc.): ").strip()
            
            NilaiController.insert_nilai(ID_MAHASISWA, NAMA_MAHASISWA, NAMA_MATKUL, GRADE, INDEKS)
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def perbarui_nilai():
        try:
            ID_NILAI = input("Enter Grade ID: ").strip()
            if not ID_NILAI:
                print("Grade ID cannot be empty.")
                return

            GRADE = input("Enter new Grade (leave blank if no change): ").strip().upper() or None
            INDEKS = input("Enter new Index (leave blank if no change): ").strip()

            if GRADE and GRADE not in ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D', 'E']:
                print("Invalid grade.")
                return

            INDEKS = float(INDEKS) if INDEKS else None
            if INDEKS is not None and (INDEKS < 0 or INDEKS > 4.0):
                print("Index must be between 0 and 4.0")
                return

            NilaiController.update_nilai(ID_NILAI, GRADE, INDEKS)
        except ValueError:
            print("Index must be a number.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def delete_nilai():
        ID_NILAI = input("Enter Grade ID (ID_NILAI) to delete: ").strip()
        if not ID_NILAI:
            print("Grade ID cannot be empty.")
            return
        NilaiController.delete_nilai(ID_NILAI)

    @staticmethod
    def delete_ipk():
        """View for deleting a grade entry by ID_IPK within a specific ID_NILAI."""
        ID_NILAI = input("Silahkan input tujuan ID_NILAI: ").strip()
        if not ID_NILAI:
            print("ID_NILAI tidak boleh kosong.")
            return

        ID_IPK = input("Silahkan input yang mau dihapus ID_IPK: ").strip()
        if not ID_IPK:
            print("ID_IPK tidak boleh kosong.")
            return

        NilaiController.delete_ipk(ID_NILAI, ID_IPK)

    @staticmethod
    def lihat_semua_nilai():
        nilai = NilaiController.list_all_nilai()
        if not nilai:
            print("No grade data.")
        else:
            for n in nilai:
                print(f"Grade ID: {n['ID_NILAI']}",
                      f"Student ID: {n['ID_MAHASISWA']}",
                      f"Student Name: {n['NAMA_MAHASISWA']}")
                for nilai_item in n.get('NILAI', []):
                    print(
                          f"Course ID: {nilai_item['ID_IPK']}, "
                          f"Course Name: {nilai_item['NAMA_MATKUL']}, "
                          f"Grade: {nilai_item['GRADE']}, "
                          f"Index: {nilai_item['INDEKS']}")
    @staticmethod
    def lihat_nilai_mahasiswa():
        """View grades for a specific student without totals."""
        NAMA_MAHASISWA = input("Enter Student Name: ").strip()
        if not NAMA_MAHASISWA:
            print("Student name cannot be empty.")
        else:
            # Mengambil nilai berdasarkan nama mahasiswa
            NilaiController.get_nilai_by_mahasiswa(NAMA_MAHASISWA)
            return

