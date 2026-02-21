class Reservation:
    """Class representing a Reservation abstraction."""
    def __init__(self, reservation_id, customer_id, hotel_id):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def create_reservation(self):
        pass

    def cancel_reservation(self):
        pass