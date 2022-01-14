n = int(input("Вкажіть вимір вектора: "))

x = [float(input("Задайте {0}-координату вектора: ".format(i+1))) for i in range(n)]

print("Вектор х=",x)

a = float(input("Введіть множник: "))

d = [ el*a for el in x]

print("Добуток вектора x на число= {0}".format(d))