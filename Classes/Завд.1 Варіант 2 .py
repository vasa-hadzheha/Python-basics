import math
class Vector:
    n=[]
    def __init__(self, vector_space=0, coordinates=0):
        self.vector_space = vector_space
        self.coordinates = coordinates


    def inp(self, vector_space):
        self.vector_space=vector_space
        # vector_space = int(input("Введіть вимір вектора:"))
        self.coordinates = [float(input("Координати вектора x{0}: ".format(i+1))) for i in range(vector_space)]

    def print_vector(self):
        print("Ваш вектор:{0} ".format(self.coordinates))


    def vector_fab(self):
        b=[el**2 for el in self.coordinates]
        s=sum(b)
        fab = math.sqrt(s)
        print("Довжина вектора= {0}".format(fab))
        return fab
    def norm(self,fab):
        # n=[el/fab for el in self.coordinates]

        for i in range(self.vector_space):
            el= float(self.coordinates[i]/fab)
            self.n.append(el)
        print("Нормування вектора ={0}".format(self.n))


a = Vector()
a.inp(4)
a.print_vector()
f=a.vector_fab()

Vector.norm(a,f)