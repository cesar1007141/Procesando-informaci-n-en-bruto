import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)

# Datos de calificaciones de los estudiantes
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

# Datos de errores para el gráfico de barras de error
errores_matematicas = rng.uniform(2, 5, 2)
errores_matematicas = [min(errores_matematicas), max(errores_matematicas)]

errores_ciencias = rng.uniform(1, 4, 2)
errores_ciencias = [min(errores_ciencias), max(errores_ciencias)]

errores_literatura = rng.uniform(3, 6, 2)
errores_literatura = [min(errores_literatura), max(errores_literatura)]

# Gráfico de dispersión
plt.scatter(matematicas, ciencias)
plt.xlabel('Calificaciones de Matemáticas')
plt.ylabel('Calificaciones de Ciencias')
plt.title('Relación entre Calificaciones de Matemáticas y Ciencias')
plt.show()

# Gráfico de barras de error
materias = ['Matemáticas', 'Ciencias', 'Literatura']
calificaciones_promedio = [np.mean(matematicas), np.mean(ciencias), np.mean(literatura)]
errores = [errores_matematicas, errores_ciencias, errores_literatura]

plt.bar(materias, calificaciones_promedio, yerr=errores, capsize=5)
plt.xlabel('Materias')
plt.ylabel('Calificación Promedio')
plt.title('Calificación Promedio en Tres Materias con Barras de Error')
plt.legend(['Calificación Promedio'])
plt.show()

# Histograma
plt.hist(matematicas, bins=10, edgecolor='black')
plt.xlabel('Calificaciones de Matemáticas')
plt.ylabel('Frecuencia')
plt.title('Distribución de Calificaciones de Matemáticas')
plt.show()
