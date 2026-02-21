import unittest
import os
import shutil
import sys

# Add the 'source' directory to the Python path dynamically
current_dir = os.path.dirname(__file__)
source_path = os.path.abspath(os.path.join(current_dir, "..", "source"))
sys.path.append(source_path)

from reservation import Reservation

class TestReservation(unittest.TestCase):
    """Pruebas unitarias para la clase Reservation."""

    def setUp(self):
        """Configuración antes de cada prueba."""
        self.data_dir = "data"
        self.source_file = os.path.join(self.data_dir, "reservations.json")
        self.test_file = Reservation.FILE_PATH
        
        os.makedirs(os.path.dirname(self.test_file), exist_ok=True)

        if os.path.exists(self.source_file):
            shutil.copy(self.source_file, self.test_file)
        elif os.path.exists(self.test_file):
            os.remove(self.test_file)
            
        self.res_id = "R001"

    def tearDown(self):
        """Limpieza después de la prueba."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_create_reservation(self):
        """Prueba la creación de una reservación."""
        Reservation.create_reservation(self.res_id, "C001", "H001")
        data = Reservation._load_data()
        self.assertTrue(any(res['reservation_id'] == self.res_id for res in data))

    def test_create_reservation(self):
        """Prueba la creación de una reservación."""
        Reservation.create_reservation(self.res_id, "C001", "H001") 
        
        data = Reservation._load_data()
        
        # Change 'reservation_id' to 'res_id' to match your dictionary output
        self.assertTrue(
            any(res.get('res_id') == self.res_id for res in data),
            f"Reservation {self.res_id} not found in {data}"
        )

    def test_invalid_reservation_json(self):
        """Req 5: Manejo de JSON inválido para reservaciones."""
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write("{'bad': 'format'")
        
        data = Reservation._load_data()
        # Ensure consistency: use [] if the method returns a list on error
        self.assertEqual(data, [])

if __name__ == '__main__':
    unittest.main()