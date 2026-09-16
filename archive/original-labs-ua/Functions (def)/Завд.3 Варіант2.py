def g(n):
    a = [9,35]
    i=2
    import math
    while i<=n:
        el = math.sin(a[i-1]+math.cos(a[i-2]))
        a.append(el)
        i+=1
    return(el)
#--------------------------------------------------
h = int(input("h="))
perevirka = g(h)
print(perevirka)
s = g(7)+g(9)
print("S=",s)