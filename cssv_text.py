import csv
jl=open("new.csv","r")
reader=csv.reader(jl)
df=open("onetext.txt","w+")
for data in reader:
     df.write(str(data))
