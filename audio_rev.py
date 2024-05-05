from scipy.io import wavfile

# Read the audio file
f, x = wavfile.read("/home/rguktrkvalley/python(Cl)/Chorus.wav")

# Reverse the audio
rev = x[::-1]

# Write the reversed audio to a new file
wavfile.write("new.wav", f, rev)
