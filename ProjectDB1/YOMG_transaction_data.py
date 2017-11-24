""" Yanet Olimpia Mora Garcia
 yanemora1996@gmail.com
 GITI9072-e
 Unidad III-Patrones de diseño"""

import psycopg2
from config import config

def add_part(part_name, vendor_list):
    # ejecutar la sentencia statement de una nueva fila en la tabla partes
    inser_part = "INSERT INTO parts(part_name) VALUES  (%s) RETURNING part_id;"
    # ejecutar la sentencia statement de una nueva fila en la tabla partes
    assign_vendor = "INSERT INTO vendor_parts(vendor_id, part_id) VALUES (%s, %s)"

    conn = None
    try:
        # leer la configuracion de la base de datos
        params = config()
        # conectar a la base de Datos de PostgreSQL
        conn = psycopg2.connect(**params)
        # crear un nuevo curso
        cur = conn.cursor()
        # insertar una nueva parte
        cur.execute(insert_part, (part_name,))
        # obtener el id_part
        part_id = cur.fetchone()[0]
        # asignar piezas proporcionadas por los proveedores
        for vendor_id in vendor_list:
            cur.execute(assign_vendor, (vendor_id, part_id))

        # guardar cambios
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
