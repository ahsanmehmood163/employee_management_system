#Productivity System -- Roles
class ManagerRole:
    def perform_duties(self, hours):
        return f'yells for {hours} hours.'
    
class SecretaryRole:
    def perform_duties(self, hours):
        return f'do paper work for {hours} hours.'
    
class SalesRole:
    def perform_duties(self, hours):
        return f'take orders for {hours} hours on phone.'
    
class FactoryPersonRole:
    def perform_duties(self, hours):
        return f'make products for {hours} hours.'
    
    
    
    
    
class ProductivitySystem:
    def __init__(self):
        self._roles = {
            'manager' : ManagerRole,
            'secretary' : SecretaryRole,
            'sales' : SalesRole,
            'factory' : FactoryPersonRole
            }
    
    def get_role(self, role_key):
        role_type = self._roles.get(role_key)
        if not role_type:
            raise ValueError('Invalid Role')
        return role_type()
        
    def track_system(self, employees, hours):
        print('Tracking Productivity Of Employee')
        print('---------------------')
        for employee in employees:
            print(employee.work(hours))
        print('')
