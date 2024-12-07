from models.lab import LabModel

class LabController:

    @staticmethod
    def list_lab():
        return LabModel.get_all()

    @staticmethod
    def find_lab(ID_LAB):
        return LabModel.get_by_id(ID_LAB)

    @staticmethod
    def add_lab(NAMA_LAB):
        ID_LAB = LabModel.generate_lab_id()
        data = {
            "ID_LAB": ID_LAB,
            "NAMA_LAB": NAMA_LAB
        }
        LabModel.insert(data)
        print(f"lab {NAMA_LAB} berhasil ditambahkan dengan ID {ID_LAB}.")

    @staticmethod
    def update_lab(ID_LAB, NAMA_LAB=None):
        data = {}
        if NAMA_LAB:
            data["NAMA_LAB"] = NAMA_LAB
        if data:
            LabModel.update(ID_LAB, data)
            print(f"lab dengan ID {ID_LAB} berhasil diperbarui.")
        else:
            print("Tidak ada data yang diubah.")

    @staticmethod
    def delete_lab(ID_LAB):
        data = LabModel.get_by_id(ID_LAB) 
        if data: 
            LabModel.delete(ID_LAB) 
            print(f"lab dengan ID {ID_LAB} berhasil dihapus.")
        else: 
            print(f"Tidak ada data yang ditemukan dengan ID {ID_LAB}.")

