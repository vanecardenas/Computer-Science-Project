import time

class EmergencyService:
    def __init__(self):
        self.hotline = 112

    def call_ambulance(self, patient, emergency_vital_sign_report):
        print(f"""\n The following data of the patient will be send:
                Name: {patient.name}
                Gender: {patient.gender} 
                Comorbidities: {patient.comorbidities}
                Allergies: {patient.allergies}
                Insurance Number: {patient.insurance_num}
                Insurance Company: {patient.insurance}
        """)
        time.sleep(3) # This is simulating the records processing and fordwarding.
        print(f"Data was successfully sent and the ambulance was called at the phone number: {self.hotline}")
        print(f"It is on the way to the following address: {patient.address.get_complete_address()}")
        time.sleep(3) # This is simulating the contacting of the contact person.
        print(f"\n{patient.contact_person.name} was contacted at the phone number: {patient.contact_person.phone_num}.")
