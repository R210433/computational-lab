def read(write.txt):
     with open(write.txt,'rb') as file:
         content=np.loadtxt(file)
    return content
read_binary=read(write.txt-binary)
print(read-binary)
