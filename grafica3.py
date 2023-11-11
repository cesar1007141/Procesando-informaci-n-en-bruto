import plotly.express as px
import pandas as pd

# Datos del dataset
data = {
    'id': list(range(1, 21)),
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'] * 5,
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

# Gráfico de boxplot
fig_box = px.box(df, x='materia', y='nota', points="all", title='Distribución de Notas de Estudiantes')
fig_box.update_layout(xaxis_title='Materia', yaxis_title='Nota')
fig_box.show()

# Gráfico de pie chart
fig_pie = px.pie(df, names='aprobado', title='Proporción de Estudiantes Aprobados y No Aprobados')
fig_pie.show()
