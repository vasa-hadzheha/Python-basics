import copy
import math
class Rectangle:
    def __init__(self, *args):
        arguments_count = len(args)
        if arguments_count == 0:
            self.a = 0
            self.b = 0
        elif arguments_count == 1:
            if type(args[0]) == int or type(args[0]) == float:
                self.a = args[0]
                self.b = args[0]
            elif type(args[0]) == str:
                arg_list = args[0].split(' ')
                if len(arg_list) == 1:
                    self.a = float(arg_list[0])
                    self.b = self.a
                elif len(arg_list) == 2:
                    self.a = float(arg_list[0])
                    self.b = float(arg_list[1])
                else:
                    raise Exception("arguments are incorrect")
        elif arguments_count == 2:
            self.a = args[0]
            self.b = args[1]
        else:
            raise Exception("arguments are incorrect")

    def copy_f(self, old_rectangle, new_rectangle):
        new_rectangle = copy.deepcopy(old_rectangle)
        return new_rectangle

    def input(self):
        self.a =float(input("Введіть сторону прямокутника - а=: "))
        self.b =float(input("Введіть сторону прямокутника - b=: "))
        print("Сторона а={0}, сторона b={1}".format(self.a, self.b))
        return self.a, self.b

    def str(self):
        return str(self.a, self.b)
    @property
    def repr(self):
        return self.a, self.b

    def s(self):
        s = self.a * self.b
        print("Площа= {0}".format(s))
        return s

    def p(self):
        p =2 * (self.a + self.b)
        print("Периметр= {0}".format(p))
        return 2 * (self.a + self.b)

    def __eq__(self, other_rectangle):
        print("eqql")
        return self.s() < other_rectangle.s() #-------------- не повертає площу

    def __add__(self, other):
        return Rectangle(self.a+other.a,self.b+other.b)

    def __sub__(self, other):
        return Rectangle(math.fabs(self.a - other.a), math.fabs(self.b - other.b))


    def __mul__(self, other):
        return  Rectangle(self.a*math.fabs(other),self.b*math.fabs(other))


class Paralelepiped(Rectangle):

    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h

    def v(self):
        return super().s() * self.h




rec1=Rectangle(3,8)
rec2=Rectangle(4)
# rec1.p
# rec2.s      НЕ РАХУЄ ПЛОЩУ ТА ПЕРИМЕТР!!!
rec3=rec1+rec2
print(rec3.repr)
rec4=rec1 - rec2
print(rec4.repr)
rec5=rec2*2
print(rec5.repr)
rec1=rec2
if rec1==rec2:
    print("Прямокутники рівні!!!")
else:
    print("Прямокутники не рівні!!!")


p=Paralelepiped(4,3,6)
print("v=",p.v())


