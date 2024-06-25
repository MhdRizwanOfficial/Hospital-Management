# Hospital-Management-System

## Overview
The Hospital Management System is a Python-based console application designed to streamline various administrative tasks within a hospital. The system allows the receptionist to efficiently manage patient admissions, check room availability, discharge patients, and display lists of admitted patients and available doctors.

## Features
- **Patient Management**: Admit new patients, display admitted patients, and discharge patients.
- **Room Management**: Check room availability to ensure optimal utilization of hospital resources.
- **Doctor Management**: Maintain a list of available doctors and their specializations.

## Classes and Methods
### `Person`
Base class representing a person with basic attributes:
- `name`
- `age`
- `gender`

### `Patient`
Inherits from `Person` and adds patient-specific attributes:
- `patient_id`
- `illness`
- `admitted_date`
- `room_number`

### `Doctor`
Inherits from `Person` and adds doctor-specific attributes:
- `doctor_id`
- `specialization`
- `available`

### `HospitalManagementSystem`
Manages lists of patients and doctors, and includes methods to:
- `admit_patient(patient)`: Admits a new patient.
- `display_admitted_patients()`: Displays all admitted patients.
- `display_doctors()`: Displays all doctors.
- `add_doctor(doctor)`: Adds a new doctor.
- `discharge_patient(patient_id)`: Discharges a patient by ID.
- `check_room_availability()`: Checks and displays available rooms.

## Usage
1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/Hospital-Management-System.git
   cd Hospital-Management-System
