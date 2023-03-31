from app import calculate
import random
operation = ()
t = random.randint(0,3)
if t == 0:
    operation = 'add'
elif t == 1:
    operation = 'subtract'
elif t == 2:
    operation = 'multiply'
else:
    operation = 'divide'
def calculate_test(num1, num2):

    if operation == 'add':
        assert calculate(1, 3) == 4
        assert calculate(10, -10) == 0
        assert calculate(20, -100) == 100

    elif operation == 'subtract':
        assert calculate(1, 3) == -2
        assert calculate(10, -10) == 20
        assert calculate(-10, -20) == 10

    elif operation == 'multiply':
        assert calculate(2, 2) == 4
        assert calculate(10, -10) == -100
        assert calculate(-2, -2) == 4

    elif operation == 'divide':
        assert calculate(10, 10) == 1
        assert calculate(-20, 10) == -2
        assert calculate(-50, -10) == 5