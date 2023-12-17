def f(g):
	if g==1:
		return 1
	return g*f(g-1)
n=int(input("Введите число: "))
ch=0
for i in range(1,n+1):
	ch+=f(i)
print(ch)
