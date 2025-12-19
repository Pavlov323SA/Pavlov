from dataclasses import dataclass

@dataclass(frozen=True)
class Product:
    name: str
    price: float
    weight: float
    is_available: bool
    
    def order_cost(self, quantity):
        return self.price * quantity


if __name__ == "__main__":
    apple = Product("Apple", 15.0, 0.2, True)
    print(apple)
    print(apple.order_cost(10))
