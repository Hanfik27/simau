from models.jurusan import JurusanModel

class JurusanController:

    @staticmethod
    def list_jurusan():
        return JurusanModel.get_all()

    @staticmethod
    def find_jurusan(ID_JURUSAN):
        return JurusanModel.get_by_id(ID_JURUSAN)

    @staticmethod
    def add_jurusan(NAMA_JURUSAN):
        ID_JURUSAN = JurusanModel.generate_jurusan_id()
        data = {
            "ID_JURUSAN": ID_JURUSAN,
            "NAMA_JURUSAN": NAMA_JURUSAN
        }
        JurusanModel.insert(data)
        print(f"jurusan {NAMA_JURUSAN} berhasil ditambahkan dengan ID {ID_JURUSAN}.")

    @staticmethod
    def update_jurusan(ID_JURUSAN, NAMA_JURUSAN=None):
        data = {}
        if NAMA_JURUSAN:
            data["NAMA_JURUSAN"] = NAMA_JURUSAN
        if data:
            JurusanModel.update(ID_JURUSAN, data)
            print(f"jurusan dengan ID {ID_JURUSAN} berhasil diperbarui.")
        else:
            print("Tidak ada data yang diubah.")

    @staticmethod
    def delete_jurusan(ID_JURUSAN):
        data = JurusanModel.get_by_id(ID_JURUSAN) 
        if data: 
            JurusanModel.delete(ID_JURUSAN) 
            print(f"jurusan dengan ID {ID_JURUSAN} berhasil dihapus.")
        else: 
            print(f"Tidak ada data yang ditemukan dengan ID {ID_JURUSAN}.")

