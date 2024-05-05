import os,sys
file=input("enter a file name")
if os.path.isfile(file):
   print("file exist")
else:
    print("file not exist")

