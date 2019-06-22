import librosa,numpy,pickle
from os import listdir
from os.path import isfile, join

tp='latih'
dur=[10,20,30]
offs=[30,60,90,120]
file=[f for f in listdir('../Music/'+tp+'128kbps') if isfile(join('../Music/'+tp+'128kbps', f))]

def extraction(song,offset,duration):
    hop_length = 256
    frame_length = 512
    x, sr = librosa.load(song, offset=offset, duration=duration)
    zeros = librosa.feature.zero_crossing_rate(x)[0]
    spec_centroid = librosa.feature.spectral_centroid(x, sr=sr)[0]
    spec_rolloff = librosa.feature.spectral_rolloff(x + 0.01, sr=sr)[0]
    energy = numpy.array([sum(x[i:i + frame_length] ** 2)for i in range(0, len(x), hop_length)])
    return [zeros,spec_centroid,spec_rolloff,energy,song[22:-4]]

def run(dur,offs):
    print('databin/'+tp+str(offs)+str(dur)+'.p')
    result=[extraction('../Music/'+tp+'128kbps/'+x,offs,dur) for x in file]
    print(result[0][0][:10])
    result=minmax(result)
    print(result[0][0][:10])
    #pickle.dump(result,open('databin/'+tp+str(offs)+str(dur)+'.p','wb'))

def minmax(mnmx):
    temp=[numpy.concatenate(x,axis=None) for x in numpy.transpose(mnmx)]
    mn=[min(x) for x in temp]
    mx=[max(x) for x in temp]
    std=[x.std() for x in temp]
    mean=[x.mean() for x in temp]
    form=lambda a,i:(a-mn[i])/(mx[i]-mn[i])
    print(len(mnmx[0]))
    #mnmx=[[form(b[a],a) for a in range(4)] for b in mnmx]
    mnmx=[[(b[a]-mean)/std for a in range(4)] for b in mnmx]
    return mnmx

"""for x in dur:
    for y in offs:
        run(x,y)"""

run(10,30)
