import math
x=float(input("Введіть значення x: "))
n=float(input("Введіть значення n: "))

if x<=n:
    print("y={0}".format(math.log(math.fabs(x))-n))
else:
    print("y={0}".format(math.cos(x*n)))