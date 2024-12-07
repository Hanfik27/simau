from core.lib.db import kelas_col

class KelasModel:
    @staticmethod
    def generate_kelas_id():
        
        last_kelas = kelas_col.find_one(sort=[("ID_KELAS", -1)])  
        if last_kelas:
            last_id = int(last_kelas["ID_KELAS"][1:])  
            new_id = f"K{last_id + 1:02d}" 
        else:
            new_id = "K01" 
        return new_id

    @staticmethod
    def get_all():
        return list(kelas_col.find({}))

    @staticmethod
    def get_by_id(ID_KELAS):
        return kelas_col.find_one({"ID_KELAS": ID_KELAS})

    @staticmethod
    def insert(data):
        data["ID_KELAS"] = KelasModel.generate_kelas_id()
        result = kelas_col.insert_one(data)
        return result.inserted_id if result.inserted_id else None
    @staticmethod
    def update(ID_KELAS, data):
        return kelas_col.update_one({"ID_KELAS": ID_KELAS}, {"$set": data})

    @staticmethod
    def delete(ID_KELAS):
        return kelas_col.delete_one({"ID_KELAS": ID_KELAS})
