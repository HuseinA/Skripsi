import librosa,numpy,pickle
from os import listdir
from os.path import isfile, join

tp='uji'
dur=20
offs=60
file=[f for f in listdir('../Music/'+tp) if isfile(join('../Music/'+tp, f))]

def extraction(song,offset,duration):
    hop_length = 256
    frame_length = 512
    x, sr = librosa.load(song, offset=offset, duration=duration)
    zeros = librosa.zero_crossings(x, pad=False)
    spec_centroid = librosa.feature.spectral_centroid(x, sr=sr)[0]
    spec_rolloff = librosa.feature.spectral_rolloff(x + 0.01, sr=sr)[0]
    energy = numpy.array([sum(x[i:i + frame_length] ** 2)for i in range(0, len(x), hop_length)])
    return [zeros,spec_centroid,spec_rolloff,energy,song[13:-4]]

result=[extraction('../Music/'+tp+'/'+x,offs,dur) for x in file ]
#result=extraction('lagu/'+tp+'/'+file[0],offs,dur)
pickle.dump(result,open('databin/classic'+tp+str(offs)+str(dur)+'.p','wb'))
