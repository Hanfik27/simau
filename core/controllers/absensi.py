from models.absensi import AbsensiModel

class AbsensiController:
    @staticmethod
    def tambah_absensi(ID_MAHASISWA, STATUS_ABSEN):
        try:
            return AbsensiModel.insert_absensi(ID_MAHASISWA, STATUS_ABSEN)
        except ValueError as e:
            print(e)
            return None

    @staticmethod
    def lihat_semua_absensi():
        return AbsensiModel.get_all_absensi()

    @staticmethod
    def lihat_absensi_mahasiswa(ID_MAHASISWA):
        return AbsensiModel.get_absensi_by_mahasiswa(ID_MAHASISWA)

    @staticmethod
    def perbarui_absensi(ID_ABSENSI, TGL_ABSENSI=None, STATUS_ABSEN=None):
        return AbsensiModel.update_absensi(ID_ABSENSI, TGL_ABSENSI, STATUS_ABSEN)

    @staticmethod
    def hapus_absensi(ID_ABSENSI):
        return AbsensiModel.delete_absensi(ID_ABSENSI)
