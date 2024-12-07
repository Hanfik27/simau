from core.lib.db import jadwal_col

class JadwalModel:
    @staticmethod
    def generate_jadwal_id():
        last_jadwal = jadwal_col.find_one(sort=[("ID_JADWAL", -1)])  
        if last_jadwal:
            last_id = int(last_jadwal["ID_JADWAL"][1:])  
            new_id = f"J{last_id + 1:02d}" 
        else:
            new_id = "J01" 
        return new_id

    @staticmethod
    def insert(data):
        data["ID_JADWAL"] = JadwalModel.generate_jadwal_id()
        result = jadwal_col.insert_one(data)
        return result.inserted_id if result.inserted_id else None

    @staticmethod
    def get_all():
        return list(jadwal_col.find())

    @staticmethod
    def update_jadwal(ID_JADWAL, data):
        """Update a schedule by ID."""
        return jadwal_col.update_one({"ID_JADWAL": ID_JADWAL}, {"$set": data}).modified_count

    @staticmethod
    def delete_jadwal(ID_JADWAL):
        """Delete a schedule by ID."""
        return jadwal_col.delete_one({"ID_JADWAL": ID_JADWAL}).deleted_count
