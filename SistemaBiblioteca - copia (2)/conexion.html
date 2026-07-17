import sqlite3

# ==========================================
# CONECTAR A LA BASE DE DATOS
# ==========================================

conexion = sqlite3.connect("biblioteca.db")

# ==========================================
# CREAR EL CURSOR
# ==========================================

cursor = conexion.cursor()

# ==========================================
# CREAR LA TABLA LIBROS
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS libros(

    id_libro INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    autor TEXT,
    categoria TEXT,
    editorial TEXT,
    disponible INTEGER

)

""")

conexion.commit()

# ==========================================
# FUNCIÓN PARA GUARDAR UN LIBRO (CREATE)
# ==========================================

def guardar_libro(titulo, autor, categoria, editorial, disponible):

    cursor.execute("""
    INSERT INTO libros
    (titulo, autor, categoria, editorial, disponible)
    VALUES (?, ?, ?, ?, ?)
    """, (titulo, autor, categoria, editorial, disponible))

    conexion.commit()

# ==========================================
# FUNCIÓN PARA MOSTRAR LOS LIBROS (READ)
# ==========================================

def mostrar_libros():

    cursor.execute("SELECT * FROM libros")

    return cursor.fetchall()
