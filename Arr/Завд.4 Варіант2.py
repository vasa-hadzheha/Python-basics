n = int(input("Введіть кількість елементів масиву: "))

k = [float(input("{0}-ий елемент: ".format(i+1))) for i in range(n)]

print("Ваш масив:",k)

v = sorted(k,reverse=True)

print("Впорядкування за спаданням:",v)