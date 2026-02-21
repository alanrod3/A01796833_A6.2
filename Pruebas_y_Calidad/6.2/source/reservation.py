"""
Module for Reservation management.
"""
import json
import os
from .file_manager import load_data, save_data


class Reservation:
    """Class handling the logic for room bookings."""
    FILE_PATH = '../data/reservations.json'

    def __init__(self, res_id, customer_id, hotel_id):
        """Initialize reservation instance."""
        self.res_id = res_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    @classmethod
    def _load_data(cls):
        """Usa la utilidad centralizada. Retorna lista vacía si falla."""
        data = load_data(cls.FILE_PATH)
        return data if isinstance(data, list) else []

    @classmethod
    def _save_data(cls, data):
        """Usa la utilidad centralizada para guardar datos."""
        save_data(cls.FILE_PATH, data)

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
        data = [r for r in data if r.get('res_id') != res_id]
        cls._save_data(data)