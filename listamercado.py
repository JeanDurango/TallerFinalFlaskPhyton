from flask import Flask, render_template, request, redirect, flash
import controlador_productos

app = Flask(__name__)

"""
Definición de rutas
"""


@app.route("/agregar_producto")
def formulario_agregar_producto():
    return render_template("agregar_producto.html")


@app.route("/guardar_producto", methods=["POST"])
def guardar_producto():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    cantidad = request.form["cantidad"]
    controlador_productos.insertar_producto(nombre, descripcion, cantidad)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/productos")


@app.route("/")
@app.route("/productos")
def productos():
    productos = controlador_productos.obtener_producto()
    return render_template("productos.html", productos=productos)


@app.route("/eliminar_producto", methods=["POST"])
def eliminar_producto():
    controlador_productos.eliminar_producto(request.form["id"])
    return redirect("/productos")


@app.route("/formulario_editar_producto/<int:id>")
def editar_producto(id):
    # Obtener el juego por ID
    producto = controlador_productos.obtener_producto_por_id(id)
    return render_template("editar_producto.html", producto=producto)


@app.route("/actualizar_producto", methods=["POST"])
def actualizar_producto():
    id = request.form["id"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    cantidad = request.form["cantidad"]
    controlador_productos.actualizar_productos(nombre, descripcion, cantidad, id)
    return redirect("/productos")


# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
