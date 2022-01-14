import random
rowCount = int(input("кількість рядків ="))
colCount = int(input("кількість елементів (стовпців) ="))

a = [[random.randint(0, 4) for j in range(colCount)] for i in range(rowCount)]
print("Матриця а ={0}".format(a))

count = 0
for j in range(colCount):  # для кожного стовпця з номером j
    # визначити чи у стовпці нулі
    is_zero = False
    for i in range(rowCount):  # переглянути усі елементи у стовпці
        if a[i][j] == 0:
            is_zero = True
            break
    if is_zero == False:
        count += 1

print(count)


