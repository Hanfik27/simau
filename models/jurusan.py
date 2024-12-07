from core.lib.db import jurusan_col

class JurusanModel:
    @staticmethod
    def generate_jurusan_id():
        
        last_jurusan = jurusan_col.find_one(sort=[("ID_JURUSAN", -1)])  
        if last_jurusan:
            last_id = int(last_jurusan["ID_JURUSAN"][1:])  
            new_id = f"F{last_id + 1:02d}" 
        else:
            new_id = "F01" 
        return new_id

    @staticmethod
    def get_all():
        return list(jurusan_col.find({}))

    @staticmethod
    def get_by_id(ID_JURUSAN):
        return jurusan_col.find_one({"ID_JURUSAN": ID_JURUSAN})

    @staticmethod
    def insert(data):
        data["ID_JURUSAN"] = JurusanModel.generate_jurusan_id()
        result = jurusan_col.insert_one(data)
        return result.inserted_id if result.inserted_id else None
    @staticmethod
    def update(ID_JURUSAN, data):
        return jurusan_col.update_one({"ID_JURUSAN": ID_JURUSAN}, {"$set": data})

    @staticmethod
    def delete(ID_JURUSAN):
        return jurusan_col.delete_one({"ID_JURUSAN": ID_JURUSAN})
