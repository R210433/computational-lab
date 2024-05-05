% Prompt user to enter a file name
file = input("Enter a file name: ", 's');

% Check if the file exists
if exist(file, 'file') == 2
    disp("File exists");
else
    disp("File does not exist");
end