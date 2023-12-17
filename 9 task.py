def mc(x, n):
    resultat = 0
    for i in range(n+1):
        resultat += (x**i) / factor(i)
    return resultat

def factor(n):
    if n == 0:
        return 1
    else:
        return n * factor(n-1)

x = float(input("Введите значение x: "))
n = int(input("Введите количество членов ряда: "))
result = mc(x, n)
print("Результат вычисления ряда Маклорена:", result)

