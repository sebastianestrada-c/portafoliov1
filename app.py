from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

# --- MAGIA DE RUTAS ABSOLUTAS ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "portafolio.db")
# --------------------------------

@app.route("/")
def hello_world():
    titular = "Portafolio"
    return render_template("index.html", subtitulo_hero=titular)

@app.route("/contacto", methods=['GET', 'POST'])
def contacto():
    mensaje_confirmacion = None
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        mensaje = request.form.get('mensaje')

        if nombre and email and mensaje:
            conexion = sqlite3.connect(DB_PATH)
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO mensajes_contacto (nombre, email, mensaje)
                VALUES (?, ?, ?)
            """, (nombre, email, mensaje))
            conexion.commit()
            conexion.close()

            mensaje_confirmacion = f"Gracias, {nombre}. Tu mensaje fue guardado exitosamente."

    return render_template("contacto.html", confirmacion=mensaje_confirmacion) 

@app.route("/sobre-mi")
def sobre_mi():
    return render_template("sobre_mi.html")

# --- RUTA DINÁMICA CON FILTRO ---
@app.route("/<categoria>")
def ver_categoria(categoria):
    # 1. Conectamos a la BD
    conexion = sqlite3.connect(DB_PATH)
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()

    # 2. Atrapamos el filtro de la URL si es que existe
    sub_filtro = request.args.get('filtro')

    # 3. Condicionamos la búsqueda SQL
    if sub_filtro:
        # Si hay filtro, buscamos categoría Y subcategoría
        cursor.execute("SELECT * FROM proyectos WHERE categoria_principal = ? AND subcategoria = ?", (categoria, sub_filtro))
    else:
        # Si no hay filtro, traemos todo de esa categoría
        cursor.execute("SELECT * FROM proyectos WHERE categoria_principal = ?", (categoria,))

    proyectos_encontrados = cursor.fetchall()
    conexion.close()

    # 4. Pasamos el filtro actual al HTML para saber qué pestaña "iluminar"
    return render_template("categoria.html", 
                         nombre_categoria=categoria, 
                         lista_proyectos=proyectos_encontrados, 
                         filtro_actual=sub_filtro)

@app.route("/proyecto/<int:id>")
def detalle_proyecto(id):
    conexion = sqlite3.connect(DB_PATH)
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()

    # Buscamos el proyecto específico por su ID
    cursor.execute("SELECT * FROM proyectos WHERE id = ?", (id,))
    proyecto = cursor.fetchone()
    conexion.close()

    return render_template("detalle.html", proyecto=proyecto)

if __name__ == "__main__":
    
    app.run(debug=True)

    

