
res=[]
with open("Test2.txt") as f:
    for row in f:       # row= '313 4 52'
        numbers=list(map(float, row.split(' ')))  # ['313','4','52']
        res+=numbers

print(res)
m=max(res)

new_list=[]

for el in res:
    if el==0:
        new_list.append(m)
    else:
        new_list.append(el)

with open("new_data.txt",'w') as f:
    f.write(str(new_list))





