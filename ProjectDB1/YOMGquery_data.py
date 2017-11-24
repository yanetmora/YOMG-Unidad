""" Yanet Olimpia Mora Garcia
 yanemora1996@gmail.com
 GITI9072-e
 Unidad III-Patrones de diseño"""

import psycopg2
from config import config

def get_vendors():
    """datos de consulta de tabla proveedores"""
    conn = None
    try:
        params = config()
        conn= psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name")
        print("El numero de partes: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
