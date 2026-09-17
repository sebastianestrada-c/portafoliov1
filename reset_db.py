import sqlite3
import os

# Rutas absolutas inquebrantables
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "portafolio.db")

def reiniciar_todo():
    # 1. Destruimos la base de datos vieja si existe (Adiós errores)
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print("Base de datos anterior eliminada. Empezando en limpio...")

    # 2. Conectamos y creamos el archivo nuevo en el lugar exacto
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    # 3. Creamos la tabla de proyectos
    cursor.execute("""
        CREATE TABLE proyectos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            categoria_principal TEXT NOT NULL,
            subcategoria TEXT NOT NULL,
            descripcion TEXT,
            imagen_url TEXT NOT NULL,
            archivo_pdf TEXT,
            video_url TEXT
        )
    """)

    # Creamos también la tabla de contacto
    cursor.execute("""
        CREATE TABLE mensajes_contacto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            mensaje TEXT NOT NULL,
            fecha DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # 4. Inyectamos tus proyectos
    proyectos_semilla = [
        # --- FOTOGRAFÍA: Naturaleza ---
        ("Insecto bajo el sol", "fotografia", "naturaleza", "Grillo en el Mirador Picacho sierra de Guadalupe. Estado de México", "/static/img/fotografia/naturaleza/cerro/a1.jpg", None, None),
        ("La luz en el cerro", "fotografia", "naturaleza", "Interior de la sierra de Guadalupe", "/static/img/fotografia/naturaleza/cerro/a2.jpg", None, None),
        ("Mariposa en planta", "fotografia", "naturaleza", "Mariposa en el Parque Estatal Sierra de Guadalupe. Estado de México", "/static/img/fotografia/naturaleza/cerro/a3.jpg", None, None),
        ("Mariposas juntas", "fotografia", "naturaleza", "Mariposas en el Parque Estatal Sierra de Guadalupe. Estado de México", "/static/img/fotografia/naturaleza/cerro/a4.jpg", None, None),
        ("Mariposa total", "fotografia", "naturaleza", "Otra mariposa en el Parque Estatal Sierra de Guadalupe. Estado de México", "/static/img/fotografia/naturaleza/cerro/a5.jpg", None, None),

        ("Lagartija sobre madera", "fotografia", "naturaleza", "Lagartija en las cercanías del Monte Tláloc. Estado de México", "/static/img/fotografia/naturaleza/lagartijas/b1.jpg", None, None),
        ("Lagartija tomando sol", "fotografia", "naturaleza", "Lagartija en las cercanías del Monte Tláloc", "/static/img/fotografia/naturaleza/lagartijas/b2.jpg", None, None),
        ("Lagartija tomando sol", "fotografia", "naturaleza", "Lagartija en las cercanías del Monte Tláloc", "/static/img/fotografia/naturaleza/lagartijas/b3.jpg", None, None),
        ("Lagartijas tomando sol", "fotografia", "naturaleza", "Lagartijas en las cercanías del Monte Tláloc", "/static/img/fotografia/naturaleza/lagartijas/b4.jpg", None, None),
        ("Lagartilla sobre tronco", "fotografia", "naturaleza", "Lagartija en las cercanías del Monte Tláloc", "/static/img/fotografia/naturaleza/lagartijas/b5.jpg", None, None),

        ("Rosa", "fotografia", "naturaleza", "Flor en Coyoacán", "/static/img/fotografia/naturaleza/plantas/c1.jpg", None, None),
        ("Planta en Monte Tlaloc", "fotografia", "naturaleza", "Plantas y flores en las cercanías del Monte Tláloc", "/static/img/fotografia/naturaleza/plantas/c2.jpg", None, None),
        ("Vegetación en Monte Tlaloc", "fotografia", "naturaleza", "Plantas y flores en las cercanías del Monte Tláloc", "/static/img/fotografia/naturaleza/plantas/c3.jpg", None, None),
        ("Hongo en Monte Tlaloc", "fotografia", "naturaleza", "Plantas y flores en las cercanías del Monte Tláloc", "/static/img/fotografia/naturaleza/plantas/c5.jpg", None, None),
        ("Flor en Monte Tlaloc", "fotografia", "naturaleza", "Plantas y flores en las cercanías del Monte Tláloc", "/static/img/fotografia/naturaleza/plantas/c6.jpg", None, None),
        ("Rosa en la ciudad", "fotografia", "naturaleza", "Plantas y flores en las cercanías del Monte Tláloc", "/static/img/fotografia/naturaleza/plantas/c7.jpg", None, None),

        # --- FOTOGRAFÍA: Retrato ---
        ("Determinación", "fotografia", "retrato", "Sesión fotográfica escolar. La muerte en diferentes culturas. Incas", "/static/img/fotografia/retrato/inca/d1.jpg", None, None),
        ("Meditación", "fotografia", "retrato", "Sesión fotográfica escolar. La muerte en diferentes culturas. Incas", "/static/img/fotografia/retrato/inca/d2.jpg", None, None),
        ("Movimiento", "fotografia", "retrato", "Sesión fotográfica escolar. La muerte en diferentes culturas. Incas", "/static/img/fotografia/retrato/inca/d3.jpg", None, None),

        ("En llamada", "fotografia", "retrato", "Sesión fotográfica escolar. pinup", "/static/img/fotografia/retrato/pinup/pinup1.jpg", None, None),
        ("Contestando la llamada", "fotografia", "retrato", "Sesión fotográfica escolar. pinup", "/static/img/fotografia/retrato/pinup/pinup2.jpg", None, None),
        ("Soda", "fotografia", "retrato", "Sesión fotográfica escolar. pinup", "/static/img/fotografia/retrato/pinup/pinup3.jpg", None, None),

        ("Práctica 1", "fotografia", "retrato", "Prácticas fotográficas escolares.", "/static/img/fotografia/retrato/practicasestudio/f1.jpg", None, None),
        ("Práctica 2", "fotografia", "retrato", "Prácticas fotográficas escolares.", "/static/img/fotografia/retrato/practicasestudio/f2.jpg", None, None),
        ("Práctica 3", "fotografia", "retrato", "Prácticas fotográficas escolares.", "/static/img/fotografia/retrato/practicasestudio/f3.jpg", None, None),
        ("Autoretrato 1", "fotografia", "retrato", "Prácticas fotográficas escolares.", "/static/img/fotografia/retrato/practicasestudio/f4.jpg", None, None),
        ("Autoretrato 2", "fotografia", "retrato", "Prácticas fotográficas escolares.", "/static/img/fotografia/retrato/practicasestudio/f5.jpg", None, None),

        ("Retrato 1", "fotografia", "retrato", "Sesión fotográfica junto con colega @shutterfabs.", "/static/img/fotografia/retrato/rana/r1.jpg", None, None),
        ("Retrato 2", "fotografia", "retrato", "Sesión fotográfica junto con colega @shutterfabs.", "/static/img/fotografia/retrato/rana/r2.jpg", None, None),
        ("Retrato 3", "fotografia", "retrato", "Sesión fotográfica junto con colega @shutterfabs.", "/static/img/fotografia/retrato/rana/r3.jpg", None, None),
        ("Retrato 4", "fotografia", "retrato", "Sesión fotográfica junto con colega @shutterfabs.", "/static/img/fotografia/retrato/rana/r4.jpg", None, None),
        ("Retrato 5", "fotografia", "retrato", "Sesión fotográfica junto con colega @shutterfabs.", "/static/img/fotografia/retrato/rana/r5.jpg", None, None),

        # --- FOTOGRAFÍA: Social ---
        ("Cruz", "fotografia", "social", "Día de muertos en Tlatelolco.", "/static/img/fotografia/social/s1.jpg", None, None),
        ("Altar", "fotografia", "social", "Día de muertos en Tlatelolco.", "/static/img/fotografia/social/s2.jpg", None, None),
        ("Tlalocan 1", "fotografia", "social", "Aquifera: Festival del Bosque de Chapultepec 2026.", "/static/img/fotografia/social/s3.jpg", None, None),
        ("Stickers en la ciudad", "fotografia", "social", "Aquifera: Festival del Bosque de Chapultepec 2026.", "/static/img/fotografia/social/s4.jpg", None, None),
        ("Danzante", "fotografia", "social", "Aquifera: Festival del Bosque de Chapultepec 2026.", "/static/img/fotografia/social/s5.jpg", None, None),
        ("Tlalocan 1.2", "fotografia", "social", "Aquifera: Festival del Bosque de Chapultepec 2026.", "/static/img/fotografia/social/s6.jpg", None, None),
        ("Tlalocans", "fotografia", "social", "Aquifera: Festival del Bosque de Chapultepec 2026.", "/static/img/fotografia/social/s7.jpg", None, None),
        ("Danzante 2", "fotografia", "social", "Aquifera: Festival del Bosque de Chapultepec 2026.", "/static/img/fotografia/social/s8.jpg", None, None),
        ("Tlalocan 2", "fotografia", "social", "Aquifera: Festival del Bosque de Chapultepec 2026.", "/static/img/fotografia/social/s9.jpg", None, None),

        # --- DISEÑO ---
        ("Revista 7a", "diseno", "editorial", "Revista 7a. Revista de las 7 artes. Trabajo en Equipo escolar.", "/static/img/diseno/7a/REVISTA 7A_Página_01.jpg", "/static/img/diseno/7a/revista7a.pdf", None),
        ("Mochileando con estilo", "diseno", "branding", "Rediseño agencia de viajes Mochileando con estilo. Proyecto escolar en equipo", "/static/img/diseno/mochileando/portada1.jpg", "/static/img/diseno/mochileando/moch.pdf", None),
        ("Microacción", "diseno", "branding", "Rediseño de identidad para programa Microacción.", "/static/img/diseno/microaccion/p1.jpg", "/static/img/diseno/microaccion/midentm.pdf", None),
        ("Plantilla CREA Earthgonomic México A.C.", "diseno", "editorial", "Diseño de plantilla editorial CREA.", "/static/img/diseno/plantilla/port1.jpg", "/static/img/diseno/plantilla/Plantilla Editorial CREA.pdf", None),

        # --- AUDIOVISUAL ---
        ("Ejemplos redes sociales 1", "audiovisual", "redes", "Contenido vertical para redes sociales.", "/static/img/audiovisual/jpeg/j1.jpg", None, "https://www.youtube.com/embed/8aPCwXDgQJc"),
        ("Ejemplos redes sociales 2", "audiovisual", "redes", "Contenido vertical para redes sociales", "/static/img/audiovisual/jpeg/j2.jpg", None, "https://www.youtube.com/embed/Wq3PuqT6rjI"),
        ("Ejemplos redes sociales 3", "audiovisual", "redes", "Contenido vertical para redes sociales", "/static/img/audiovisual/jpeg/j3.jpg", None, "https://www.youtube.com/embed/2b6LgfDSN_s"),
        ("Ejemplos redes sociales 4", "audiovisual", "redes", "Contenido vertical para redes sociales", "/static/img/audiovisual/jpeg/j0.jpg", None, "https://www.youtube.com/embed/gL37aRxe_hM"),
        ("Sistema solar (3d)", "audiovisual", "otros", "Trabajo escolar sistema solar", "/static/img/audiovisual/jpeg/j4.jpg", None, "https://www.youtube.com/embed/VCKu4GE9WTw")
    ]

    cursor.executemany("""
        INSERT INTO proyectos (titulo, categoria_principal, subcategoria, descripcion, imagen_url, archivo_pdf, video_url)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, proyectos_semilla)

    conexion.commit()
    conexion.close()
    print("¡Éxito total! Tablas creadas y proyectos sembrados correctamente.")

if __name__ == "__main__":
    reiniciar_todo()