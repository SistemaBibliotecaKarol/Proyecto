import tkinter as tk
from tkinter import END
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from conexion import guardar_libro, mostrar_libros

# ==========================================
# VENTANA DEL SISTEMA
# ==========================================

def abrir_sistema():

    sistema = tk.Toplevel()

    sistema.title("Sistema de Gestión de Biblioteca")
    sistema.geometry("700x600")
    sistema.resizable(False, False)

    # ==========================================
    # TÍTULO
    # ==========================================

    titulo = tk.Label(
        sistema,
        text="SISTEMA DE GESTIÓN DE BIBLIOTECA",
        font=("Arial",16,"bold")
    )

    titulo.pack(pady=10)

    # ==========================================
    # TÍTULO DEL LIBRO
    # ==========================================

    lbl_titulo = tk.Label(sistema,text="Título")
    lbl_titulo.pack()

    txt_titulo = tk.Entry(sistema,width=40)
    txt_titulo.pack()

    # ==========================================
    # AUTOR
    # ==========================================

    lbl_autor = tk.Label(sistema,text="Autor")
    lbl_autor.pack()

    txt_autor = tk.Entry(sistema,width=40)
    txt_autor.pack()

    # ==========================================
    # CATEGORÍA
    # ==========================================

    lbl_categoria = tk.Label(sistema,text="Categoría")
    lbl_categoria.pack()

    txt_categoria = tk.Entry(sistema,width=40)
    txt_categoria.pack()

    # ==========================================
    # EDITORIAL
    # ==========================================

    lbl_editorial = tk.Label(sistema,text="Editorial")
    lbl_editorial.pack()

    txt_editorial = tk.Entry(sistema,width=40)
    txt_editorial.pack()

    # ==========================================
    # DISPONIBLE
    # ==========================================

    disponible = tk.IntVar()

    chk_disponible = tk.Checkbutton(
        sistema,
        text="Disponible",
        variable=disponible
    )

    chk_disponible.pack(pady=5)

    # ==========================================
    # FUNCIÓN REGISTRAR
    # ==========================================

    def registrar():

        guardar_libro(
            txt_titulo.get(),
            txt_autor.get(),
            txt_categoria.get(),
            txt_editorial.get(),
            disponible.get()
        )

        txt_titulo.delete(0,END)
        txt_autor.delete(0,END)
        txt_categoria.delete(0,END)
        txt_editorial.delete(0,END)

        disponible.set(0)

        lista.delete(1.0,END)

        lista.insert()
        END,
        "Libro registrado correctamente\n"

    # ==========================================
    # FUNCIÓN MOSTRAR LIBROS
    # ==========================================

    def mostrar():

        lista.delete(1.0, END)

        libros = mostrar_libros()

        for libro in libros:

            lista.insert(
                END,
                f"ID: {libro[0]}\n"
                f"Título: {libro[1]}\n"
                f"Autor: {libro[2]}\n"
                f"Categoría: {libro[3]}\n"
                f"Editorial: {libro[4]}\n"
                f"Disponible: {libro[5]}\n"
                "----------------------------\n"
            )

    # ==========================================
    # BOTÓN REGISTRAR
    # ==========================================

    btn_registrar = tk.Button(
        sistema,
        text="Registrar Libro",
        width=20,
        command=registrar
    )

    btn_registrar.pack(pady=5)

    # ==========================================
    # BOTÓN MOSTRAR
    # ==========================================

    btn_mostrar = tk.Button(
        sistema,
        text="Mostrar Libros",
        width=20,
        command=mostrar
    )

    btn_mostrar.pack(pady=5)

    # ==========================================
    # ÁREA DE TEXTO
    # ==========================================

    lista = tk.Text(
        sistema,
        width=75,
        height=12
    )

    lista.pack(pady=10)


# ==========================================
# INICIAR SESIÓN
# ==========================================

def iniciar_sesion():

    usuario = txt_usuario.get()
    contraseña = txt_password.get()

    lbl_mensaje.config(
        text=f"Bienvenido al Sistema, {usuario}"
    )

    abrir_sistema()


# ==========================================
# VENTANA LOGIN
# ==========================================

ventana = tk.Tk()

ventana.title("Sistema de Gestión de Biblioteca")
ventana.geometry("500x350")
ventana.resizable(False, False)

titulo = tk.Label(
    ventana,
    text="SISTEMA DE GESTIÓN DE BIBLIOTECA",
    font=("Arial",16,"bold")
)

titulo.pack(pady=20)

lbl_usuario = tk.Label(ventana,text="Usuario:")
lbl_usuario.pack()

txt_usuario = tk.Entry(ventana,width=30)
txt_usuario.pack()

lbl_password = tk.Label(ventana,text="Contraseña:")
lbl_password.pack()

txt_password = tk.Entry(
    ventana,
    show="*",
    width=30
)

txt_password.pack()

btn_ingresar = tk.Button(
    ventana,
    text="Iniciar Sesión",
    width=20,
    command=iniciar_sesion
)

btn_ingresar.pack(pady=10)

btn_salir = tk.Button(
    ventana,
    text="Salir",
    width=20,
    command=ventana.destroy
)

btn_salir.pack()

lbl_mensaje = tk.Label(
    ventana,
    text="",
    font=("Arial",11)
)

lbl_mensaje.pack(pady=15)(

ventana.mainloop()
        )


