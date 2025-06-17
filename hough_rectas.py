import numpy as np
import matplotlib.pyplot as plt

# Crear una imagen en blanco
image = np.ones((100, 100))

# Dibujar dos líneas diagonales negras manualmente
for i in range(100):
    if i < 80:
        image[i, i] = 0  # diagonal principal
        image[i, 99 - i] = 0  # diagonal secundaria

# Mostrar imagen original
plt.imshow(image, cmap='gray')
plt.title('Imagen original con líneas')
plt.show()

# Transformada de Hough desde cero
thetas = np.deg2rad(np.arange(-90, 90))
width, height = image.shape
diag_len = int(np.ceil(np.sqrt(width ** 2 + height ** 2)))
rhos = np.linspace(-diag_len, diag_len, diag_len * 2)

accumulator = np.zeros((2 * diag_len, len(thetas)))

# Detectar bordes manualmente (valores oscuros)
y_idxs, x_idxs = np.where(image < 0.5)

# Votación en el acumulador
for i in range(len(x_idxs)):
    x = x_idxs[i]
    y = y_idxs[i]
    for t in range(len(thetas)):
        rho = int(round(x * np.cos(thetas[t]) + y * np.sin(thetas[t]))) + diag_len
        accumulator[rho, t] += 1

# Mostrar acumulador (espacio Hough)
plt.imshow(accumulator, cmap='hot', extent=[-90, 90, -diag_len, diag_len])
plt.title('Espacio de parámetros Hough (rectas)')
plt.xlabel('Theta (°)')
plt.ylabel('Rho (px)')
plt.show()
