#Визначити суму додатних елементів матриці з першим парним і другим непарним індексами.
import random

r=int(input("кількість рядків r="))
e=int(input("кількість елементів e="))

a=[[random.randint(-10,20)  for j in range(e)] for i in range(r)]

b=[]
for row in a:
    row_str=['{0:5d}'.format(el) for el in row]
    b.append(row_str)

b=[''.join([ '{0:7d}'.format(el) for el in row])   for row in a]
print(*b,sep='\n')

s=0
for i in range(0,r,2):
    for j in range(1,e,2):
        if a[i][j]>0:
            s+=a[i][j]
print("сума додатних елементів матриці з першим парним і другим непарним індексами= {0}".format(s))