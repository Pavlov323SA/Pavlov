class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __setattr__(self, name, value):
        if name == 'age':
            if value < 0:
                print("Нельзя быть младше 0")
                value = 0
        super().__setattr__(name, value)
    
    def __getattr__(self, name):
        return None


if __name__ == "__main__":
    p = Person("Ivan", 30)
    p.age = -5
    print(p.age)
    print(p.name)
    print(p.job)