from models.kelas import KelasModel

class KelasController:

    @staticmethod
    def list_kelas():
        return KelasModel.get_all()

    @staticmethod
    def find_kelas(ID_KELAS):
        return KelasModel.get_by_id(ID_KELAS)

    @staticmethod
    def add_kelas(NAMA_KELAS):
        ID_KELAS = KelasModel.generate_kelas_id()
        data = {
            "ID_KELAS": ID_KELAS,
            "NAMA_KELAS": NAMA_KELAS
        }
        KelasModel.insert(data)
        print(f"kelas {NAMA_KELAS} berhasil ditambahkan dengan ID {ID_KELAS}.")

    @staticmethod
    def update_kelas(ID_KELAS, NAMA_KELAS=None):
        data = {}
        if NAMA_KELAS:
            data["NAMA_KELAS"] = NAMA_KELAS
        if data:
            KelasModel.update(ID_KELAS, data)
            print(f"kelas dengan ID {ID_KELAS} berhasil diperbarui.")
        else:
            print("Tidak ada data yang diubah.")

    @staticmethod
    def delete_kelas(ID_KELAS):
        data = KelasModel.get_by_id(ID_KELAS) 
        if data: 
            KelasModel.delete(ID_KELAS) 
            print(f"kelas dengan ID {ID_KELAS} berhasil dihapus.")
        else: 
            print(f"Tidak ada data yang ditemukan dengan ID {ID_KELAS}.")

