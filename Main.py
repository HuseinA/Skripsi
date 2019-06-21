import pickle, numpy
from statistics import mode
from functools import reduce as rd
import operator

dur=10
offs=30
K=5
data=numpy.array(pickle.load(open('databin/latih'+str(offs)+str(dur)+'.p','rb')))
tes=numpy.array(pickle.load(open('databin/uji'+str(offs)+str(dur)+'.p','rb')))
kelas=pickle.load(open('databin/songclass.p','rb'))

def cros_corr(train,test):
    return sum([a*b for a,b in zip(train,test)])/numpy.sqrt(sum([a**2 for a in train]) * sum([a**2 for a in test]))

def xor(train,test):
    return len([True for a,b in zip(train,test) if a is b])

def distance(train,test):
    return [cros_corr(train[i],test[i]) for i in range(4)]

def minmax(train,test):
    norm=numpy.concatenate((train,test))
    temp=[numpy.concatenate((x),axis=None) for x in numpy.transpose(norm)]
    mn=[min(x) for x in temp[:4]]
    mx=[max(x) for x in temp[:4]]
    form=lambda a,i:(a-mn[i])/(mx[i]-mn[i])
    train=[[form(b[a],a) for a in range(4)]+[b[4]] for b in train]
    test=[[form(b[a],a) for a in range(4)]+[b[4]] for b in test]
    return train,test

def init(uji):
    a=[distance(x,uji) for x in data]
    a=[[4-sum(x),y[4]] for x,y in zip(a,data)]

    a=[a[i]+[kelas[x[1]]] for i,x in enumerate(a) if x[1] in kelas]
    a.sort(key=lambda x:x[0])
    res={'Hip Hop':[0,0],'Pop':[0,0],'Electronic':[0,0],'Rock':[0,0],'Jazz':[0,0],'Classic':[0,0]}
    for x in a[:K]:
        if x[2] in res:
            res[x[2]][0]+=1
            res[x[2]][1]+=x[0]

    test=[[v[0],k] for k,v in res.items()]
    test.sort(reverse=True)

    print([x[:2] for x in a[:K]])

    return [x[1] for x in test[:1]]

def Main():
    z=[tes[i]+[kelas[x[4]]] for i,x in enumerate(tes) if x[4] in kelas]
    z=[x[4:]+init(x) for x in z]
    for x in z:
        print(x[2])
    z=[x for x in z if x[2] == x[1]]
    print(len(z))

data,tes=minmax(data,tes)
Main()