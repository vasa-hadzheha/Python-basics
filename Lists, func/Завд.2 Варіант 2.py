
def add_product(base_of_products):                #Якщо ім'я є у словнику то ми додамо продукт, якщо ні то створимо новий
    name_of_product=input("Введіть назву продукта:" )
    product_in_base = name_of_product in base_of_products
    n=1

    if product_in_base==True:
        count = int(input("Введіть кількість нових продуктів ,{0},: ".format(name_of_product)))
        base_of_products[name_of_product]["наявна кількість"]+=count
    else:
        print("Такого продукта немає!!!")
        count_of_new_products = int(input("Введіть кількість видів нових продуктів: "))
        while n<=count_of_new_products:
            name_of_product=input("Введіть назву нового продукта: ")
            measurement =input("Введіть одиницю виміру: ")
            count =int(input("Введіть кількість даного продукта: "))

            new_product={name_of_product:{"од.виміру":measurement,"кількість":count}}
            print("Ви додали: ",new_product)
            base_of_products.update(new_product)
            n+=1
        return base_of_products

def search_product(base_of_products):

    searching=input("Введіть назву продукта для пошуку: ")
    print(base_of_products.get(searching,"Нічого не знайдено"))

base_of_products={'Молоко':{"од.виміру":'пак.',"наявна кількість":10,"ціна":14.00},'Хліб':{"од.виміру":"шт.","наявна кількість":6,"ціна":13.50},
'Сіль':{"од.виміру":'пак.',"наявна кількість":13,"ціна":7.00},'Кола':{"од.виміру":"банок","наявна кількість":15,"ціна":11.99}}

search_product(base_of_products)
add_product(base_of_products)
search_product(base_of_products)
