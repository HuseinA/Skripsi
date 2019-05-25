import librosa, librosa.display
import numpy, scipy, matplotlib.pyplot as plt, IPython.display as ipd, sklearn
music = 'fly.mp3'
x,sr=librosa.load(music,duration=10)
zeros=librosa.zero_crossings(x,pad=False)
#print(zeros.shape)
#print(sum(zeros))
#print(len(x))
#spectral_centroids = librosa.feature.spectral_centroid(x, sr=sr)[0]
#print(spectral_centroids)
#frames = range(len(spectral_centroids))
#t = librosa.frames_to_time(frames)
print(sr)
print(x.shape)
print(librosa.get_duration(x,sr))
hop_length = 256
frame_length = 512
energy = numpy.array([
    sum(abs(x[i:i+frame_length]**2))
    for i in range(0, len(x), hop_length)
])
print(energy)