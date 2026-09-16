
s=[]
res=[]
with open("Test.txt") as f:
    for row in f:       # row= '313 4 52'
        numbers=list(map(float, row.split(' ')))  # ['313','4','52']
        res+=numbers
    for el in res:
        if el<0:
            s.append(el)
print(res)
print(s)
print("Найбільший елемент серед від’ємних=",max(s))


