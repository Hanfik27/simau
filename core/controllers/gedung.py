from models.gedung import GedungModel
import requests

class GedungController:
    def geocode_maps(address):
        base_url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": address,
            "format": "json",
            "addressdetails": 1, 
            "limit": 1, 
        }

        headers = {
            "User-Agent": "MyAppName/1.0 (hanfik27@gmail.com)"  
        }

        try:
            response = requests.get(base_url, params=params, headers=headers)
            if response.status_code == 200:
                data = response.json()
                if data:
                    latitude = float(data[0]['lat'])
                    longitude = float(data[0]['lon'])
                    return latitude, longitude
                else:
                    print("Location not found.")
                    return None, None
            else:
                print(f"Error: Unable to fetch data. HTTP Status Code: {response.status_code}")
                return None, None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None, None


    @staticmethod
    def create_gedung(nama_gedung, lokasi, koordinat, fakultas, jumlah_ruangan):
        """Create a new gedung."""
        kode_gedung = GedungModel.generate_kode_gedung()
        data = {
            "KODE_GEDUNG": kode_gedung,
            "NAMA_GEDUNG": nama_gedung,
            "LOKASI": lokasi,
            "KOORDINAT": {
                "type": "Point",
                "coordinates": koordinat
            },
            "FAKULTAS": fakultas,
            "JUMLAH_RUANGAN": jumlah_ruangan
        }
        GedungModel.insert_gedung(data)
        return kode_gedung

    @staticmethod
    def list_gedung():
        """List all gedung."""
        return GedungModel.get_all_gedung()

    @staticmethod
    def find_gedung(kode_gedung):
        """Find a gedung by its kode."""
        return GedungModel.get_gedung_by_kode(kode_gedung)

    @staticmethod
    def update_gedung(kode_gedung, **kwargs):
        """Update gedung details."""
        return GedungModel.update_gedung(kode_gedung, kwargs)

    @staticmethod
    def delete_gedung(kode_gedung):
        """Delete gedung by kode."""
        return GedungModel.delete_gedung(kode_gedung)
