path = '/home/rguktrkvalley/python(Cl)/Chorus.wav';

% Read the audio file
[audio_data, sample] = audioread(path);

% Plot the audio signal
time= (0:length(audio_data)-1) / sample;
plot(time, audio_data);
xlabel('Time (s)');
ylabel('Amplitude');
title('Audio Signal');