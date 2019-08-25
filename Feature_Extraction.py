import librosa,numpy,pickle
from os import listdir
from os.path import isfile, join

tp='uji'
dur=10
offs=120

file=[f for f in listdir('../Music/'+tp+'128kbps') if isfile(join('../Music/'+tp+'128kbps', f))]

def extraction(song,offset,duration):
    hop_length = 256
    frame_length = 512
    x, sr = librosa.load(song, offset=offset, duration=duration)
    #if len(x)==0: 
    #    return None
    zeros = librosa.feature.zero_crossing_rate(x)[0]
    spec_centroid = librosa.feature.spectral_centroid(x, sr=sr)[0]
    spec_rolloff = librosa.feature.spectral_rolloff(x + 0.01, sr=sr)[0]
    energy = numpy.array([sum(x[i:i + frame_length] ** 2)for i in range(0, len(x), hop_length)])
    return [zeros,spec_centroid,spec_rolloff,energy,song[20:-4]]

def run(dur,offs):
    print('databin/'+tp+str(offs)+str(dur)+'.p')
    result=[extraction('../Music/'+tp+'128kbps/'+x,offs,dur) for x in file]
    print(result[0])
    #result=[x for x in result if x!=None]
    print(len(result))
    #pickle.dump(result,open('databin/'+tp+str(offs)+str(dur)+'.p','wb'))

#for x in offs:
#    run(dur,x)

result=[extraction('../Music/'+tp+'128kbps/'+x,offs,dur) for x in file]
#result=extraction('../Music/uji128kbps/Black Dog',offs,dur)
#pickle.dump(result,open('databin/'+tp+str(offs)+str(dur)+'.p','wb'))
