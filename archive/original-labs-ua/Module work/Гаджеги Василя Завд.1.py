import copy
import math
class TCircle:

    def __init__(self, *args):
        arguments_count=len(args)
        if arguments_count==0:
            self.radius=0
        elif arguments_count==1:
            if type(args[0])==int or type(args[0])==float:
                self.radius=args[0]
            elif type(args[0])==str:
                arg_list=args[0].split(' ')
                if len(arg_list)==1:
                    self.radius=float(arg_list[0])
            else:
                raise Exception("Неправильний аргумент!!!")
        elif arguments_count==1:
            self.radius=args[0]
        else:
            raise Exception("Неправильний аргумент!!!")

    @classmethod
    def from_tcircle(cls, class_instance):
        radius = copy.deepcopy(class_instance.radius)
        return cls(radius)

    def input(self):
        self.radius=int(input("Введіть радіус кола: "))
        print("Ваш радіус = {0}".format(self.radius))
        return self.radius

    def str(self):
        return str(self.radius)

    def repr(self):
        return self.radius


    def S_circle(self):
        s=math.pi*(self.radius)**2
        print("Радіус кола= {0}".format(s))
        self.s=s
        return s                           # Не зберігає s --------------------------------------

    def len_circle(self):
        l=2*math.pi*self.radius
        print("Довжина кола= {0}".format(l))
        return l

    def __eq__(self, other_circle):
        # print("eqql")
        return self.s() < other_circle.s()

    def __add__(self, other):
        return TCircle(other.radius + self.radius)

    def __sub__(self, other):
        return TCircle(math.fabs(other.radius - self.radius))

    def __mul__(self, other):
        return TCircle(other * self.radius)


c1=TCircle(60)
c2=TCircle(90)
c1.S_circle()
c1.len_circle()

c3=c1+c2
print(c3.repr())

c4=c2-c1
print(c4.repr())

mu=c1*3
mu.str()
c5 = copy.deepcopy(c1)
print(c5.repr())
c1=c2
if c1==c2:
    print("Кола рівні")

class Cone(TCircle):

    def __init__(self,radius,h):
        super().__init__(self,radius)
        self.h=h


    def V(self):
        return super().s()*self.h *(1/3)



con=Cone(30,6)
print("v=",con.V())


