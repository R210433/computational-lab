m = imread("/home/rguktrkvalley/Pictures/recent_addiction.jpg");
red = m(:, :, 1);
green = m(:, :, 2);
blue = m(:, :, 3);
csvwrite("red.csv", red(:));
csvwrite("green.csv", green(:));
csvwrite("blue.csv", blue(:));
