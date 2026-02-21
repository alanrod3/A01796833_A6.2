import unittest
import os
import shutil
from Pruebas_y_Calidad.6.2.source.hotel import Hotel

class TestHotel(unittest.TestCase):
    """Pruebas unitarias para la clase Hotel."""

    def setUp(self):
        """Configuración antes de cada prueba usando los archivos de data/."""
        self.data_dir = "data"
        self.source_file = os.path.join(self.data_dir, "hotels.json")
        self.test_file = Hotel.FILE_PATH  # El archivo que usa la clase original
        
        # Asegurar que el directorio de destino existe
        os.makedirs(os.path.dirname(self.test_file), exist_ok=True)

        # Si existe un archivo base en data/, lo copiamos para la prueba
        # Si no existe, nos aseguramos de empezar con un archivo limpio
        if os.path.exists(self.source_file):
            shutil.copy(self.source_file, self.test_file)
        elif os.path.exists(self.test_file):
            os.remove(self.test_file)
            
        self.hotel_id = "H001"

    def tearDown(self):
        """Limpieza después de la prueba para no dejar basura."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_create_and_display(self):
        """Prueba creación y visualización (Happy Path)."""
        Hotel.create_hotel(self.hotel_id, "Hotel Test", "CDMX", 10)
        info = Hotel.display_information(self.hotel_id)
        self.assertIsNotNone(info)
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
        """Req 5: Verifica que el programa maneje JSON inválido desde data/."""
        corrupt_source = os.path.join(self.data_dir, "corrupt.json")
        
        # Si creaste el archivo corrupt.json en el commit anterior:
        if os.path.exists(corrupt_source):
            shutil.copy(corrupt_source, self.test_file)
        else:
            # Si no existe, lo creamos manualmente para la prueba
            with open(self.test_file, 'w', encoding='utf-8') as f:
                f.write("{'invalid': json")

        # Debe retornar dict vacío y no lanzar excepción (Req 5)
        data = Hotel._load_data()
        self.assertEqual(data, {})

if __name__ == '__main__':
    unittest.main()