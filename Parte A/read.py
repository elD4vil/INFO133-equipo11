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



