import pandas as pd
import mysql.connector
import sys

# Connect to MariaDB Platform
try:
    conn = mysql.connector.connect(
        user="nuevousuario",
        password="contraseña",
        host="127.0.0.1",
        port=3306
    )

except mysql.connector.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

# Create Database
cur.execute("DROP DATABASE ParteA")
query_create = "CREATE DATABASE ParteA"
cur.execute(query_create)
cur.execute("USE ParteA")

# Crear la tabla Medio
cur.execute("""
    CREATE TABLE Medio (
        ID_Medio INT PRIMARY KEY,
        Comuna VARCHAR(100),
        Region VARCHAR(100),
        Nombre_Medio VARCHAR(100),
        Cobertura VARCHAR(100),
        Continente VARCHAR(100),
        Año_Fundacion VARCHAR(100),
        Pais VARCHAR(100)
    )
""")

# Crear la tabla Fundador
cur.execute("""
    CREATE TABLE Fundador (
        ID_Fundador INT PRIMARY KEY,
        Nombre_Fundador VARCHAR(100)
    )
""")

# Crear la tabla RedSocial
cur.execute("""
    CREATE TABLE RedSocial (
        Nombre_Usuario VARCHAR(100) PRIMARY KEY,
        ID_Medio INT,
        Nombre_Red VARCHAR(100),
        N_Seguidores INT,
        Fecha_Actualizacion VARCHAR(100),
        FOREIGN KEY (ID_Medio) REFERENCES Medio(ID_Medio)
    )
""")

# Crear la tabla SitioWeb
cur.execute("""
    CREATE TABLE SitioWeb (
        ID_SitioWeb INT PRIMARY KEY,
        ID_Medio INT,
        Nombre_SitioWeb VARCHAR(100),
        URL VARCHAR(255),
        FOREIGN KEY (ID_Medio) REFERENCES Medio(ID_Medio)
    )
""")
# Crear la tabla Categoria
cur.execute("""
    CREATE TABLE Categoria (
        Nombre_Categoria VARCHAR(100) PRIMARY KEY,
        ID_SitioWeb INT,
        URL VARCHAR(255),
        Xpath_URL_Noticia VARCHAR(255),
        FOREIGN KEY (ID_SitioWeb) REFERENCES SitioWeb(ID_SitioWeb)
    )
""")

# Crear la tabla Noticia
cur.execute("""
    CREATE TABLE Noticia (
        ID_Noticia INT PRIMARY KEY,
        ID_SitioWeb INT,
        URL VARCHAR(255),
        Xpath_Titulo VARCHAR(255),
        Xpath_Contenido VARCHAR(255),
        Xpath_URL_Fecha VARCHAR(255),
        FOREIGN KEY (ID_SitioWeb) REFERENCES SitioWeb(ID_SitioWeb)
    )
""")

# Crear la tabla Fundar
cur.execute("""
    CREATE TABLE Fundar (
        ID_Medio INT,
        ID_Fundador INT,
        PRIMARY KEY (ID_Medio, ID_Fundador),
        FOREIGN KEY (ID_Medio) REFERENCES Medio(ID_Medio),
        FOREIGN KEY (ID_Fundador) REFERENCES Fundador(ID_Fundador)
    )
""")
try:
    df = pd.read_csv("files/TablaMedio.csv", sep=';')
    # Iterar sobre cada fila del DataFrame
    for _, row in df.iterrows():
        # Obtener los valores de cada columna
        col1 = row['ID_Medio']
        col2 = row['Comuna']
        col3 = row['Region']
        col4 = row['Nombre_Medio']
        # col5 = row['Cobertura']
        col6 = row['Continente']
        col7 = row['Año_Fundacion']
        col8 = row['Pais']
        # Construir la consulta SQL de inserción
        sql = f"INSERT INTO Medio (ID_Medio, Comuna, Region, Nombre_Medio, Continente, Año_Fundacion, Pais) VALUES ('{col1}', '{col2}', '{col3}', '{col4}', '{col6}', '{col7}', '{col8}')"
        # Ejecutar la consulta SQL
        cur.execute(sql)
    # Confirmar los cambios en la base de datos
    conn.commit()
    print("Los datos se han insertado correctamente en la base de datos.")

    df = pd.read_csv("files/TablaFundador.csv", sep=';')
    # Iterar sobre cada fila del DataFrame
    for _, row in df.iterrows():
        # Obtener los valores de cada columna
        col1 = row['ID_Fundador']
        col2 = row['Nombre_Fundador']
        # Construir la consulta SQL de inserción
        sql = f"INSERT INTO Fundador (ID_Fundador, Nombre_Fundador) VALUES ('{col1}', '{col2}')"
        # Ejecutar la consulta SQL
        cur.execute(sql)
    # Confirmar los cambios en la base de datos
    conn.commit()
    print("Los datos se han insertado correctamente en la base de datos.")
    
    df = pd.read_csv("files/TablaRedSocial.csv", sep=';')
    # Iterar sobre cada fila del DataFrame
    for _, row in df.iterrows():
        # Obtener los valores de cada columna
        col1 = row['Nombre_Usuario']
        col2 = row['ID_Medio']
        col3 = row['Nombre_Red']
        col4 = row['N_Seguidores']
        col5 = row['Fecha_Actualizacion']
        # Construir la consulta SQL de inserción
        sql = f"INSERT INTO RedSocial (Nombre_Usuario, ID_Medio, Nombre_Red, N_Seguidores, Fecha_Actualizacion) VALUES ('{col1}', '{col2}', '{col3}', '{col4}', '{col5}')"
        # Ejecutar la consulta SQL
        cur.execute(sql)
    # Confirmar los cambios en la base de datos
    conn.commit()
    print("Los datos se han insertado correctamente en la base de datos.")
    
    df = pd.read_csv("files/TablaSitioWeb.csv", sep=';')
    # Iterar sobre cada fila del DataFrame
    for _, row in df.iterrows():
        # Obtener los valores de cada columna
        col1 = row['ID_SitioWeb']
        col2 = row['ID_Medio']
        col3 = row['Nombre_SitioWeb']
        col4 = row['URL']
        # Construir la consulta SQL de inserción
        sql = f"INSERT INTO Fundador (ID_SitioWeb, ID_Medio, Nombre_SitioWeb, URL) VALUES ('{col1}', '{col2}', '{col3}', '{col4}')"
        # Ejecutar la consulta SQL
        cur.execute(sql)
    # Confirmar los cambios en la base de datos
    conn.commit()
    print("Los datos se han insertado correctamente en la base de datos.")
    
    df = pd.read_csv("files/TablaCategoria.csv", sep=';')
    # Iterar sobre cada fila del DataFrame
    for _, row in df.iterrows():
        # Obtener los valores de cada columna
        col1 = row['Nombre_Categoria']
        col2 = row['ID_SitioWeb']
        col3 = row['URL']
        col4 = row['Xpath_URL_Noticia']
        # Construir la consulta SQL de inserción
        sql = f"INSERT INTO Categoria (Nombre_Categoria, ID_SitioWeb, URL, Xpath_URL_Noticia) VALUES ('{col1}', '{col2}', '{col3}', '{col4}')"
        # Ejecutar la consulta SQL
        cur.execute(sql)
    # Confirmar los cambios en la base de datos
    conn.commit()
    print("Los datos se han insertado correctamente en la base de datos.")

    df = pd.read_csv("files/TablaNoticia.csv", sep=';')
    # Iterar sobre cada fila del DataFrame
    for _, row in df.iterrows():
        # Obtener los valores de cada columna
        col1 = row['ID_Noticia']
        col2 = row['ID_SitioWeb']
        col1 = row['URL']
        col2 = row['Xpath_Titulo']
        col1 = row['Xpath_Contenido']
        col2 = row['Xpath_URL_Fecha']
        # Construir la consulta SQL de inserción
        sql = f"INSERT INTO Noticia (ID_Noticia, ID_SitioWeb, URL, Xpath_Titulo, Xpath_Contenido, Xpath_URL_Fecha) VALUES ('{col1}', '{col2}', '{col3}', '{col4}', '{col5}', '{col6}')"
        # Ejecutar la consulta SQL
        cur.execute(sql)
    # Confirmar los cambios en la base de datos
    conn.commit()
    print("Los datos se han insertado correctamente en la base de datos.")

    df = pd.read_csv("files/TablaFundar.csv", sep=';')
    # Iterar sobre cada fila del DataFrame
    for _, row in df.iterrows():
        # Obtener los valores de cada columna
        col1 = row['ID_Medio']
        col2 = row['ID_Fundador']
        # Construir la consulta SQL de inserción
        sql = f"INSERT INTO Fundar (ID_Medio, ID_Fundador) VALUES ('{col1}', '{col2}')"
        # Ejecutar la consulta SQL
        cur.execute(sql)
    # Confirmar los cambios en la base de datos
    conn.commit()
    print("Los datos se han insertado correctamente en la base de datos.")

except Exception as e:
    # Imprimir cualquier error que ocurra
    print("Error:", str(e))
    conn.rollback()

cur.close()
conn.close()
