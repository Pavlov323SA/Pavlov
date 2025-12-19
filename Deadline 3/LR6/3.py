class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, number):
        return number * self.factor


if __name__ == "__main__":
    by_5 = Multiplier(5)
    print(by_5(10))
    print(by_5(2))