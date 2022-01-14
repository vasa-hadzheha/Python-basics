import random
rowCount = int(input("кількість рядків ="))
colCount = int(input("кількість елементів ="))

a = [[random.randint(0, 4) for j in range(colCount)] for i in range(rowCount)]
print("Матриця а ={0}".format(a))
# Недороблено-----------------------------------------------------------------
count = 0

f = [0 if 0 in column  else 1 for column  in a ]
print (f)