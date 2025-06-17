import numpy as np
import matplotlib.pyplot as plt

# Crear una imagen en blanco
image = np.ones((100, 100))

# Dibujar un círculo negro de radio fijo
cx, cy, radius = 50, 50, 20
for angle in range(0, 360, 1):
    theta = np.deg2rad(angle)
    x = int(cx + radius * np.cos(theta))
    y = int(cy + radius * np.sin(theta))
    if 0 <= x < 100 and 0 <= y < 100:
        image[y, x] = 0  # pixel negro en el borde

# Mostrar imagen con el círculo
plt.imshow(image, cmap='gray')
plt.title('Imagen con circunferencia')
plt.show()

# Inicializar acumulador para centros (x0, y0)
accumulator = np.zeros((100, 100))

# Buscar píxeles oscuros que podrían ser parte del borde del círculo
y_idxs, x_idxs = np.where(image < 0.5)

# Transformada de Hough para círculos (radio fijo)
for i in range(len(x_idxs)):
    x = x_idxs[i]
    y = y_idxs[i]
    for angle in range(0, 360, 5):
        t = np.deg2rad(angle)
        x0 = int(round(x - radius * np.cos(t)))
        y0 = int(round(y - radius * np.sin(t)))
        if 0 <= x0 < 100 and 0 <= y0 < 100:
            accumulator[y0, x0] += 1

# Mostrar acumulador de centros
plt.imshow(accumulator, cmap='hot')
plt.title('Acumulador de centros (circunferencias)')
plt.show()
