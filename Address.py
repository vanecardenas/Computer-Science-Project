class Address:
    def __init__(self, street, number, city, state, zip_code, country):
        self.street = street
        self.number = number
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country

    def get_complete_address(self):
        return f"""
                {self.street} {self.number} 
                {self.zip_code} {self.city}
                {self.country}"""