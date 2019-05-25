import math
from statistics import mode

def EuclideanDis(tes,train):
    return math.sqrt(sum([(x-train[i])**2 for i,x in enumerate(tes)]))

def hasil(test_data,train_data):
    [train_data[i].append(EuclideanDis(test_data,x)) for i,x in enumerate(train_data)]
    train_data.sort(key=lambda  x: x[5])
    return mode([x[4] for i,x in enumerate(train_data[:3])])
