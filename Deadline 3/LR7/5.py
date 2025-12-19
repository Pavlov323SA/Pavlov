class LoggableMixin:
    def log(self, message):
        print(f"[INFO] {self.__class__.__name__}: {message}")


class Employee(LoggableMixin):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


if __name__ == "__main__":
    emp = Employee("Manager", 50000)
    emp.log("Сотрудник создан")