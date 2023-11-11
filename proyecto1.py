import requests

def descargar_y_guardar_csv_desde_url(url, nombre_archivo):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(respuesta.text)
        print(f"Los datos fueron descargados correctamente y guardados en {nombre_archivo}.")
    else:
        print(f"Error al descargar los datos. Código de respuesta: {respuesta.status_code}")

url_datos = "https://ej.com/datos.csv"
nombre_archivo_csv = "datos_descargados.csv"
descargar_y_guardar_csv_desde_url(url_datos, nombre_archivo_csv)
