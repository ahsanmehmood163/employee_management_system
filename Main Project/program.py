import hr
import contacts
import employees
import productivity
from hr import PayrollSystem
from productivity import ProductivitySystem
from employees import EmployeeDatabase

#salary_employee = employees.SalaryEmployee(1, 'James', 2000)
#hourly_employee = employees.HourlyEmployee(2, 'Norie', 10, 25)
#comission_employee = employees.ComisssionEmployee(3, 'Joe', 1000, 100)

#manager = employees.Manager(1, 'James', 2000)
#secretary = employees.Secretary(2, 'Norie', 1500)
#sales_boy = employees.SalesPerson(3, 'Joe', 1000, 100)
#factory_person = employees.FactoryPerson(4, 'Barbie', 12, 150)
#temporary_secretary = employees.TemporarySecretary(5, 'Maline', 10, 160)

# manager = employees.Manager(1, 'James', 2000)
# manager.address = contacts.Address('11th Street', 'Lahore', 'Punjab', 55239)

# secretary = employees.Secretary(2, 'Norie', 1500)
# secretary.address = contacts.Address('12th Street', 'Faisalabad', 'Punjab', 45891)

# temporary_secretary = employees.TemporarySecretary(5, 'Maline', 10, 160)
# temporary_secretary.address = contacts.Address('01st Street', 'Quetta', 'Balochistan', 35981)

# sales_boy = employees.SalesBoy(3, 'Joe', 1000, 150)
# factory_person = employees.FactoryPerson(4, 'Barbie', 10, 100)

# employees_list = [
#     manager,
#     secretary,
#     sales_boy,
#     factory_person,
#     temporary_secretary
#     ]

productivity_system = ProductivitySystem()
payroll_system = PayrollSystem()
employee_database = EmployeeDatabase()
employees = employee_database.employees
productivity_system.track_system(employees, 40)
payroll_system.calculate_payroll(employees)