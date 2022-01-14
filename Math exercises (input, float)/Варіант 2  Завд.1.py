a=float(input("Введіть довжину першої сторони: "))
b=float(input("Введіть довжину другої сторони: "))
c=float(input("Введіть довжину третьої сторони: "))

import math

if math.fabs(b-c)<a<b+c:
    p=float((a+b+c)/2)      #Півпериметр
    S=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Площа трикутника={0}".format(S))
else:
    print("Даний об'єкт не є трикутником")