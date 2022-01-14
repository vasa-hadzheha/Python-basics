import random
class Prism:
    def __init__(self,count_sides,high):
        self.count_sides=count_sides
        self.high=high

    def sides_len(self):
        sides=[random.randint(3,20) for i in range(self.count_sides)]
        print("Сторони багатокутника: ",sides)
        return sides

    def S(self):







