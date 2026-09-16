r=int(input("кількість рядків r="))
e=int(input("кількість елементів e="))
a = [[float(input("a[{0}][{1}]=".format(i,j))) for j in range(e)] for i in range(r)]
print("Матриця а = {0}".format(a))
import random
b = [[random.randint(1,100)for j in range(e)] for i in range(r)]
print("Матриця b={0}".format(b))
for i in range(r):
    for j in range(e):
        if a[i][j]==0:
            a[i][j]=b[i][j]
print("Матриця а із заміненими нульовими елементами ={0}".format(a))
