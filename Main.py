import pickle, numpy
from statistics import mode
from functools import reduce as rd
import operator

dur=10 # song duration
offs=120 # song offset
K=10 # K in KNN

#dur=int(input('input durasi testing :'))
#offs=int(input('input offset testing :'))
#K=int(input('input K testing :'))

train=numpy.array(pickle.load(open('databin/latih'+str(offs)+str(dur)+'.p','rb')))
test=numpy.array(pickle.load(open('databin/uji'+str(offs)+str(dur)+'.p','rb')))
class=pickle.load(open('databin/songclass.p','rb'))

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
    distance=[[cros_corr(x[i],uji[i]) for i in range(4)] for x in train]
    distance=[[4-sum(x),y[4]] for x,y in zip(distance,train)]

    distance=[distance[i]+[class[x[1]]] for i,x in enumerate(distance) if x[1] in class]
    distance.sort(key=lambda x:x[0])

    result={'Hip Hop':[0,0],'Pop':[0,0],'Electronic':[0,0],'Rock':[0,0],'Jazz':[0,0]}
    for x in distance[:K]:
        if x[2] in result:
            result[x[2]][0]+=1
            result[x[2]][1]+=x[0]

    try:
        return [mode([x[2] for x in distance[:K]])]
    except:
        return [min([v[1],k] for k,v in result.items() if v[0]==max(v[0] for v in result.values()))[1]]

def Main():
    index=int(input('Choose index song:'))
    printHasil(test,index-1)
    #Pengujian()

def Pengujian(): # Confusion Matrix Multiclass Problem
    cmmp=[x[4:]+init(x) for x in test]
    #pickle.dump(cmmp,open('databin/hasil'+str(offs)+str(dur)+str(K)+'.p','wb'))
    cmmp=[x for x in cmmp if x[2] == x[1]]
    print(len(cmmp))

def printHasil(cmmp,i):
    print('\nduration:'+str(dur)+'\toffset:'+str(offs)+'\tK:'+str(K))
    print('Song\t\t: '+cmmp[i][4])
    print('Actual\t\t: '+cmmp[i][5])
    print('Predicted\t: '+init(test[i])[0])

def printLagu():
    for i,x in enumerate(test):
        print('{} : {}'.format(i+1,x[4]))

train,test=minmax(train,test)
if input('Show Song List? (y/n) :')=='y':printLagu()
test=[test[i]+[class[x[4]]] for i,x in enumerate(test) if x[4] in class]
Main()