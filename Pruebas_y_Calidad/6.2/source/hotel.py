import json
import os

class Hotel:
    """Clase para gestionar la información de Hoteles."""
    FILE_PATH = '../data/hotels.json'

    def __init__(self, hotel_id, name, location, total_rooms):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.total_rooms = total_rooms

    @classmethod
    def _load_data(cls):
        if not os.path.exists(cls.FILE_PATH):
            return {}
        try:
            with open(cls.FILE_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error al cargar datos de hoteles: {e}")
            return {}

    @classmethod
    def _save_data(cls, data):
        try:
            os.makedirs(os.path.dirname(cls.FILE_PATH), exist_ok=True)
            with open(cls.FILE_PATH, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            print(f"Error al guardar datos de hoteles: {e}")

    @classmethod
    def create_hotel(cls, hotel_id, name, location, rooms):
        data = cls._load_data()
        data[hotel_id] = {'name': name, 'location': location, 'rooms': rooms}
        cls._save_data(data)

    @classmethod
    def delete_hotel(cls, hotel_id):
        data = cls._load_data()
        if hotel_id in data:
            del data[hotel_id]
            cls._save_data(data)

    @classmethod
    def display_information(cls, hotel_id):
        data = cls._load_data()
        hotel = data.get(hotel_id)
        if hotel:
            print(f"Hotel: {hotel['name']}, Ubicación: {hotel['location']}")
        return hotel

    @classmethod
    def modify_information(cls, hotel_id, **kwargs):
        data = cls._load_data()
        if hotel_id in data:
            data[hotel_id].update(kwargs)
            cls._save_data(data)