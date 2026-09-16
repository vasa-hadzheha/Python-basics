import math
def f(x,y):
    if x>0 and y>0:
        g=x**3+(x**2+y**4)**1/2
        return(g)
    elif x>0 and y<0:
        m=(x**2-2*x+(x)**1/2)/(x)**3/5
        return(m)
    else:
        m=math.sin(x*y)
        return (m)

#--------------------------------------
a=float(input('a='))
b=float(input('b='))
print("f(a,b)=",f(a,b))
print("f(2,a)=",f(2,a))
u= f(a,b)+f(2,a)+2
print("U=",u)


