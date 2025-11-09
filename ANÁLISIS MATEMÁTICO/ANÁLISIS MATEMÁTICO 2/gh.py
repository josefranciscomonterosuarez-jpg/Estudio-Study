import matplotlib
matplotlib.use('Agg')  # sin interfaz gráfica, genera la imagen directamente
import matplotlib.pyplot as plt

# Datos
x = [i for i in range(-10, 11)]
y = [i**2 for i in x]

# Gráfico
plt.plot(x, y, label="y = x^2")
plt.title("Gráfico cuadrático")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

# Guarda la imagen
plt.savefig("grafico.png")  # se guarda en la misma carpeta que tu archivo .py

print("✅ Gráfico guardado como 'grafico.png'")
