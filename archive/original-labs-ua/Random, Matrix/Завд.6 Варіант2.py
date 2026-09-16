import random
r=int(input("кількість рядків r="))
e=int(input("кількість елементів e="))
g=[]
a=[[random.randint(-5,20)  for j in range(e)] for i in range(r)]
print(a)

h=[]

for i in range(r):
    h.append(sum([l for l in a[i] if l%2==0 and l>0]))
print(h)

for i in range(r):
    g.append(a[h.index(min(h))])
    h[h.index(min(h))]=10000000
print(g)





