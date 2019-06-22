import pickle, numpy
from statistics import mode
from functools import reduce as rd
import operator

dur=10
offs=60
K=5
data=numpy.array(pickle.load(open('databin/latih'+str(offs)+str(dur)+'.p','rb')))
tes=numpy.array(pickle.load(open('databin/uji'+str(offs)+str(dur)+'.p','rb')))
kelas=pickle.load(open('databin/songclass.p','rb'))

def cros_corr(train,test):
    return sum([a*b for a,b in zip(train,test)])/numpy.sqrt(sum([a**2 for a in train]) * sum([a**2 for a in test]))

def minmax(train,test):
    norm=numpy.concatenate((train,test))
    temp=[numpy.concatenate((x),axis=None) for x in numpy.transpose(norm)]
    mean=[numpy.mean(x) for x in temp[:4]]
    std=[numpy.std(x) for x in temp[:4]]
    form=lambda a,i:(a-mean[i])/std[i]
    train=[[form(b[a],a) for a in range(4)]+[b[4]] for b in train]
    test=[[form(b[a],a) for a in range(4)]+[b[4]] for b in test]
    return train,test

def init(uji):
    a=[[cros_corr(x[i],uji[i]) for i in range(4)] for x in data]
    a=[[4-sum(x),y[4]] for x,y in zip(a,data)]

    a=[a[i]+[kelas[x[1]]] for i,x in enumerate(a) if x[1] in kelas]
    a.sort(key=lambda x:x[0])

    res={'Hip Hop':[0,0],'Pop':[0,0],'Electronic':[0,0],'Rock':[0,0],'Jazz':[0,0]}
    for x in a[:K]:
        if x[2] in res:
            res[x[2]][0]+=1
            res[x[2]][1]+=x[0]

    test=[[v[0],k] for k,v in res.items()]
    test.sort(reverse=True)

    #print([x[:2] for x in a[:K]])

    try:
        return [mode([x[2] for x in a[:K]])]
    except:
        return [min([v[1],k] for k,v in res.items() if v[0]==max(v[0] for v in res.values()))[1]]

def Main():
    z=[tes[i]+[kelas[x[4]]] for i,x in enumerate(tes) if x[4] in kelas]
    z=[x[4:]+init(x) for x in z]
    z=[x for x in z if x[2] == x[1]]
    print(len(z))

data,tes=minmax(data,tes)
Main()