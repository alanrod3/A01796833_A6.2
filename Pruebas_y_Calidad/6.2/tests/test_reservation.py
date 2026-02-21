import unittest
from Pruebas_y_Calidad.6.2.source.reservation import Reservation

class TestReservation(unittest.TestCase):
    def test_create_and_cancel_reservation(self):
        res_id = "R777"
        Reservation.create_reservation(res_id, "CUST01", "HOTEL01")
        data = Reservation._load_data()
        self.assertTrue(any(r['res_id'] == res_id for r in data))
        
        Reservation.cancel_reservation(res_id)
        data_after = Reservation._load_data()
        self.assertFalse(any(r['res_id'] == res_id for r in data_after))

if __name__ == '__main__':
    unittest.main()