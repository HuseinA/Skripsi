import librosa,numpy,pickle
from os import listdir
from os.path import isfile, join

tp='uji'
dur=10
offs=120
fd='../Music/'+tp+'128kbps'

file=[f for f in listdir(fd) if isfile(join(fd, f))]

def extraction(song,offset,duration):
    hop_length = 256
    frame_length = 512
    x, sr = librosa.load(song, offset=offset, duration=duration)
    zeros = librosa.feature.zero_crossing_rate(x)[0]
    spec_centroid = librosa.feature.spectral_centroid(x, sr=sr)[0]
    spec_rolloff = librosa.feature.spectral_rolloff(x + 0.01, sr=sr)[0]
    energy = numpy.array([sum(x[i:i + frame_length] ** 2)for i in range(0, len(x), hop_length)])
    return [zeros,spec_centroid,spec_rolloff,energy,song[20:-4]]

def run(dur,offs):
    print('databin/'+tp+str(offs)+str(dur)+'.p')
    result=[extraction('../Music/'+tp+'128kbps/'+x,offs,dur) for x in file]
    print(result[0])
    print(len(result))
    pickle.dump(result,open('databin/'+tp+str(offs)+str(dur)+'.p','wb'))

# Use it to make multiple dataset
#for x in offs:
#    run(dur,x)

# Use it to make single dataset
result=[extraction('../Music/'+tp+'128kbps/'+x,offs,dur) for x in file]
pickle.dump(result,open('databin/'+tp+str(offs)+str(dur)+'.p','wb'))
