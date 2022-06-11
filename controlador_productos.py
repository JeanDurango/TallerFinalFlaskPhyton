from bd import obtener_conexion


def insertar_producto(nombre, descripcion, cantidad):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO productos(nombre, descripcion, cantidad) VALUES (%s, %s, %s)",
                       (nombre, descripcion, cantidad))
    conexion.commit()
    conexion.close()


def obtener_producto():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
    conexion.close()
    return productos


def eliminar_producto(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM productos WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_producto_por_id(id):
    conexion = obtener_conexion()
    producto = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM productos WHERE id = %s", (id,))
        producto = cursor.fetchone()
    conexion.close()
    return producto


def actualizar_productos(nombre, descripcion, cantidad, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE productos SET nombre = %s, descripcion = %s, cantidad = %s WHERE id = %s",
                       (nombre, descripcion, cantidad, id))
    conexion.commit()
    conexion.close()
