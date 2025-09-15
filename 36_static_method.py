class Employee:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manger", "Cashier", "Cook", "Janitor"]
        return position in valid_position
    
employee1 = Employee("Eungune", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongbob", "Cook")

print(Employee.is_valid_position("Cook"))
print(employee1.get_info())