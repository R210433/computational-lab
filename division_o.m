x=input("Enter a:");
y=input("Ente b:");
if(y!=0)
   if((isa(x, 'double')&& isa(y, 'double')) || (isa(x, 'single')&& isa(y, 'double'))||
   (isa(x, 'double')&& isa(y, 'single')) || (isa(x, 'single')&& isa(y, 'single')))
        disp(x/y);
   end
end
else  
    disp("division not possible");
end