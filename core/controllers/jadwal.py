from models.jadwal import JadwalModel

class JadwalController:
    @staticmethod
    def add_jadwal(NAMA_JADWAL, HARI, JAM, NAMA_KELAS, NAMA_LAB, NAMA_MATKUL):
        ID_JADWAL = JadwalModel.generate_jadwal_id()
        data = {
            "ID_JADWAL": ID_JADWAL,
            "NAMA_JADWAL": NAMA_JADWAL,
            "HARI": HARI,
            "JAM": JAM,
            "NAMA_KELAS": NAMA_KELAS,
            "NAMA_LAB": NAMA_LAB,
            "NAMA_MATKUL": NAMA_MATKUL
        }
        JadwalModel.insert(data)
        print(f"Berhasil Menambahkan Jadwal dengan ID: {ID_JADWAL}" )


    @staticmethod
    def lihat_jadwal():
        jadwal = JadwalModel.get_all()
        if not jadwal:
            print("Jadwal Tidak Ditemukan.")
        else:
            print("Jadwal:")
            for j in jadwal:
                print(
                    f"ID: {j['ID_JADWAL']}, Nama: {j['NAMA_JADWAL']}, "
                    f"Hari: {j['HARI']}, Jam: {j['JAM']}, Kelas: {j['NAMA_KELAS']}, "
                    f"Lab: {j['NAMA_LAB']}, Mata Kuliah: {j['NAMA_MATKUL']}"
                )

    @staticmethod
    def ubah_jadwal(ID_JADWAL, NAMA_JADWAL=None, HARI=None, JAM=None, NAMA_KELAS=None, NAMA_LAB=None, NAMA_MATKUL=None):

        data = {}
        if NAMA_JADWAL: data["NAMA_JADWAL"] = NAMA_JADWAL
        if HARI: data["HARI"] = HARI
        if JAM: data["JAM"] = JAM
        if NAMA_KELAS: data["NAMA_KELAS"] = NAMA_KELAS
        if NAMA_LAB: data["NAMA_LAB"] = NAMA_LAB
        if NAMA_MATKUL: data["NAMA_MATKUL"] = NAMA_MATKUL
        if data:
            JadwalModel.update_jadwal(ID_JADWAL, data)
            print("Jadwal berhasil diperbarui!")
        else:
            print("Tidak ditemukan jadwal dengan ID yang diberikan.")

    @staticmethod
    def hapus_jadwal():
        id_jadwal = input("Masukkan ID Jadwal yang ingin dihapus: ").strip()
        result = JadwalModel.delete_jadwal(id_jadwal)
        if result:
            print("Jadwal berhasil dihapus!")
        else:
            print("Tidak ditemukan jadwal dengan ID yang diberikan.")
