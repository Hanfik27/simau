from models.fakultas import FakultasModel

class FakultasController:

    @staticmethod
    def list_fakultas():
        return FakultasModel.get_all()

    @staticmethod
    def find_fakultas(ID_FAKULTAS):
        return FakultasModel.get_by_id(ID_FAKULTAS)

    @staticmethod
    def add_fakultas(NAMA_FAKULTAS):
        ID_FAKULTAS = FakultasModel.generate_fakultas_id()
        data = {
            "ID_FAKULTAS": ID_FAKULTAS,
            "NAMA_FAKULTAS": NAMA_FAKULTAS
        }
        FakultasModel.insert(data)
        print(f"Fakultas {NAMA_FAKULTAS} berhasil ditambahkan dengan ID {ID_FAKULTAS}.")

    @staticmethod
    def update_fakultas(ID_FAKULTAS, NAMA_FAKULTAS=None):
        data = {}
        if NAMA_FAKULTAS:
            data["NAMA_FAKULTAS"] = NAMA_FAKULTAS
        if data:
            FakultasModel.update(ID_FAKULTAS, data)
            print(f"fakultas dengan ID {ID_FAKULTAS} berhasil diperbarui.")
        else:
            print("Tidak ada data yang diubah.")

    @staticmethod
    def delete_fakultas(ID_FAKULTAS):
        data = FakultasModel.get_by_id(ID_FAKULTAS) 
        if data: 
            FakultasModel.delete(ID_FAKULTAS) 
            print(f"fakultas dengan ID {ID_FAKULTAS} berhasil dihapus.")
        else: 
            print(f"Tidak ada data yang ditemukan dengan ID {ID_FAKULTAS}.")

