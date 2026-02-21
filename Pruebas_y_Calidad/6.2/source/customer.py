"""
Module for Customer management.
"""
from file_manager import load_data, save_data


class Customer:
    """Clase para gestionar la información de Clientes."""
    FILE_PATH = '../data/customers.json'

    def __init__(self, customer_id, name, email):
        """Initialize customer instance."""
        self.customer_id = customer_id
        self.name = name
        self.email = email

    @classmethod
    def _load_data(cls):
        """Usa la utilidad centralizada para cargar datos."""
        return load_data(cls.FILE_PATH)

    @classmethod
    def _save_data(cls, data):
        """Usa la utilidad centralizada para guardar datos."""
        save_data(cls.FILE_PATH, data)

    @classmethod
    def create_customer(cls, customer_id, name, email):
        """Adds a new customer to the database."""
        data = cls._load_data()
        data[customer_id] = {'name': name, 'email': email}
        cls._save_data(data)

    @classmethod
    def delete_customer(cls, customer_id):
        """Removes a customer from the database."""
        data = cls._load_data()
        if customer_id in data:
            del data[customer_id]
            cls._save_data(data)

    @classmethod
    def display_information(cls, customer_id):
        """Retrieves details for a specific customer."""
        data = cls._load_data()
        return data.get(customer_id)

    @classmethod
    def modify_information(cls, customer_id, **kwargs):
        """Updates information for an existing customer."""
        data = cls._load_data()
        if customer_id in data:
            data[customer_id].update(kwargs)
            cls._save_data(data)
