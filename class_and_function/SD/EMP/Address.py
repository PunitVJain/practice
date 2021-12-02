
#  stores the address of the EMP
#  params in the address are:
#  1. Street
#  2. near By location
#  3. City/ Villege
#  4. District
#  5. State
#  6. PinCode

class Address:

    def __init__(self, street:str, near_by_location:str, city:str, district:str, pincode:int) -> None:
        self.street = street
        self.near_by_location = near_by_location
        self.city = city
        self.district = district
        self.pincode = pincode
