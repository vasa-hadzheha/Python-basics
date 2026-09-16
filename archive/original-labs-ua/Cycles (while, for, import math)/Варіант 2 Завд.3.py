x = float(input("Введіть змінну х (від -1 до1): "))
e = float(input("Введіть точність е: "))

S=0
a=1
import math

while math.fabs((x**a)/a)>e:
    S-=(x**a)/a
    a+=1
print("Сума={0}".format(S))

if math.log(1-x)-S<e:
    print("рівність справедлива S=log(1-x)")
else:
    print ("Рівність не cправедлива")
