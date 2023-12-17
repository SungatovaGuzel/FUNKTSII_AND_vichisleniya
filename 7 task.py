import math

def calculate(x, precision):
    result = 1
    term = 1
    n = 1
    
    while abs(term) > precision:
        term *= x / n
        result += term
        n += 1
    
    return result

x = float(input("Введите значение x: "))
precision = float(input("Введите значение точности: "))

result = calculate(x, precision)
print("Значение e^x с точностью", precision, "равно", result)
