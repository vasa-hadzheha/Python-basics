def add_good(base_of_goods,name_of_good):                #Якщо ім'я є у словнику то ми додамо товар, якщо ні то створимо новий
    good_in_base = name_of_good in base_of_goods
    n=1

    if good_in_base==True:
        count = int(input("Введіть кількість завезеного товару ,{0},: ".format(name_of_good)))
        base_of_goods[name_of_good]["кількість"]+=count
    else:
        print("Такого товару немає!!!")
        count_of_new_goods = int(input("Введіть кількість видів нового товару: "))
        while n<=count_of_new_goods:
            name_of_good=input("Введіть назву нового товару: ")
            measurement =input("Введіть одиницю виміру: ")
            count =int(input("Введіть кількість даного товару: "))

            new_good={name_of_good:{"од.виміру":measurement,"кількість":count}}
            print("Ви додали: ",new_good)
            base_of_goods.update(new_good)
            n+=1
        # print("Оновлена база товарів:", base_of_goods)
        return base_of_goods


def del_good(base_of_goods,ship_the_goods=0):  #ship_the_goods- відвантажений товар (якщо він не вказаний то товар удалятиметься
    if ship_the_goods==0:
        name_of_good = input("Введіть назву товару для видалення: ")
        good_in_base = name_of_good in base_of_goods

        if good_in_base==True:
            print("Ви видалили:-{0}".format(base_of_goods[name_of_good]))
            del base_of_goods[name_of_good]
        else:
            print("Такого товару немає!!!")
        return base_of_goods
    else:
        name_of_good = input("Введіть назву товару для відвантаження: ")
        good_in_base = name_of_good in base_of_goods

        if good_in_base == True:
            count = int(input("Введіть кількість відвантаженого товару: "))
            base_of_goods[name_of_good]["кількість"] -= count
            print("Ви видалили:{0}-{1} -одиниць".format(base_of_goods[name_of_good],count))
            return base_of_goods
        else:
            print("Такого товару немає!!!")


base_of_goods={'Молоко':{"од.виміру":'пак.',"кількість":10},'Хліб':{"од.виміру":"шт.","кількість":6},
'Сіль':{"од.виміру":'пак.',"кількість":13},'Кола':{"од.виміру":"банок","кількість":15}}

for key, value in base_of_goods.items():     # Виводить кожний елемент словника в новому рядку
    print(key, '\n', value,'\n')

# base_of_goods['Молоко']["кількість"]+=2
# base_of_goods["м'ясо"]={"од.виміру":'кг.',"кількість":45}


add_good(base_of_goods,"Шоколад")
del_good(base_of_goods)

print("Оновлена база товарів:")
for key, value in base_of_goods.items():
    print(key, '\n', value,'\n')



