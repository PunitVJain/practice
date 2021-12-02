# class will take the any number of address of the employee

#  with this code the emp can take any number of address.

from Address import Address


class Employee:

    def __init__(self, firstname:str, lastname:str, address) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.address = []
        if isinstance(address, Address):
            self.address.append(address)
        elif isinstance(address, list):
            for entry in address:
                if not isinstance(address, Address):
                    raise ValueError("Invalid Address.")
            self.address.append(address)
        else:
            raise ValueError("Invalid Address.")
        
    def add_address(self, address):
        if not isinstance(address, Address):
            raise ValueError("Invalid Address.")
        self.address.append(address)

                    

                

        