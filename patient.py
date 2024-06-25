class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Patient(Person):
    def __init__(self, name, age, gender, patient_id, illness, admitted_date, room_number):
        super().__init__(name, age, gender)
        self.patient_id = patient_id
        self.illness = illness
        self.admitted_date = admitted_date
        self.room_number = room_number

    def __str__(self):
        return (f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, "
                f"Gender: {self.gender}, Illness: {self.illness}, Admitted Date: {self.admitted_date}, Room: {self.room_number}")
