"""
Module for Reservation management.
"""
import json
import os


class Reservation:
    """Class handling the logic for room bookings."""
    FILE_PATH = '../data/reservations.json'

    @classmethod
    def _load_data(cls):
        """Loads reservation lists from the storage file."""
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
        """Saves reservation lists to the storage file."""
        os.makedirs(os.path.dirname(cls.FILE_PATH), exist_ok=True)
        with open(cls.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def create_reservation(cls, res_id, customer_id, hotel_id):
        """Registers a new booking for a customer at a hotel."""
        data = cls._load_data()
        data.append({
            'res_id': res_id,
            'customer_id': customer_id,
            'hotel_id': hotel_id
        })
        cls._save_data(data)

    @classmethod
    def cancel_reservation(cls, res_id):
        """Cancels an existing booking based on the reservation ID."""
        data = cls._load_data()
        data = [r for r in data if r['res_id'] != res_id]
        cls._save_data(data)
