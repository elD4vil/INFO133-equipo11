import mysql.connector

def obtener_datos_noticia(nombre_medio, url):
    # Configurar los datos de conexión a la base de datos
    config = {
        'user': 'root',
        'password': '123456',
        'host': 'localhost',
        'database': 'Medios',
        'raise_on_warnings': True
    }

    try:
        # Establecer la conexión a la base de datos
        conexion = mysql.connector.connect(**config)

        # Crear un cursor para ejecutar consultas
        cursor = conexion.cursor()

        # Ejecutar una consulta para obtener los datos de la noticia
        consulta = """
        SELECT Noticia.Xpath_Titulo, Noticia.Xpath_URL_Fecha
        FROM Noticia
        INNER JOIN SitioWeb ON Noticia.ID_SitioWeb = SitioWeb.ID_SitioWeb
        INNER JOIN Medio ON SitioWeb.ID_Medio = Medio.ID_Medio
        WHERE Medio.Nombre_Medio = %s AND Noticia.URL = %s
        """
        valores = (nombre_medio, url)
        cursor.execute(consulta, valores)

        # Obtener los resultados de la consulta
        resultado = cursor.fetchone()

        # Cerrar el cursor y la conexión a la base de datos
        cursor.close()
        conexion.close()

        # Verificar si se encontró la noticia en la base de datos
        if resultado:
            titulo, fecha_publicacion = resultado
            return titulo, fecha_publicacion
        else:
            return None, None

    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)


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
