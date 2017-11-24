""" Yanet Olimpia Mora Garcia
 yanemora1996@gmail.com
 GITI9072-e
 Unidad III-Patrones de diseño"""

import psycopg2
from config import config

def delete_part(part_id):
    """Eliminar la tabla parte mediante el id_parte"""
    conn = None
    rows_deleted = 0
    try:
        # leer la configuracion de la base de datos
        params = config()
        # conectar a la base de datos de Postgres
        conn = psycopg2.connect(**params)
        #crear un nuevo cursopr
        cur = conn.cursor()
        # ejecutar la modificacion del statement
        cur.execute("DELETE FROM parts WHERE part_id = %s", (part_id,))
        # obtiene el numero de filas modificadas
        rows_deleted = cur.rowcount
        # guarda los cambios en la base de datos
        conn.commit()
        # cierra la comunicacion con la base de datos de PostGres
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted