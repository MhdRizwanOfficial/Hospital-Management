class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.is_occupied = False

    def occupy(self):
        self.is_occupied = True

    def vacate(self):
        self.is_occupied = False

class RoomManager:
    def __init__(self, total_rooms):
        self.rooms = [Room(i) for i in range(1, total_rooms + 1)]

    def check_availability(self):
        for room in self.rooms:
            if not room.is_occupied:
                return room.room_number
        return None

    def admit_patient_to_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                room.occupy()
                break

    def discharge_patient_from_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                room.vacate()
                break
