import unittest
import os
import shutil
import sys 

# Add the 'source' directory to the Python path dynamically
current_dir = os.path.dirname(__file__)
source_path = os.path.abspath(os.path.join(current_dir, "..", "source"))
sys.path.append(source_path)

from customer import Customer

class TestCustomer(unittest.TestCase):
    """Pruebas unitarias para la clase Customer."""

    def setUp(self):
        """Configuración antes de cada prueba."""
        self.data_dir = "data"
        self.source_file = os.path.join(self.data_dir, "customers.json")
        self.test_file = Customer.FILE_PATH
        
        os.makedirs(os.path.dirname(self.test_file), exist_ok=True)

        if os.path.exists(self.source_file):
            shutil.copy(self.source_file, self.test_file)
        elif os.path.exists(self.test_file):
            os.remove(self.test_file)
            
        self.customer_id = "C001"

    def tearDown(self):
        """Limpieza después de la prueba."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_create_and_display_customer(self):
        """Prueba creación y visualización de cliente."""
        Customer.create_customer(self.customer_id, "John Doe", "john@example.com")
        info = Customer.display_information(self.customer_id)
        self.assertIsNotNone(info)
        self.assertEqual(info['name'], "John Doe")

    def test_modify_customer(self):
        """Prueba la modificación de un cliente."""
        Customer.create_customer(self.customer_id, "Old Name", "old@mail.com")
        Customer.modify_information(self.customer_id, name="New Name")
        info = Customer.display_information(self.customer_id)
        self.assertEqual(info['name'], "New Name")

    def test_delete_customer(self):
        """Prueba la eliminación de un cliente."""
        Customer.create_customer(self.customer_id, "To Delete", "del@mail.com")
        Customer.delete_customer(self.customer_id)
        self.assertIsNone(Customer.display_information(self.customer_id))

    def test_invalid_customer_json(self):
        """Req 5: Manejo de JSON inválido para clientes."""
        corrupt_source = os.path.join(self.data_dir, "corrupt.json")
        if os.path.exists(corrupt_source):
            shutil.copy(corrupt_source, self.test_file)
        
        data = Customer._load_data()
        self.assertEqual(data, {})

if __name__ == '__main__':
    unittest.main()