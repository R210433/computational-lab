import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
path = '/home/rguktrkvalley/python(Cl)/Chorus.wav'
sample, audio_data = wavfile.read(file_path)
time= np.arange(len(audio_data)) / sample
plt.plot(time,audio_data)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Audio Signal')
plt.show()
