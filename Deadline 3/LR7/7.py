class Vector3D:
    __slots__ = ('x', 'y', 'z')
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


if __name__ == "__main__":
    v = Vector3D(1, 2, 3)
    
    print(f"Координаты: ({v.x}, {v.y}, {v.z})")
    
    try:
        print(v.__dict__)
    except AttributeError as e:
        print(f"✓ __dict__ отсутствует: {e}")
    
    try:
        v.color = "red"
        print("✗ Атрибут color добавлен (не должно быть)")
    except AttributeError as e:
        print(f"✓ Нельзя добавить новый атрибут: {e}")
    
    try:
        v.x = 10
        print(f"✓ Существующий атрибут x изменён: {v.x}")
    except AttributeError as e:
        print(f"✗ Ошибка изменения существующего атрибута: {e}")