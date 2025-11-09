clc; clear; close all;

x = linspace(0, 2, 100);
y = x.^2;

% crear la malla de revolución
theta = linspace(0, 2*pi, 100);
[X, T] = meshgrid(x, theta);
Y = (X.^2) .* cos(T);
Z = (X.^2) .* sin(T);

surf(X, Y, Z);
shading interp
colormap("jet");
xlabel("x");
ylabel("y");
zlabel("z");
title("Volumen de revolución de y = x^2 alrededor del eje X");
axis equal;
grid on;
view(45, 30);
print("C:/Users/Cris/Desktop/trabajo/GRAFICOS_OCTAVE/grafico 2.png", "-dpng", "-r300");



$$GRAFICO$$

<img width="1744" height="1308" alt="grafico 2" src="https://github.com/user-attachments/assets/b6c73a02-d0ce-4fd6-b0a8-6fc556ebfbc2" />

