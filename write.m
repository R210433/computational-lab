function write(write.txt,content);
      with open(write.txt,'w') as file;
           for item in content:
               file.write("\n",item)
endfunction
write_mode(write.txt,sine-wave)
