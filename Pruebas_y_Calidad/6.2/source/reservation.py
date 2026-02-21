import json
import os

class Reservation:
    """Clase para gestionar Reservaciones."""
    FILE_PATH = '../data/reservations.json'

    @classmethod
    def _load_data(cls):
        if not os.path.exists(cls.FILE_PATH):
            return []
        try:
            with open(cls.FILE_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error al cargar reservaciones: {e}")
            return []

    @classmethod
    def _save_data(cls, data):
        os.makedirs(os.path.dirname(cls.FILE_PATH), exist_ok=True)
        with open(cls.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def create_reservation(cls, res_id, customer_id, hotel_id):
        data = cls._load_data()
        data.append({
            'res_id': res_id,
            'customer_id': customer_id,
            'hotel_id': hotel_id
        })
        cls._save_data(data)

    @classmethod
    def cancel_reservation(cls, res_id):
        data = cls._load_data()
        data = [r for r in data if r['res_id'] != res_id]
        cls._save_data(data)