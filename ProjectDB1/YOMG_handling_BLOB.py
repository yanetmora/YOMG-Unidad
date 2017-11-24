""" Yanet Olimpia Mora Garcia
 yanemora1996@gmail.com
 GITI9072-e
 Unidad III-Patrones de diseño"""

import psycopg2
from config import config

def write_blob(part_id, path_to_file, file_extension):
    """Insert a BLOB into table"""
    con = None
    try:
        # Leer datos de una imagen
        drawing = open(path_to_file, 'rb').read()
        # Leer la configuracion de la Base de Datos
        params = config()
        # Conectar a la Base de datos de PostgreSQL
        conn = psycopg2.connect(**params)
        # Crear un nuevo cursor
        cur = con.cursor()
        # ejecutar la sentencia Insert
        cur.execute("INSERT INTO part_drawings,(part_id, file_extension, drawing_data)"
                    "VALUES (%s,%s,%s)",
                    (part_id, file_extension, psycopg2.Binary(drawing)))
        # Guarda los cambioes en la base de datos
        con.commit()
        # Cerramos la comunicacion con la base de datos
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
