path = '/home/rguktrkvalley/python(Cl)/Chorus.wav';
[audio_data, sample] = audioread(path);
time= (0:length(audio_data)-1) / sample;
plot(time, audio_data);
xlabel('Time (s)');
ylabel('Amplitude');
title('Audio Signal');
