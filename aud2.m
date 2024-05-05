[x,f]=audioread("/home/rguktrkvalley/python(Cl)/Chorus.wav");
m=size(x,1);
rev=x(m:-1:1,:);
audiowrite("new.wav",rev,f);