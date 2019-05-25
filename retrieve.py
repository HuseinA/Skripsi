import librosa
import IPython.display as ipd
#%matplotlib inline
import matplotlib.pyplot as plt
import librosa.display

music = 'Hero.mp3'
x,sr=librosa.load(music,duration=30)
ipd.Audio(x,rate=sr,autoplay=True)

plt.figure(figsize=(14, 5))
librosa.display.waveplot(x, sr)
