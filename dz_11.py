
# f(x) = (sin(x)/2 + cos(x)/2) ** 2 * sin(x)
# 1 Определить корни

from cmath import cos, sin
from sympy import *

x = Symbol('x')
func=(sin(x)/2 + cos(x)/2) ** 2 * sin(x)
y=solve(func)
x1=float(y[0])
x2=float(y[1])
print(x1,x2)

# 2 Найти интервалы, на которых функция возрастает

fd=diff(func)
print(solve(0<fd))

# 3 Найти интервалы, на которых функция убывает

print(solve(fd<0))

# 4 Построить график

import matplotlib.pyplot as plt

list_y=[]
for i in range(-5,6):
    x=i
    y=(sin(x)/2 + cos(x)/2) ** 2 * sin(x)
    list_y.append(y)
print(list_y)
plt.plot(range(-5,6),[0,0,0,0,0,0,0,0,0,0,0])
plt.plot(range(-5,6),list_y)

# 5 Вычислить вершину

corni=solve(fd)
top=corni[0]
x=top
y=-12*x**4*sin(cos(x))-18*x**3 + 5*x*+2 + 10*x - 30
print(top,y)

# 6 Определить промежутки, на котором f > 0

solve(0<func)

# 7 Определить промежутки, на котором f < 0

solve(func<0)