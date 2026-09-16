n=int(input("Введіть номер n-го елемента: "))
x1=1
x0=1
for i in range(2,n+1):
    xi = x1+2*x0
    x0=x1
    x1=xi
print("xn={0}".format(xi))
