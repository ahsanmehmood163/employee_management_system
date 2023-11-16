from hr import PayrollSystem
from productivity import *
from contacts import AddressBook


class Employee:
    def __init__(self, id, name, address, role, payroll):
        self.id = id
        self.name = name
        self.address = address
        self.role = role
        self.payroll = payroll
        
    def work(self, hours):
        duties = self.role.perform_duties(hours)
        print(f'Employee {self.id} - {self.name}:')
        print(f'- {duties}')
        print('')
        self.payroll.track_work(hours)

    def calculate_payroll(self):
        return self.payroll.calculate_payroll()
        
# class Manager(Employee, ManagerRole, SalaryPayroll):
#     def __init__(self, id, name, weekly_salary):
#         # MRO
#         SalaryPayroll.__init__(self, weekly_salary)
#         super().__init__(id, name)

# class Secretary(Employee, SecretaryRole, SalaryPayroll):
#     def __init__(self, id, name,weekly_salary):
#         # MRO
#         SalaryPayroll.__init__(self, weekly_salary)
#         super().__init__(id, name)
        
# class SalesBoy(Employee, SalesRole, ComisssionPayroll):
#     def __init__(self, id, name, weekly_salary, comission):
#         # MRO
#         ComisssionPayroll.__init__(self, weekly_salary, comission)
#         super().__init__(id, name)
        
# class FactoryPerson(Employee, FactoryPersonRole, HourlyPayroll):
#     def __init__(self, id, name, work_hours, pay_per_hour):
#         HourlyPayroll.__init__(self, work_hours, pay_per_hour)
#         super().__init__(id, name)

# #Multiple Inheritance
# class TemporarySecretary(Employee, SecretaryRole, HourlyPayroll): #--Warning shows because HourlyPayroll and SecretaryRole is inherited from staric(*)
#     def __init__(self, id, name, work_hours, pay_per_hour):
#         HourlyPayroll.__init__(self, work_hours, pay_per_hour)
#         super().__init__(id, name)
        
        
        
        
        
class EmployeeDatabase:
    def __init__(self):
        self._employees = [
            {
                'id' : 1,
                'name' : 'James',
                'role' : 'manager'
                },
            {
                'id' : 2,
                'name' : 'Norie',
                'role' : 'secretary'
                },
            {
                'id' : 3,
                'name' : 'Barbie',
                'role' : 'factory'
                },
            ]
        self.productivity = ProductivitySystem()
        self.payroll = PayrollSystem()
        self.employee_address = AddressBook()
    
    @property
    def employees(self):
        return [self._create_employee(**data) for data in self._employees]
    
    def _create_employee(self, id, name, role):
       address = self.employee_address.get_employee_address(id)
       employee_role = self.productivity.get_role(role)
       payroll_policy = self.payroll.get_policy(id)
       return Employee(id, name, address, employee_role, payroll_policy)
    