import unittest
import os
import json
from Pruebas_y_Calidad.6.2.source.customer import Customer

class TestCustomer(unittest.TestCase):
    """Pruebas unitarias para la clase Customer."""

    def setUp(self):
        """Configuración inicial: Limpia el archivo de datos antes de cada prueba."""
        if os.path.exists(Customer.FILE_PATH):
            os.remove(Customer.FILE_PATH)
        self.cust_id = "C001"
        self.name = "Juan Perez"
        self.email = "juan@example.com"

    def test_create_customer(self):
        """Verifica que un cliente se cree y persista correctamente."""
        Customer.create_customer(self.cust_id, self.name, self.email)
        data = Customer._load_data()
        self.assertIn(self.cust_id, data)
        self.assertEqual(data[self.cust_id]['name'], self.name)

    def test_display_customer(self):
        """Verifica la recuperación de información de un cliente."""
        Customer.create_customer(self.cust_id, self.name, self.email)
        info = Customer.display_information(self.cust_id)
        self.assertIsNotNone(info)
        self.assertEqual(info['email'], self.email)

    def test_modify_customer(self):
        """Verifica la actualización de los datos del cliente."""
        Customer.create_customer(self.cust_id, self.name, self.email)
        Customer.modify_information(self.cust_id, name="Juan Garcia")
        info = Customer.display_information(self.cust_id)
        self.assertEqual(info['name'], "Juan Garcia")

    def test_delete_customer(self):
        """Verifica la eliminación de un cliente del sistema."""
        Customer.create_customer(self.cust_id, self.name, self.email)
        Customer.delete_customer(self.cust_id)
        info = Customer.display_information(self.cust_id)
        self.assertIsNone(info)

    def test_invalid_json_file(self):
        """Req 5: Manejo de archivos corruptos o datos inválidos."""
        # Creamos un archivo con contenido que no es JSON válido
        os.makedirs(os.path.dirname(Customer.FILE_PATH), exist_ok=True)
        with open(Customer.FILE_PATH, 'w', encoding='utf-8') as f:
            f.write("ESTO_NO_ES_JSON")
        
        # El programa debe manejar el error, imprimirlo y continuar con un dict vacío
        data = Customer._load_data()
        self.assertEqual(data, {})

if __name__ == '__main__':
    unittest.main()