import math
class Rectangle:

    def __init__(self, *args):
        arguments_count = len(args)
        if arguments_count == 0:  # rect=Rectangle()
            self.a = 0
            self.b = 0
        elif arguments_count == 1:
            if type(args[0]) == int or type(args[0]) == float:  # rect=Rectangle(2)
                self.a = args[0]
                self.b = args[0]
        elif arguments_count == 2:  # rect=Rectangle(3.5,  9)
            self.a = args[0]
            self.b = args[1]
        else:
            raise Exception("arguments are incorrect")

    def S(self):
        s=self.a*self.b
        print("Площа=",s)
        return s

    def P(self):
        p=2*(self.a+self.b)
        print("Периметр=", p)
        return p

    def __eq__(self, other):
        return self.S() < other.S()
    def __add__(self, other):
        return Rectangle(other+self.a,other+self.b)

    def __sub__(self, other):
        return Rectangle(math.fabs(other-self.a),math.fabs(other-self.b))

    def __mul__(self,other):
        return Rectangle(other*self.a,other*self.b)
    @property
    def vyvid(self):
        print(self.a,self.b)
#----------------------------------------------------------------------------------------------
#ДРУГА ЧАСТИНА ЛАБ. №12
    def __getitem__(self, key):
        if key==1:
            return self.a
        elif key==2:
            return self.b
        else:
            raise Exception("Некоректний елемент!!!")    #Error--не працює

    def __setitem__(self, key, value):
        if key == 1:
            self.a=value
        elif key == 2:
            self.b=value
        else:
            raise Exception("Некоректний елемент!!!")    #Error--не працює

    def __delitem__(self, key):
        if key == 1:
           del self.a
        elif key == 2:
           del self.b
        else:
            raise Exception("Некоректний елемент!!!")     #Error--не працює

    def show_sides(self):

        print("Сторoнa a={0}, сторона b={1};".format(self.a,self.b))



rect1=Rectangle(3,7)

print('b=',rect1[2])
rect1[2]=10
print('b=',rect1[2])
del rect1[2]

rect1.show_sides() #показує що елемент був видалений ('Rectangle' object has no attribute 'b')




# rect2=Rectangle(2,3)
# rect1.S()
# rect1.P()
#
# sum= rect1+6
# print(sum.vyvid)
#
# neg=rect1-3
# print(neg.vyvid)
#
# mu=rect1*2
# print(mu.vyvid)
#
# if rect1==rect2:
#     print("rectangles are considered as equal ")
# else:
#     print("Прямокутники не рівні")

