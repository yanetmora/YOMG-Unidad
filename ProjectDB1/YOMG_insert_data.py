""" Yanet Olimpia Mora Garcia
 yanemora1996@gmail.com
 GITI9072-e
 Unidad III-Patrones de diseño"""

import psycopg2
from config import config


def insert_vendor(vendor_name):
    """ inserta un nuevo vendedor en la tabla vendedor """
    sql = """INSERT INTO vendors(vendor_name)
             VALUES(%s) RETURNING vendor_id;"""
    conn = None
    vendor_id = None
    try:
        # leer configuracion de la base de datos
        params = config()
        # conectarse a la Base de Datos PostgreSQL
        conn = psycopg2.connect(**params)
        # Crear un nuevo Cursor
        cur = conn.cursor()
        # ejecutar la instruccion INSERT
        cur.execute(sql, (vendor_name,))
        # recuperar el id generado
        vendor_id = cur.fetchone()[0]
        # commit cambios a la Base de Datos
        conn.commit()
        # cerra la comunicacion con l Base de Datos
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return vendor_id
