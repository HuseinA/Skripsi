import librosa, numpy, pickle
from os import listdir
from os.path import isfile, join

data = "uji"
dur = 5  # song duration
offs = 120  # song offset
directory = "../Music/" + data + "128kbps" # song directory

file = [f for f in listdir(directory) if isfile(join(directory, f))]


def extraction(song, offset, duration):
    hop_length = 256
    frame_length = 512
    waveform, sr = librosa.load(song, offset=offset, duration=duration)
    zcr = librosa.feature.zero_crossing_rate(waveform)[0]  # zero crossing rate
    spec_centroid = librosa.feature.spectral_centroid(waveform, sr=sr)[0]  # spectral centroid
    spec_rolloff = librosa.feature.spectral_rolloff(waveform + 0.01, sr=sr)[0]  # spectral rolloff
    energy = numpy.array([sum(waveform[i : i + frame_length] ** 2) for i in range(0, len(waveform), hop_length)])  # energy
    return [zcr, spec_centroid, spec_rolloff, energy, song[20:-4]]


def run(dur, offs):
    print("databin/" + data + str(offs) + str(dur) + ".p")
    result = [extraction(directory + waveform, offs, dur) for waveform in file]
    print(result[0])
    print(len(result))
    pickle.dump(result, open("databin/" + data + str(offs) + str(dur) + ".p", "wb"))


# Use it to make multiple dataset
# for waveform in offs:
#    run(dur,waveform)

# Use it to make single dataset
result = [extraction(directory + waveform, offs, dur) for waveform in file]
pickle.dump(result, open("databin/" + data + str(offs) + str(dur) + ".p", "wb"))
