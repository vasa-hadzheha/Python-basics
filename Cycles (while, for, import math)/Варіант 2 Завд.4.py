n=int(input("Введіть ціле значення n: "))
a = [1,1]
i=2

while i<=n:
    el = a[i-1]+2*(a[i-2])
    a.append(el)
    i+=1

print("Весь список:{0}".format(a))
print("xn={0}".format(el))
