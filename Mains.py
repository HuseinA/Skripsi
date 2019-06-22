import pickle

z=pickle.load(open('databin/hasil1201015.p','rb'))
"""for x in z:
    print(x)
for x in z:
    print(x[2])"""
z=[x for x in z if x[2]==x[1]]
"""print([x[2] for x in z].count('Rock'))
print([x[2] for x in z].count('Hip Hop'))
print([x[2] for x in z].count('Jazz'))
print([x[2] for x in z].count('Pop'))
print([x[2] for x in z].count('Electronic'))"""
print(len(z))
print(z)

"""x=[30,60,90,120]
y=[10,20,30]
k=[5,10,15]

for a in x:
    print('_________________________________________________')
    for b in y:
        for c in k:
            z=pickle.load(open('databin/hasil'+str(a)+str(b)+str(c)+'.p','rb'))
            z=[x for x in z if x[2]==x[1]]
            print('duration:'+str(b)+'\toffset:'+str(a)+'\tK:'+str(c)+'\tHasil:'+str(len(z)))"""
