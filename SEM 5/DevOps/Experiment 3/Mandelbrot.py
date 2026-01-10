import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    image = np.zeros((height, width))
    for x in range(width):
        for y in range(height):
            real = xmin + (x / width) * (xmax - xmin)
            imag = ymin + (y / height) * (ymax - ymin)
            c = complex(real, imag)
            color = mandelbrot(c, max_iter)
            image[y, x] = color
    return image

# Settings
xmin, xmax = -2.5, 1.5
ymin, ymax = -2, 2
width, height = 800, 800
max_iter = 256

# Generate and plot
mandelbrot_image = generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)
plt.imshow(mandelbrot_image, extent=(xmin, xmax, ymin, ymax), cmap='hot')
plt.colorbar(label='Iterations')
plt.title("Mandelbrot Set")
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()
