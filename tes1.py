import numpy
from functools import reduce as rd
import pickle

z=pickle.load(open('databin/latih3010.p','rb'))

a=numpy.array([[[1,1,1],2,3],[[4,4,4],5,6],[[7,7,7],8,9]])

b=[2,4]
c=[3,6]
d=lambda x,y:x+y
print(rd(d,a))
a=numpy.transpose(a)
print(a[0])
print(rd(d,a[0]))
print(len(z[0][0]))
print(numpy.std(z[1][3]))