from core.lib.db import nilai_col

class NilaiModel:
    @staticmethod
    def generate_id_nilai():
        last_nilai = nilai_col.find_one(sort=[("ID_NILAI", -1)])  
        if last_nilai:
            last_id = int(last_nilai["ID_NILAI"][2:])  
            new_id = f"NL{last_id + 1:02d}" 
        else:
            new_id = "NL01" 
        return new_id
    @staticmethod
    def generate_nilai():
        last_nilai = nilai_col.find_one(sort=[("ID_NILAI", -1)])  # Use ID_NILAI for generation
        if last_nilai:
            last_id = int(last_nilai["ID_NILAI"][2:])  # Extract last ID
            new_id = f"I{last_id + 1:02d}"  # Generate new ID
        else:
            new_id = "I01"  # Default for first entry
        return new_id
    
    @staticmethod
    def get_nilai_by_mahasiswa(NAMA_MAHASISWA):
        """Retrieve grade data for a specific student by name."""
        print(f"Searching for student: {NAMA_MAHASISWA}")  # Debug print
        
        # Pencarian lebih fleksibel dengan regex (case-insensitive)
        pipeline = [
            {"$match": {"NAMA_MAHASISWA": {"$regex": f"^{NAMA_MAHASISWA}$", "$options": "i"}}},  # Case-insensitive matching
            {"$unwind": "$NILAI"},
            {
                "$lookup": {
                    "from": "mata_kuliah",
                    "localField": "NILAI.ID_MATA_KULIAH",
                    "foreignField": "_id",
                    "as": "MATA_KULIAH_DETAIL"
                }
            },
            {"$unwind": "$MATA_KULIAH_DETAIL"},
            {
                "$project": {
                    "_id": 0,
                    "ID_NILAI": "$NILAI.ID_NILAI",
                    "NAMA_MATA_KULIAH": "$MATA_KULIAH_DETAIL.NAMA",
                    "SKS": "$MATA_KULIAH_DETAIL.SKS",
                    "GRADE": "$NILAI.GRADE",
                    "INDEKS": "$NILAI.INDEKS",
                    "KN": {"$multiply": ["$MATA_KULIAH_DETAIL.SKS", "$NILAI.INDEKS"]}
                }
            }
        ]
        
        # Print all documents to understand the data structure
        result = list(nilai_col.aggregate(pipeline))

        all_docs = list(nilai_col.find({"NAMA_MAHASISWA": {"$regex": f"^{NAMA_MAHASISWA}$", "$options": "i"}}))  # Debugging
        print("All matching documents:", all_docs, result)
                
        return result

    @staticmethod
    def insert(ID_MAHASISWA, NAMA_MAHASISWA, NAMA_MATKUL, GRADE, INDEKS):
        """Insert or update a grade record for a student."""
        # Generate unique IDs for the grade entry and overall record
        ID_NILAI = NilaiModel.generate_id_nilai()
        ID_IPK = NilaiModel.generate_nilai()

        # Data for a single course grade
        nilai_data = {
            "ID_IPK": ID_IPK,
            "NAMA_MATKUL": NAMA_MATKUL,
            "GRADE": GRADE,
            "INDEKS": INDEKS
        }

        # Check if the student already exists in the collection
        existing_record = nilai_col.find_one({"ID_MAHASISWA": ID_MAHASISWA})

        if existing_record:
            # Append the new grade data to the existing record
            nilai_col.update_one(
                {"ID_MAHASISWA": ID_MAHASISWA},
                {"$push": {"NILAI": nilai_data}}
            )
        else:
            # Create a new record for the student
            new_record = {
                "ID_NILAI": ID_NILAI,
                "NAMA_MAHASISWA": NAMA_MAHASISWA,
                "ID_MAHASISWA": ID_MAHASISWA,
                "NILAI": [nilai_data]
            }
            nilai_col.insert_one(new_record)

        return ID_NILAI


    @staticmethod
    def update(ID_NILAI, GRADE=None, INDEKS=None):
        """Update grade by ID_NILAI."""
        update_fields = {}
        if GRADE:
            update_fields["NILAI.$.GRADE"] = GRADE
        if INDEKS is not None:
            update_fields["NILAI.$.INDEKS"] = INDEKS

        nilai_col.update_one(
            {"NILAI.ID_NILAI": ID_NILAI},
            {"$set": update_fields}
        )

    @staticmethod
    def delete(ID_NILAI):
        nilai_col.delete_one({"ID_NILAI": ID_NILAI})

    @staticmethod
    def delete_by_id_ipk(ID_NILAI, ID_IPK):
        """Delete a specific grade by ID_NILAI and ID_IPK."""
        # Cari dokumen dengan ID_NILAI yang cocok
        existing_grade = nilai_col.find_one(
            {"ID_NILAI": ID_NILAI, "NILAI.ID_IPK": ID_IPK}
        )

        if existing_grade:
            # Hapus nilai spesifik dari array NILAI
            nilai_col.update_one(
                {"ID_NILAI": ID_NILAI},
                {"$pull": {"NILAI": {"ID_IPK": ID_IPK}}}
            )
            return True
        return False

    @staticmethod
    def get_all_nilai():
        """Retrieve all grade data."""
        return list(nilai_col.find())