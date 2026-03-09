import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from libro import Libro
from usuario import Usuario
from biblioteca import Biblioteca


def iniciar_interfaz():

    biblioteca = Biblioteca()

    ventana = tk.Tk()
    ventana.title("Biblioteca Digital")
    ventana.geometry("700x600")

    # -----------------------
    # TABLA DE LIBROS
    # -----------------------

    tabla = ttk.Treeview(ventana)

    tabla["columns"] = ("Titulo", "Autor", "Categoria", "Estado")

    tabla.column("#0", width=80)
    tabla.column("Titulo", width=120)
    tabla.column("Autor", width=120)
    tabla.column("Categoria", width=120)
    tabla.column("Estado", width=100)

    tabla.heading("#0", text="ISBN")
    tabla.heading("Titulo", text="Título")
    tabla.heading("Autor", text="Autor")
    tabla.heading("Categoria", text="Categoría")
    tabla.heading("Estado", text="Estado")

    tabla.pack(pady=20)

    # -----------------------
    # ACTUALIZAR TABLA
    # -----------------------

    def actualizar_tabla():

        for fila in tabla.get_children():
            tabla.delete(fila)

        for isbn, libro in biblioteca.libros.items():

            estado = "Disponible" if libro.disponible else "Prestado"

            tabla.insert(
                "",
                "end",
                text=isbn,
                values=(
                    libro.obtener_titulo(),
                    libro.obtener_autor(),
                    libro.categoria,
                    estado
                )
            )

    # -----------------------
    # FUNCIONES
    # -----------------------

    def agregar_libro():

        titulo = entry_titulo.get()
        autor = entry_autor.get()
        categoria = entry_categoria.get()
        isbn = entry_isbn.get()

        libro = Libro(titulo, autor, categoria, isbn)

        resultado = biblioteca.añadir_libro(libro)

        messagebox.showinfo("Resultado", resultado)

        actualizar_tabla()

    def registrar_usuario():

        nombre = entry_nombre.get()
        id_usuario = int(entry_id.get())

        usuario = Usuario(nombre, id_usuario)

        resultado = biblioteca.registrar_usuario(usuario)

        messagebox.showinfo("Resultado", resultado)

    def prestar_libro():

        isbn = entry_isbn_prestamo.get()
        id_usuario = int(entry_id_prestamo.get())

        resultado = biblioteca.prestar_libro(isbn, id_usuario)

        messagebox.showinfo("Resultado", resultado)

        actualizar_tabla()

    def devolver_libro():

        isbn = entry_isbn_dev.get()
        id_usuario = int(entry_id_dev.get())

        resultado = biblioteca.devolver_libro(isbn, id_usuario)

        messagebox.showinfo("Resultado", resultado)

        actualizar_tabla()

    # -----------------------
    # CAMPOS LIBRO
    # -----------------------

    tk.Label(ventana, text="Agregar Libro").pack()

    entry_titulo = tk.Entry(ventana)
    entry_titulo.pack()
    entry_titulo.insert(0, "Titulo")

    entry_autor = tk.Entry(ventana)
    entry_autor.pack()
    entry_autor.insert(0, "Autor")

    entry_categoria = tk.Entry(ventana)
    entry_categoria.pack()
    entry_categoria.insert(0, "Categoria")

    entry_isbn = tk.Entry(ventana)
    entry_isbn.pack()
    entry_isbn.insert(0, "ISBN")

    tk.Button(ventana, text="Guardar Libro", command=agregar_libro).pack(pady=5)

    # -----------------------
    # CAMPOS USUARIO
    # -----------------------

    tk.Label(ventana, text="Registrar Usuario").pack()

    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack()
    entry_nombre.insert(0, "Nombre")

    entry_id = tk.Entry(ventana)
    entry_id.pack()
    entry_id.insert(0, "ID")

    tk.Button(ventana, text="Registrar Usuario", command=registrar_usuario).pack(pady=5)

    # -----------------------
    # PRESTAR
    # -----------------------

    tk.Label(ventana, text="Prestar Libro").pack()

    entry_isbn_prestamo = tk.Entry(ventana)
    entry_isbn_prestamo.pack()
    entry_isbn_prestamo.insert(0, "ISBN")

    entry_id_prestamo = tk.Entry(ventana)
    entry_id_prestamo.pack()
    entry_id_prestamo.insert(0, "ID Usuario")

    tk.Button(ventana, text="Prestar", command=prestar_libro).pack(pady=5)

    # -----------------------
    # DEVOLVER
    # -----------------------

    tk.Label(ventana, text="Devolver Libro").pack()

    entry_isbn_dev = tk.Entry(ventana)
    entry_isbn_dev.pack()
    entry_isbn_dev.insert(0, "ISBN")

    entry_id_dev = tk.Entry(ventana)
    entry_id_dev.pack()
    entry_id_dev.insert(0, "ID Usuario")

    tk.Button(ventana, text="Devolver", command=devolver_libro).pack(pady=5)

    ventana.mainloop()