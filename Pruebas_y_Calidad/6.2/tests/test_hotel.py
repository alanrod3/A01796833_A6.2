import unittest
import os
import json
from Pruebas_y_Calidad.6.2.source.hotel import Hotel

class TestHotel(unittest.TestCase):
    def setUp(self):
        """Limpia el archivo de datos antes de cada prueba."""
        if os.path.exists(Hotel.FILE_PATH):
            os.remove(Hotel.FILE_PATH)
        self.hotel_id = "H001"

    def test_create_and_display(self):
        """Prueba creación y visualización (Happy Path)."""
        Hotel.create_hotel(self.hotel_id, "Hotel Test", "CDMX", 10)
        info = Hotel.display_information(self.hotel_id)
        self.assertEqual(info['name'], "Hotel Test")

    def test_modify_hotel(self):
        """Prueba la modificación de datos."""
        Hotel.create_hotel(self.hotel_id, "Original", "Cancun", 5)
        Hotel.modify_information(self.hotel_id, name="Nuevo Nombre")
        info = Hotel.display_information(self.hotel_id)
        self.assertEqual(info['name'], "Nuevo Nombre")

    def test_delete_hotel(self):
        """Prueba la eliminación de un hotel."""
        Hotel.create_hotel(self.hotel_id, "Borrar", "Local", 1)
        Hotel.delete_hotel(self.hotel_id)
        self.assertIsNone(Hotel.display_information(self.hotel_id))

    def test_invalid_json_handling(self):
        """Req 5: Verifica que el programa no truene con JSON inválido."""
        os.makedirs(os.path.dirname(Hotel.FILE_PATH), exist_ok=True)
        with open(Hotel.FILE_PATH, 'w') as f:
            f.write("{'bad_json': True")  # JSON mal formado
        
        # Debe retornar dict vacío y no lanzar excepción
        data = Hotel._load_data()
        self.assertEqual(data, {})

if __name__ == '__main__':
    unittest.main()