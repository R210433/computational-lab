x = [1, 3, 5, 6, 7, 8, -1, -2, 3, -6];
l = length(x);
y = zeros(1, l);

for i = 1:l
    integral = sum(x(1:i));
    y(i) = integral;
end

plot(x);
hold on;
plot(y);
hold off;
