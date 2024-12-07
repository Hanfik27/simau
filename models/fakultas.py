from core.lib.db import fakultas_col

class FakultasModel:
    @staticmethod
    def generate_fakultas_id():
        
        last_fakultas = fakultas_col.find_one(sort=[("ID_FAKULTAS", -1)])  
        if last_fakultas:
            last_id = int(last_fakultas["ID_FAKULTAS"][1:])  
            new_id = f"F{last_id + 1:02d}" 
        else:
            new_id = "F01" 
        return new_id

    @staticmethod
    def get_all():
        return list(fakultas_col.find({}))

    @staticmethod
    def get_by_id(ID_FAKULTAS):
        return fakultas_col.find_one({"ID_FAKULTAS": ID_FAKULTAS})

    @staticmethod
    def insert(data):
        data["ID_FAKULTAS"] = FakultasModel.generate_fakultas_id()
        result = fakultas_col.insert_one(data)
        return result.inserted_id if result.inserted_id else None
    @staticmethod
    def update(ID_FAKULTAS, data):
        return fakultas_col.update_one({"ID_FAKULTAS": ID_FAKULTAS}, {"$set": data})

    @staticmethod
    def delete(ID_FAKULTAS):
        return fakultas_col.delete_one({"ID_FAKULTAS": ID_FAKULTAS})
