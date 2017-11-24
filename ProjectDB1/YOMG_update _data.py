""" Yanet Olimpia Mora Garcia
 yanemora1996@gmail.com
 GITI9072-e
 Unidad III-Patrones de diseño"""

import psycopg2
from config import config


def update_vendor(vendor_id, vendor_name):
    """actualizar el nombre del proveedor basado en el id del proveedor"""

    sql = """UPDATE vendors 
              SET vendor_name = %s
              WHERE vendor_id = %s"""
    conn = None
    updated_rows = 0
    try:
        # leer la configuracion de la base
        params = config()
        # conectar a la Base de Datos PostgreSQL
        conn = psycopg2.connect(**params)
        # crear un nuevo cursor
        cursor = conn.cursor()
        # ejecutar la instruccion UPDATE
        cursor.execute(sql, (vendor_name, vendor_id))
        # obtiene el numero de filas actualizadas
        updated_rows = cursor.rowcount
        #Confirma o guarda los cambios en la Base de Datos
        conn.commit()
        # Cierra la comunicacion con la Base de Datos PostgreSQL
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows



