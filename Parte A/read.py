import pandas as pd
import mysql.connector
import sys

def ejecutar_consulta(sql):

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

    cur.execute(sql)
    resultados = cur.fetchall()

    cur.close()
    conn.close()

    return resultados

def main():
    print("OPCIONES")
    print("XPATH para leer la fecha de un medio (1)")
    print("Categorias de un medio (2)")
    print("Medio con la mayor cantidad de fundadores (3)")
    print("Cual es el medio más viejo (4)")
    print("Cual es el medio más nuevo (5)")

    opcion = int(input("Ingrese la opción que quiere leer: "))

    # if(opcion == 1):
    #     dsfsdf
    
    # elif(opcion == 2):

    # elif(opcion == 3):
    
    # elif(opcion == 4):
    
    # elif(opcion == 5):


