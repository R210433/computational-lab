import pickle
import csv
k=[1,2,3,4]
f=open("mycar.pkl",'wb')
pickle.dump(k,f)
f.close()
jk=open("mycar.pkl","rb")
l=pickle.load(jk)
gh=open("opencsv.csv","w")
writer=csv.writer(gh)
writer.writerow(l)
