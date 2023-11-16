class Address:
    def __init__(self, street, city, state, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        
    def __str__(self):
        address = [self.street]
        
        address.append(f'\t{self.city}, {self.state} {self.zipcode}')
        return '\n'.join(address)
    
    
class AddressBook:
    def __init__(self):
        self._employee_address = {
            1: Address('121 Admin Rd.', 'Concord', 'NH', '03301'),
            2: Address('67 Paperwork Ave', 'Manchester', 'NH', '03101'),
            3: Address('59 Doman Street', 'New York', 'NH', '03891')
            }
        
    def get_employee_address(self, employee_id):
        address = self._employee_address.get(employee_id)
        if not address:
            raise ValueError('Invalid ID -- Having No Address')
        return address