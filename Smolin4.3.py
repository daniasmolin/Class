class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Співробітник: {self.name} | Посада: {self.position} | Зарплата: {self.salary:.2f} грн"


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Співробітника '{employee.name}' додано до відділу '{self.name}'.")

    def remove_employee(self, name):
        for emp in self.employees:
            if emp.name.lower() == name.lower():
                self.employees.remove(emp)
                print(f"Співробітника '{name}' видалено з відділу '{self.name}'.")
                return
        print(f"Співробітника '{name}' не знайдено у відділі.")

    def calculate_total_salary(self):
        return sum(emp.salary for emp in self.employees)

    def display_department(self):
        if not self.employees:
            print(f"Відділ '{self.name}' порожній.")
            return
        print(f"\n--- ВІДДІЛ: {self.name} ---")
        for emp in self.employees:
            print(emp)
        print(f"Загальна заробітна плата відділу: {self.calculate_total_salary():.2f} грн")
        print("------------------------\n")



dept = Department("IT-відділ")

emp1 = Employee("Олександр", "Python Developer", 50000.0)
emp2 = Employee("Марія", "QA Engineer", 35000.0)
emp3 = Employee("Іван", "Project Manager", 45000.0)

dept.add_employee(emp1)
dept.add_employee(emp2)
dept.add_employee(emp3)

dept.display_department()

dept.remove_employee("Марія")

dept.display_department()