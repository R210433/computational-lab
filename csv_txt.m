df=open('onetext.txt','w+');
while(!feof(fid))
     line=fgetl(fid);
     fprintf(df,"%s\n",line);
end
fclose(fid);
fclose(df);
