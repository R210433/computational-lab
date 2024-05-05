function dydt = myODE(t, y)
    dydt = -0.5 * y; 
endfunction
tspan = [0, 10];
y0 = 1;
[t, y] = ode45(@myODE, tspan, y0);
plot(t, y);
xlabel('Time');
ylabel('y(t)');
title('Solution of the Differential Equation');
