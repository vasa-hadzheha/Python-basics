
class Something:

    def result(self):
        x = []
        y = []
        with open("Points.txt") as f:
            for num, row in enumerate(f, 1):  # row= '313 4 52'
                numbers = list(map(float, row.split(' ')))  # ['313','4','52']
                if num == 1:
                    for el in numbers:
                        if el < 0:
                            x.append(el)
                elif num == 2:
                    for el in numbers:
                        if el > 0:
                            y.append(el)

        print("x={0}'\n'y={1}".format(x, y))

        if len(x)>len(y):
            for i in range(len(y)):
                print("Точка-{0} =({1},{2})".format(i+1,x[i],y[i]))

        else:
            for i in range(len(x)):
                print("Точка-{0} =({1},{2})".format(i+1,x[i],y[i]))


r = Something()
r.result()


