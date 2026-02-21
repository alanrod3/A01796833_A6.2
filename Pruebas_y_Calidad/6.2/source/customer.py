"""
Module for Customer management.
"""
import json
import os


class Customer:
    """Clase para gestionar la información de Clientes."""
    FILE_PATH = '../data/customers.json'

    @classmethod
    def _load_data(cls):
        """Loads customer records from the JSON storage."""
        if not os.path.exists(cls.FILE_PATH):
            return {}
        try:
            with open(cls.FILE_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error al cargar datos de clientes: {e}")
            return {}

    @classmethod
    def _save_data(cls, data):
        """Saves customer records to the JSON storage."""
        os.makedirs(os.path.dirname(cls.FILE_PATH), exist_ok=True)
        with open(cls.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

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
