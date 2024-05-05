import pickle
import csv
a=open("bye.pkl",'rb')
m=pickle.load(a)
a.close()
n=open("noth.csv","w")
w=csv.writer(n)
w.writerow(m)
