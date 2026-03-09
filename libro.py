class Libro:

    def __init__(self, titulo, autor, categoria, isbn):

        # Tupla para datos que no cambian
        self.info = (titulo, autor)

        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True

    def obtener_titulo(self):
        return self.info[0]

    def obtener_autor(self):
        return self.info[1]

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.info[0]} - {self.info[1]} ({estado})"