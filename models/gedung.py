from core.lib.db import gedung_col

class GedungModel:
    @staticmethod
    def generate_kode_gedung():
        """Generate kode gedung otomatis."""
        last_gedung = gedung_col.find_one(sort=[("KODE_GEDUNG", -1)])
        if last_gedung:
            last_id = int(last_gedung["KODE_GEDUNG"][1:])
            new_id = f"G{last_id + 1:02d}"
        else:
            new_id = "G01"
        return new_id

    @staticmethod
    def insert_gedung(data):
        """Insert gedung data."""
        return gedung_col.insert_one(data)

    @staticmethod
    def get_all_gedung():
        """Retrieve all gedung data."""
        return list(gedung_col.find())

    @staticmethod
    def get_gedung_by_kode(kode_gedung):
        """Retrieve a gedung by its kode."""
        return gedung_col.find_one({"KODE_GEDUNG": kode_gedung})

    @staticmethod
    def update_gedung(kode_gedung, data):
        """Update gedung data by kode."""
        return gedung_col.update_one({"KODE_GEDUNG": kode_gedung}, {"$set": data})

    @staticmethod
    def delete_gedung(kode_gedung):
        """Delete gedung by kode."""
        return gedung_col.delete_one({"KODE_GEDUNG": kode_gedung})