import  math
class Angle:
    def __init__(self,k):
        self.k=k

    def increase(self):
        rad=float(input("Введіть на скільки радіан збільшити кут: "))

        self.k+=math.degrees(rad)
        print(self.k)
        return self.k

    def low(self):
        rad = float(input("Введіть на скільки радіан зменшити кут: "))
        self.k -= math.degrees(rad)
        print(self.k)
        return self.k

new_k=Angle(60)
new_k.increase()
new_k.low()





