from person import Person

class Doctor(Person):
    def __init__(self, name, age, gender, doctor_id, specialization):
        super().__init__(name, age, gender)
        self.doctor_id = doctor_id
        self.specialization = specialization

    def __str__(self):
        return f"Doctor ID: {self.doctor_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Specialization: {self.specialization}"
