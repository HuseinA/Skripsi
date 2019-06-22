import pickle

z=pickle.load(open('databin/hasil301015.p','rb'))
for x in z:
    print(x)
for x in z:
    print(x[2])
z=[x for x in z if any(y in x[2] for y in x[1])]
print(len(z))
print(z)

"""import pickle
x=[30,60,90,120]
y=[10,20,30]
k=[5,10,15]

for a in x:
    print('_________________________________________________')
    for b in y:
        for c in k:
            z=pickle.load(open('databin/hasil'+str(a)+str(b)+str(c)+'.p','rb'))
            z=[x for x in z if any(y in x[2] for y in x[1])]
            print('duration:'+str(b)+'\toffset:'+str(a)+'\tK:'+str(c)+'\tHasil:'+str(len(z)))"""
