from patient import Patient
from doctor import Doctor
from rooms import RoomManager

class HospitalManagementSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.room_manager = RoomManager(total_rooms=10)
        self.add_default_doctors()

    def add_default_doctors(self):
        default_doctors = [
            Doctor("Dr. Meena", 43, "Female", "D001", "Orthopedics"),
            Doctor("Dr. Felix", 35, "Male", "D002", "Cardiology"),
            Doctor("Dr. Johnson", 50, "Male", "D003", "Neurology"),
            Doctor("Dr. Smith", 45, "Female", "D004", "Pediatrics")
        ]
        self.doctors.extend(default_doctors)

    def admit_patient(self, name, age, gender, patient_id, illness, admitted_date):
        room_number = self.room_manager.check_availability()
        if room_number is None:
            print("No rooms available.")
            return
        patient = Patient(name, age, gender, patient_id, illness, admitted_date, room_number)
        self.patients.append(patient)
        self.room_manager.admit_patient_to_room(room_number)
        print(f"Patient {patient.name} admitted successfully to room {room_number}.")

    def display_admitted_patients(self):
        if not self.patients:
            print("No patients admitted.")
        else:
            for patient in self.patients:
                print(patient)

    def display_patient_names(self):
        if not self.patients:
            print("No patients admitted.")
        else:
            for patient in self.patients:
                print(patient.name)

    def discharge_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                self.patients.remove(patient)
                self.room_manager.discharge_patient_from_room(patient.room_number)
                print(f"Patient {patient.name} discharged successfully.")
                return
        print(f"No patient found with ID {patient_id}.")

    def display_doctors(self):
        if not self.doctors:
            print("No doctors available.")
        else:
            for doctor in self.doctors:
                print(doctor)

    def add_doctor(self, name, age, gender, doctor_id, specialization):
        doctor = Doctor(name, age, gender, doctor_id, specialization)
        self.doctors.append(doctor)
        print(f"Doctor {doctor.name} added successfully.")

if __name__ == "__main__":
    hospital = HospitalManagementSystem()

    while True:
        print("\n1) Display patient names who are admitted")
        print("2) Check room availability")
        print("3) Admit a patient")
        print("4) Discharge patient")
        print("5) Display Doctors")
        print("6) Add Doctor")
        print("7) Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            hospital.display_patient_names()
        elif choice == '2':
            room_number = hospital.room_manager.check_availability()
            if room_number is not None:
                print(f"Room {room_number} is available.")
            else:
                print("No rooms available.")
        elif choice == '3':
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            gender = input("Enter patient gender: ")
            patient_id = input("Enter patient ID: ")
            illness = input("Enter patient illness: ")
            admitted_date = input("Enter admitted date (YYYY-MM-DD): ")
            hospital.admit_patient(name, age, gender, patient_id, illness, admitted_date)
        elif choice == '4':
            patient_id = input("Enter patient ID to discharge: ")
            hospital.discharge_patient(patient_id)
        elif choice == '5':
            hospital.display_doctors()
        elif choice == '6':
            name = input("Enter doctor name: ")
            age = int(input("Enter doctor age: "))
            gender = input("Enter doctor gender: ")
            doctor_id = input("Enter doctor ID: ")
            specialization = input("Enter doctor specialization: ")
            hospital.add_doctor(name, age, gender, doctor_id, specialization)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
