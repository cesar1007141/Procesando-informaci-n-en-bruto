import pandas as pd
import matplotlib.pyplot as plt

# Datos del dataset
data = {
    'id': list(range(1, 21)),
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'] * 5,
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

# Gráfico de boxplot
plt.figure(figsize=(10, 6))
plt.boxplot(df['nota'], vert=False)
plt.title('Distribución de Notas de Estudiantes')
plt.xlabel('Nota')
plt.show()

# Gráfico de pie chart
aprobados = df['aprobado'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(aprobados, labels=aprobados.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral'])
plt.title('Proporción de Estudiantes Aprobados y No Aprobados')
plt.show()
