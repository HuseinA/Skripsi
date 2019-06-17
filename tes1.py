import numpy
from functools import reduce as rd
a=[[[1,1,1],2,3],[[4,4,4],5,6],[[7,7,7],8,9]]

b=[2,4]
c=[3,6]

d=lambda x,y:x+y

a=numpy.transpose(a)

print(rd(d,a[0]))
