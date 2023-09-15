class Calculator:
    def __init__(self, x, y):
        self.a = x
        self.b = y

    def __add__(self, other):
        return self.a + other.b

    def __sub__(self, other):
        return self.a - other.b

    def __mul__(self, other):
        return self.a * other.b

    def __truediv__(self, other):
        return self.a / other.b


a = int(input('Enter number1: '))
b = int(input('Enter number2: '))
obj = Calculator(a, b)


choise = 1

while choise != 0:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Truedivision")
    choise = int(input('Enter your choise: '))
    if choise == 1:
        result = obj.__add__(obj)
        print(f"Result:{result}")
    elif choise == 2:
        result = obj.__sub__(obj)
        print(f"Result:{result}")
    elif choise == 3:
        result = obj.__mul__(obj)
        print(f"Result:{result}")
    elif choise == 4:
        result = obj.__truediv__(obj)
        print(f"Result:{result}")
    else:
        print('Selection Error')
