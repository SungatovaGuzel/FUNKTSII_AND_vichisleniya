def f(g):
	if g==1:
		return 1
	return g*f(g-1)
n=int(input("Введите число: "))
x=float(input('Введите вещественное число:'))
ch=0
for k in range(1,n+1):
	ch+=f(k)*x**k
print(ch)
