function
   read(write.txt);
       with open(write.txt,'rb') as file;
             content=loadtxt(file)
      return content;
endfunction
read_binary=read(write.txt-binary);
disp(read-binary);
