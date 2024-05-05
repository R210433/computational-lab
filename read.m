function
     read(write.txt);
          with open(write.txt,'r') as file;
            content=file.readlines()
      return content;
endfunction
normal=read(write.txt_normal);
print(normal);
