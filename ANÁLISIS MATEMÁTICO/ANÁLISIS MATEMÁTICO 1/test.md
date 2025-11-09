x = -10:0.1:10;
y = x.^2;
plot(x, y);
title("y = x^2");
xlabel("x");
ylabel("y");
grid on;
print -dpng "grafico.png";

