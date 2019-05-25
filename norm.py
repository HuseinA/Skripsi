import librosa,numpy,pickle
from os import listdir
from os.path import isfile, join

tp='uji'
dur=20
offs=60
file=[f for f in listdir('lagu/'+tp) if isfile(join('lagu/'+tp, f))]

def extraction(song,offset,duration):
    hop_length = 256
    frame_length = 512
    x, sr = librosa.load(song, offset=offset, duration=duration)
    zeros = librosa.zero_crossings(x, pad=False)
    spec_centroid = norm(librosa.feature.spectral_centroid(x, sr=sr)[0])
    spec_rolloff = minmax(librosa.feature.spectral_rolloff(x + 0.01, sr=sr)[0])
    energy = minmax(numpy.array([sum(x[i:i + frame_length] ** 2)for i in range(0, len(x), hop_length)]))
    return spec_centroid#[zeros,spec_centroid,spec_rolloff,energy,song[9:-4]]

def norm(fitur):
    x=fitur.var()
    y=fitur.mean()
    return (fitur-y)/(max(fitur)-min(fitur))

def minmax(fitur):
    return (fitur-min(fitur))/(max(fitur)-min(fitur))

#result=[extraction('lagu/'+tp+'/'+x,offs,dur) for x in file ]
for x in file:
    z=extraction('lagu/'+tp+'/'+x,offs,dur)
    print(max(z),min(z))
#pickle.dump(result,open('databin/norm'+tp+str(offs)+str(dur)+'.p','wb'))
