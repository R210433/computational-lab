% Load data from pickle file
a =fopen("bye.pkl", "rb");
m =fread(a);
fclose(a);

% Open CSV file for writing
n = fopen("noth.csv", "w");

% Write data to CSV file
fprintf(n, '%f,', m);
fclose(n);
