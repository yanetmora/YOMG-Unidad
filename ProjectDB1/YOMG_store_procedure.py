""" Yanet Olimpia Mora Garcia
 yanemora1996@gmail.com
 GITI9072-e
 Unidad III-Patrones de diseño"""

import psycopg2
from config import config

def get_parts(vendor_id):
    """Obtener piezas proporcionadas por un proveedor especificado por el proveedor_id"""
    conn = None
    try:
        # leer la configuracion
        params = config()
        # conectar con la base de datos de PostgreSQL
        conn = psycopg2.connect(**params)
        # crear un nuevo cursor
        cur = conn.cursor()
        # another way to call a stored procedure
        # cur.execute("SELECT * FROM get_parts_by_vendor( %s); ",(vendor_id,))
        cur.callproc('get_parts_by_vendor', (vendor_id,))
        # establecer el proceso del resultado
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
        # cerra la comunicacion con la base de datos de PostgreSQL
            cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()