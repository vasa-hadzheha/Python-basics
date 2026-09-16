
class Matrix:

    def __init__(self,count_row,count_column,matrix):
        self.count_row=count_row
        self.count_column=count_column
        self.matrix=matrix

    # def matrix_generation(self):  ЯКЩО ГЕНЕРУВАТИ МАТРИЦЮ ТО ВОНА НЕ ВИКОРИСТОВУЄТЬСЯ У ФУНКЦІЯХ!!!
    #
    #     m=[[float(input("m[{0}][{1}]=".format(i,j))) for j in range(self.count_column)] for i in range(self.count_row)]
    #     return m
    def show_matrix(self):
        # b = []
        # for row in self.matrix:
        #     row_str = ['{0:5d}'.format(el) for el in row]
        #     b.append(row_str)
        #
        # b = [''.join(['{0:7d}'.format(el) for el in row]) for row in  self.matrix()]
        # print("Ваша матриця:",*b, sep='\n')
        return print(self.matrix)

    def __getitem__(self,el):
        for i in range(self.count_row):
            if el in self.matrix[i]==True:
                return el
            else:
                raise Exception("Такого елемента немає!!!")    #Error--не працює

    def __setitem__(self,row_count,column_count, value):
        if row_count in list(self.count_row)==True and column_count in list(self.count_column)==True:
            self.matrix[row_count][column_count]=value
        else:
            raise Exception("Значення введені неправильно!!!")    #Error--не працює

    def __delitem__(self,el):
        for i in range(self.count_row):
            if el in self.matrix[i]==True:
                self.matrix[i].remove(el)
            else:
                raise Exception("Такого елемента немає!!!")     #Error--не працює


    def max(self):
        h=[]
        for i in range(len(self.matrix)):
            l=max(self.matrix[i])
            h+=[l]
        return print(max(h))

    def min(self):
        h = []
        for i in range(len(self.matrix)):
            l = min(self.matrix[i])
            h += [l]
        return print(min(h))


m=[[float(input("m[{0}][{1}]=".format(i,j))) for j in range(3)] for i in range(3)]
d=Matrix(3,3,m)
d.show_matrix()
d.min()
d.max()
# d[100]()
# d[2,1,1000]()
del d[1]

d.show_matrix()