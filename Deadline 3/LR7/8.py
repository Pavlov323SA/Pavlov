import re

class SnakeCaseMeta(type):
    def __new__(cls, name, bases, dct):
        for attr_name, attr_value in dct.items():
            if callable(attr_value) and not attr_name.startswith('__'):
                if any(char.isupper() for char in attr_name):
                    raise TypeError(f"Метод {attr_name} должен быть написан в snake_case!")
        
        for base in bases:
            for attr_name in dir(base):
                if callable(getattr(base, attr_name)) and not attr_name.startswith('__'):
                    if any(char.isupper() for char in attr_name):
                        raise TypeError(f"Метод {attr_name} должен быть написан в snake_case!")
        
        return super().__new__(cls, name, bases, dct)


if __name__ == "__main__":
    try:
        class GoodCode(metaclass=SnakeCaseMeta):
            def get_data(self):
                pass
            def process_items(self):
                pass
            def valid_method(self):
                pass
        
        print("✓ GoodCode создан успешно")
        
        class BadCode(metaclass=SnakeCaseMeta):
            def GetData(self):
                pass
            def ProcessItems(self):
                pass
        
    except TypeError as e:
        print(f"✗ {e}")
    
    try:
        class InheritedBadCode(GoodCode):
            def BadMethodName(self):
                pass
        
        print("✗ InheritedBadCode создан (не должно быть)")
    except TypeError as e:
        print(f"✓ {e}")
    
    class NormalClass:
        def CamelCaseMethod(self):
            pass
    
    print("\n✓ Класс без метакласса создан (CamelCase разрешён)")