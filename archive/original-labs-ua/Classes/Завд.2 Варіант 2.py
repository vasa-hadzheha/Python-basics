#Завдання 2 варіант 11
import math
class Telephone_tariff:
    sum=0
    def __init__(self,name,start_date,end_date,tariff_price,m_price):
        self.name=name
        self.start_date=start_date
        self.end_date=end_date
        self.tariff_price=tariff_price
        self.m_price=m_price

    def end_of_tariff(self):
        time_of_using=int(input("Введіть кількість днів користування тарифом: "))
        to_end=self.end_date-((self.start_date+time_of_using)%31)
        if to_end>0:
            print("До закінчення дії тарифу {0} днів.".format(to_end))
        else:
            print("Дія тарифу закінчилась {0} днів тому".format(math.fabs(to_end)))
        return to_end
    def price_of_call(self):
        time_of_call=int(input("Введіть скільки хвилин говоритимете: "))
        price_of_call=time_of_call*self.m_price
        self.sum += price_of_call
        print("Вартість дзвінка:{0:.2f}.грн".format(price_of_call))
        return  price_of_call
    def sum_abon(self):
        print("Сума сплаченої абонплати={0:.2f}.грн".format(self.sum))


t=Telephone_tariff("Kyivstar",23,15,75,2.50)

print(t.end_of_tariff())
print(t.price_of_call())
print(t.price_of_call())
print(t.sum_abon())

