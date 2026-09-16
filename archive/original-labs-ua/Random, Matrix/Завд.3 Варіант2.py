m = int(input("Введіть вимір вектора (кількість елементів матриці): "))
n=int(input("кількість рядків матриці n="))

x = [float(input("Веідть {0}-у координату вектора: ".format(i+1))) for i in range(m)]
print("Вектор х={0}".format(x))
a = [[float(input("Введіть координати матриці а[{0}][{1}]=".format(i,j))) for j in range(m)] for i in range(n)]
print("Матриця А={0}".format(a))

d = [[a[i][j]*x[j] for j in range(m)] for i in range(n)]
print("Проміжковий результат={0}".format(d))

ax = []
for i in range(n):
    ax+=[sum(d[i])]
print("Добуток матриці на вектор Ax={0}".format(ax))
#не розумію умову задачі "Перевірити, чи виконується рівність Ax=b"
