import pickle, numpy
from statistics import mode
import operator

K=5
data=pickle.load(open('databin/latih601.p','rb'))
tes=pickle.load(open('databin/uji601.p','rb'))
kelas=pickle.load(open('man.p','rb'))

def cros_corr(train,test):
    return sum([a*b for a,b in zip(train,test)])/numpy.sqrt(sum([a**2 for a in train]) * sum([a**2 for a in test]))

def xor(train,test):
    return len([True for a,b in zip(train,test) if a is b])

def CC(train,test,mn,mx):
    a=xor(train[0],test[0])
    b=[cros_corr(train[i+1],test[i+1]) for i in range(3)]
    print(a,b,train[4])
    return [4-sum([(a-mn)/(mx-mn)]+b),train[4]]

def init(uji):
    temp = [xor(x[0], uji[0]) for x in data]
    mn, mx = min(temp), max(temp)
    a=[CC(x,uji,mn,mx) for x in data]
    for i,x in enumerate(a):
        if x[1] in kelas:
            a[i]+=[kelas[x[1]]]
    a.sort(key=lambda x:x[0])

    res={'Hip Hop':[0,0],'Pop':[0,0],'Electronic':[0,0],'Rock':[0,0],'Jazz':[0,0]}
    for x in a[:K]:
        if x[2] in res:
                res[x[2]][0]+=1
                res[x[2]][1]+=x[0]
    try:
        return [x for x in a[:K]]
    except:
        return min([v[1],k] for k,v in res.items() if v[0]==max(v[0] for v in res.values()))[1]

def Main():
    #for x in tes:
    #    print(init(x))
    return [(x[4],init(x)) for x in tes]

print(data[6])
