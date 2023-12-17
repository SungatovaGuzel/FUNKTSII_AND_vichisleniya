def square(n, precision):
    x = n
    while True:
        y = (x + n / x) / 2
        if abs(y - x) < precision:
            break
        x = y
    return y

n = float(input("Введите число: "))
precision = float(input("Введите точность: "))

result = square(n, precision)
print(f"Корень из {n} с точностью {precision} равен {result}")
