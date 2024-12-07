from core.lib.db import lab_col

class LabModel:
    @staticmethod
    def generate_lab_id():
        
        last_lab = lab_col.find_one(sort=[("ID_LAB", -1)])  
        if last_lab:
            last_id = int(last_lab["ID_LAB"][1:])  
            new_id = f"L{last_id + 1:02d}" 
        else:
            new_id = "L01" 
        return new_id

    @staticmethod
    def get_all():
        return list(lab_col.find({}))

    @staticmethod
    def get_by_id(ID_LAB):
        return lab_col.find_one({"ID_LAB": ID_LAB})

    @staticmethod
    def insert(data):
        data["ID_LAB"] = LabModel.generate_lab_id()
        result = lab_col.insert_one(data)
        return result.inserted_id if result.inserted_id else None
    @staticmethod
    def update(ID_LAB, data):
        return lab_col.update_one({"ID_LAB": ID_LAB}, {"$set": data})

    @staticmethod
    def delete(ID_LAB):
        return lab_col.delete_one({"ID_LAB": ID_LAB})
