import sqlite3

def obtener_datos_noticia(nombre_medio, url):
    # Conectar a la base de datos
    conexion = sqlite3.connect('basedatos.db')
    cursor = conexion.cursor()

    # Ejecutar una consulta para obtener los datos de la noticia
    cursor.execute("SELECT titulo, fecha_publicacion FROM noticias WHERE medio=? AND url=?",
                   (nombre_medio, url))

    # Obtener los resultados de la consulta
    resultado = cursor.fetchone()

    # Cerrar la conexión a la base de datos
    conexion.close()

    # Verificar si se encontró la noticia en la base de datos
    if resultado:
        titulo, fecha_publicacion = resultado
        return titulo, fecha_publicacion
    else:
        return None, None

# Solicitar al usuario el nombre del medio de prensa y la URL de la noticia
nombre_medio = input("Ingrese el nombre del medio de prensa: ")
url = input("Ingrese la URL de la noticia: ")

# Obtener los datos de la noticia
titulo, fecha_publicacion = obtener_datos_noticia(nombre_medio, url)

# Verificar si se encontró la noticia en la base de datos
if titulo and fecha_publicacion:
    print("Título:", titulo)
    print("Fecha de publicación:", fecha_publicacion)
else:
    print("No se encontraron datos para la noticia en la base de datos.")
