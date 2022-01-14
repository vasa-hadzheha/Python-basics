import math

x1=float(input("Введіть координати x1: "))  #точ.A
y1=float(input("Введіть координати y1: "))

x2=float(input("Введіть координати x2: "))  #точ.B
y2=float(input("Введіть координати y2: "))

x3=float(input("Введіть координати x3: "))  #точ.C
y3=float(input("Введіть координати y3: "))

#Вектори
#a=(x2-x1;y2-y1)  b=(x3-x2;y3-y2)  c(x3-x1;y3-y1)
#знаходження скалярного добутку векторів

scal_ab=(x2-x1)*(x3-x2)+(y2-y1)*(y3-y2)
scal_ac=(x2-x1)*(x3-x1)+(y2-y1)*(y3-y1)
scal_bc=(x3-x2)*(x3-x1)+(y3-y2)*(y3-y1)

eps=0.000001

if math.fabs(scal_ab)<eps or math.fabs(scal_ac)<eps or math.fabs(scal_bc)<eps:
    print("Трикутник прямокутний")
else:
    print("Трикутник не прямокутний")

