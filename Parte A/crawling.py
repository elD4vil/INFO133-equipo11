import mysql.connector
import random
from requests_html import HTMLSession
import sys
import time
import mariadb

def obtener_enlaces_categoria(nombre_medio, categoria):
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
        SELECT m.Nombre_Medio, s.URL, c.Xpath_URL_Noticia
        FROM SitioWeb s
        INNER JOIN Medio m ON m.ID_Medio = s.ID_Medio
        INNER JOIN Categoria c ON m.ID_Medio = c.Categoria
        WHERE m.Nombre_Medio = %s AND c.Nombre_Categoria= %s;
        """
        valores = (nombre_medio, categoria)
        cursor.execute(consulta, valores)

        # Obtener los resultados de la consulta
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado:
            medio, sitioweb, xpath_url = resultado
            return medio, sitioweb, xpath_url
        else:
            return None, None, None

    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)


# Connect to MariaDB Platform
try:
    config = {
        'user': 'root',
        'password': '123456',
        'host': 'localhost',
        'database': 'Medios',
        'raise_on_warnings': True
    }
    
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = config.cursor()

cur.execute("DROP DATABASE web_scraping")
query_create = "CREATE DATABASE web_scraping"
cur.execute(query_create)
cur.execute("USE web_scraping")
cur.execute("CREATE TABLE url (id INT AUTO_INCREMENT PRIMARY KEY, url TEXT)")

def format_date(date):
    return(date.split("T")[0])


nombre_medio = input("Ingrese el nombre del medio de prensa: ")
categoria = input("Ingrese la categoria: ")

nombre_medio, sitioweb, xpath_url = obtener_enlaces_categoria(nombre_medio, categoria)


URL_SEED = f"{sitioweb}/{categoria}"


USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
]

headers = {'user-agent':random.choice(USER_AGENT_LIST) }

session = HTMLSession()

xpath_url1 = xpath_url


for i in range(1,3):
    response = session.get("{}{}".format(URL_SEED,i),headers=headers)
    all_urls = response.html.xpath(xpath_url1)

    for url in all_urls:
        article_url = f"{sitioweb}" + url
        print(article_url)

        #Insert into mariadb
        cur.execute("INSERT INTO url (url) VALUES (?)", (article_url,))


    time.sleep(2)
