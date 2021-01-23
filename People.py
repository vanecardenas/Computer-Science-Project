from Address import Address


class Person:
    def __init__(self, name, phone_num, address):
        self.name = name
        self.phone_num = phone_num
        self.address = Address(**address)


class Patient(Person):  # Patients inherits from the class Person
    def __init__(self, age, gender, insurance_num, insurance, contact_person, comorbidities, allergies, **kwargs): # kwargs means the rest
        super().__init__(**kwargs) # Referencing the Person.__init__
        self.age = age
        self.gender = gender
        self.insurance_num = insurance_num
        self.insurance = insurance
        self.contact_person = Person(**contact_person)
        self.comorbidities = comorbidities
        self.allergies = allergies
