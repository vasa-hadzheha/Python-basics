
base=open("Meloman dict.txt",'r',encoding='latin_1')
search=open("result.txt",'w',encoding='latin_1')
searching=input("Введіть назву пісні: ")
for line in base:
    if searching in line:
        print(line.strip())
        search.write(line)
    # else:
    #     print("Нічого не знайдено")    ЗАЦИКЛЮЄ ПОВІДОМЛЕННЯ
print("Done")

base.close()
search.close()




