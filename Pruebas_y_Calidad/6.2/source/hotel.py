class Hotel:
    """Class representing a Hotel abstraction."""
    def __init__(self, hotel_id, name, location, total_rooms):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.total_rooms = total_rooms
        self.available_rooms = total_rooms

    def create_hotel(self):
        pass

    def delete_hotel(self):
        pass

    def display_information(self):
        pass

    def modify_information(self):
        pass