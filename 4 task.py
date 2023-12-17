n=int(input("Введите число: "))
ch=0
for i in range(1,n+1):
	ch+=2**i
print(ch)
