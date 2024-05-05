def read(write.txt):
      with open(write.txt,'r') as file:
            content=file.readlines()
      return content
normal=read(write.txt_normal)
print("Read from file in normal mode";normal)
