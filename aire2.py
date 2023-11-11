import requests

def ej_2_cargar_calidad_aire(ciudades: Set[str]) -> None:
    api_url = "https://api-ninjas.com/api/airquality"
    
    # Obtener datos de calidad del aire para cada ciudad
    calidad_aire_data = []
    for ciudad in ciudades:
        response = requests.get(api_url, params={'city': ciudad})
        data = response.json()
        calidad_aire_data.append({
            'city': ciudad,
            'concentration': data.get('concentration', None)
        })
    
    # Crear tabla de dimensiones usando pandas
    calidad_aire_df = pd.DataFrame(calidad_aire_data)
    
    # Guardar la tabla en un archivo CSV o en la base de datos
    calidad_aire_df.to_csv('calidad_aire.csv', index=False)
