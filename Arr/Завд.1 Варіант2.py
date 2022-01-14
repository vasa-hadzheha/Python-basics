n = int(input("Введіть кількість чисел: "))

x = [float(input("Введіть х{0}:".format(i+1))) for i in range(n)]

print("Послідовність чисел: {0}".format(x))
d=1
for el in range(len(x)):
    d*=x[el]
print("Добуток чисел= {0}".format(d))
if d>0:
    g=d**(1/n)
    print("Середнє геометричне {0}".format(g))
else:
    print("Середнього геометричного немає, оскільки добуток від'ємний")
