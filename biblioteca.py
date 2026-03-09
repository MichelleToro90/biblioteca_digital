class Biblioteca:

    def __init__(self):

        # Diccionario de libros
        self.libros = {}

        # Diccionario de usuarios
        self.usuarios = {}

        # Conjunto para IDs únicos
        self.ids_usuarios = set()

    def añadir_libro(self, libro):

        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            return "Libro añadido"
        else:
            return "El libro ya existe"

    def registrar_usuario(self, usuario):

        if usuario.id_usuario not in self.ids_usuarios:

            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            return "Usuario registrado"

        return "ID duplicado"

    def prestar_libro(self, isbn, id_usuario):

        if isbn not in self.libros:
            return "Libro no encontrado"

        if id_usuario not in self.usuarios:
            return "Usuario no encontrado"

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        if libro.disponible:

            libro.disponible = False
            usuario.prestar_libro(libro)

            return "Libro prestado"

        return "Libro no disponible"

    def devolver_libro(self, isbn, id_usuario):

        libro = self.libros.get(isbn)
        usuario = self.usuarios.get(id_usuario)

        if libro and usuario:

            if libro in usuario.libros_prestados:

                usuario.devolver_libro(libro)
                libro.disponible = True

                return "Libro devuelto"

        return "Error en devolución"