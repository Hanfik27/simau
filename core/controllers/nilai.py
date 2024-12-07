from models.nilai import NilaiModel

class NilaiController:
    @staticmethod
    def list_all_nilai():
        """Get all grade data."""
        return NilaiModel.get_all_nilai()

    @staticmethod
    def insert_nilai(ID_MAHASISWA, NAMA_MAHASISWA, NAMA_MATKUL, GRADE, INDEKS):
        """Add new grade with validation."""
        if not ID_MAHASISWA or not NAMA_MATKUL:
            print("Student ID and Course ID must be filled.")
            return False
                
        valid_grades = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D', 'E']
        if GRADE not in valid_grades:
            print("Invalid grade.")
            return False
        
        try:
            INDEKS = float(INDEKS)
            if INDEKS < 0 or INDEKS > 4.0:
                print("Index must be between 0 and 4.0")
                return False
        except ValueError:
            print("Index must be a number.")
            return False
        
        NilaiModel.insert(ID_MAHASISWA, NAMA_MAHASISWA, NAMA_MATKUL, GRADE, INDEKS)
        print(f"Grade for Course {NAMA_MATKUL} added successfully.")
        return True

    @staticmethod
    def update_nilai(ID_NILAI, GRADE=None, INDEKS=None):
        NilaiModel.update(ID_NILAI, GRADE, INDEKS)
        print(f"Grade with ID_NILAI {ID_NILAI} updated successfully.")

    @staticmethod
    def delete_nilai(ID_NILAI):
        try:
            NilaiModel.delete(ID_NILAI)
            print(f"Grade with ID_NILAI '{ID_NILAI}' deleted successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def delete_ipk(ID_NILAI, ID_IPK):
        """Delete specific grade by ID_NILAI and ID_IPK."""
        try:
            result = NilaiModel.delete_by_id_ipk(ID_NILAI, ID_IPK)
            if result:
                print(f"Data dengan ID_NILAI '{ID_NILAI}' dan ID_IPK '{ID_IPK}' berhasil dihapus.")
            else:
                print(f"Tidak ditemukan data dengan ID_NILAI '{ID_NILAI}' dan ID_IPK '{ID_IPK}'.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

    @staticmethod
    def get_nilai_by_mahasiswa(NAMA_MAHASISWA):
        """Get grades and details for a student by name."""
        try:
            return NilaiModel.get_nilai_by_mahasiswa(NAMA_MAHASISWA)
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
