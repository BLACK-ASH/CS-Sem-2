from scipy import integrate
a = lambda y, x: x*y**2
b = lambda x: 1
c = lambda x: -1
print(integrate.dblquad(a, 0, 2, b, c))