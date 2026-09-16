import math
a = float(input("Введіть дійсне число а (a!=0): "))
n = int(input("Введіть натуральне число n: "))
S = 0
while n >= 1:
    S+=math.log(math.fabs(a**n))
    n-=1

print("Сума={0}".format(S))
