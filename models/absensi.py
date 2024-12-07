from datetime import datetime
from core.lib.db import absensi_col, mahasiswa_col

class AbsensiModel:
    @staticmethod
    def generate_id_absensi():
        """Generate ID_ABSENSI secara otomatis."""
        last_absensi = absensi_col.find_one(sort=[("ID_ABSENSI", -1)])
        if last_absensi:
            last_id = int(last_absensi["ID_ABSENSI"][1:])
            return f"A{last_id + 1:02d}"
        return "A01"

    @staticmethod
    def insert_absensi(ID_MAHASISWA, STATUS_ABSEN):
        """Insert data absensi baru."""
        mahasiswa = mahasiswa_col.find_one({"ID_MAHASISWA": ID_MAHASISWA})
        if not mahasiswa:
            raise ValueError(f"Mahasiswa dengan ID_MAHASISWA '{ID_MAHASISWA}' tidak ditemukan.")

        absensi_data = {
            "ID_ABSENSI": AbsensiModel.generate_id_absensi(),
            "ID_MAHASISWA": mahasiswa["ID_MAHASISWA"],
            "NAMA_MAHASISWA": mahasiswa["NAMA"],
            "TGL_ABSENSI": datetime.now(),
            "STATUS_ABSEN": STATUS_ABSEN
        }
        absensi_col.insert_one(absensi_data)
        return absensi_data

    @staticmethod
    def get_all_absensi():
        """Ambil semua data absensi."""
        return list(absensi_col.find())

    @staticmethod
    def get_absensi_by_mahasiswa(ID_MAHASISWA):
        """Ambil data absensi berdasarkan ID_MAHASISWA."""
        return list(absensi_col.find({"ID_MAHASISWA": ID_MAHASISWA}))

    @staticmethod
    def update_absensi(ID_ABSENSI, TGL_ABSENSI=None, STATUS_ABSEN=None):
        """Update data absensi berdasarkan ID_ABSENSI."""
        update_fields = {}
        if TGL_ABSENSI:
            update_fields["TGL_ABSENSI"] = datetime.strptime(TGL_ABSENSI, "%D-%M-%Y")
        if STATUS_ABSEN:
            update_fields["STATUS_ABSEN"] = STATUS_ABSEN

        result = absensi_col.update_one(
            {"ID_ABSENSI": ID_ABSENSI},
            {"$set": update_fields}
        )
        return result.modified_count

    @staticmethod
    def delete_absensi(ID_ABSENSI):
        """Hapus data absensi berdasarkan ID_ABSENSI."""
        result = absensi_col.delete_one({"ID_ABSENSI": ID_ABSENSI})
        return result.deleted_count
