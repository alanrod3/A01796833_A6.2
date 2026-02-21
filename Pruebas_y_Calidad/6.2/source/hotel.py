"""
Module for managing Hotel information and persistence.
"""
from file_manager import load_data, save_data


class Hotel:
    """Clase para gestionar la información de Hoteles."""
    FILE_PATH = '../data/hotels.json'

    def __init__(self, hotel_id, name, location, total_rooms):
        """Initialize a hotel instance."""
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.total_rooms = total_rooms

    @classmethod
    def _load_data(cls):
        """Usa la utilidad centralizada."""
        return load_data(cls.FILE_PATH)

    @classmethod
    def _save_data(cls, hotels):
        """Usa la utilidad centralizada."""
        save_data(cls.FILE_PATH, hotels)

    @classmethod
    def create_hotel(cls, hotel_id, name, location, rooms):
        """Creates a new hotel entry in the system."""
        data = cls._load_data()
        data[hotel_id] = {'name': name, 'location': location, 'rooms': rooms}
        cls._save_data(data)

    @classmethod
    def delete_hotel(cls, hotel_id):
        """Deletes a hotel entry by its ID."""
        data = cls._load_data()
        if hotel_id in data:
            del data[hotel_id]
            cls._save_data(data)

    @classmethod
    def display_information(cls, hotel_id):
        """Returns and prints hotel details."""
        data = cls._load_data()
        hotel = data.get(hotel_id)
        if hotel:
            print(f"Hotel: {hotel['name']}, Ubicación: {hotel['location']}")
        return hotel

    @classmethod
    def modify_information(cls, hotel_id, **kwargs):
        """Modifies specific attributes of an existing hotel."""
        data = cls._load_data()
        if hotel_id in data:
            data[hotel_id].update(kwargs)
            cls._save_data(data)
