import json
from People import Patient
from Sensor import Sensor
from EmergencyService import EmergencyService


def load_patient():
    with open("patient_data.json", "r") as patient_file:
        patient_data = json.load(patient_file) # patient_data is a dictionary
    patient = Patient(**patient_data)
    print(f"Patient Data for {patient.name} was loaded successfully.")
    return patient


def greet_patient(patient):
    if patient.gender == "male":
        title = "Mr."
    else:
        title = "Mrs."
    print(f"Hello {title} {patient.name}!")
    print("Welcome to your Heart-Companion, we will now enter the monitoring mode.")


def monitor_patient(patient):
    sensor = Sensor(patient.comorbidities)
    emergency_vital_sign_report = sensor.detect_emergency()
    return emergency_vital_sign_report


def call_ambulance(patient, emergency_vital_sign_report):
    emergency_service = EmergencyService()
    emergency_service.call_ambulance(patient, emergency_vital_sign_report)


def run():
    patient = load_patient()
    greet_patient(patient)
    emergency_vital_sign_report = monitor_patient(patient)
    call_ambulance(patient, emergency_vital_sign_report)


if __name__ == "__main__":
    run()
    