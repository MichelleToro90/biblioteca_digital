# biblioteca_digital

# 📚 Sistema de Gestión de Biblioteca Digital

## Descripción

Este proyecto es un **Sistema de Gestión de Biblioteca Digital** desarrollado en **Python** utilizando **Programación Orientada a Objetos (POO)** y una **interfaz gráfica con Tkinter**.

El sistema permite administrar libros, usuarios y préstamos dentro de una biblioteca digital de forma sencilla mediante una interfaz gráfica.

---

## 🎯 Objetivo

Desarrollar una aplicación que permita:

* Gestionar libros disponibles en una biblioteca.
* Registrar usuarios.
* Prestar y devolver libros.
* Visualizar el estado de los libros en una tabla de control.

---

## 🧠 Tecnologías utilizadas

* **Python 3**
* **Tkinter** (interfaz gráfica)
* **Programación Orientada a Objetos (POO)**

---

## 📁 Estructura del proyecto

```
biblioteca_digital/
│
├── libro.py        # Clase Libro
├── usuario.py      # Clase Usuario
├── biblioteca.py   # Lógica de gestión de biblioteca
├── interfaz.py     # Interfaz gráfica con Tkinter
├── main.py         # Punto de entrada del programa
└── README.md       # Documentación del proyecto
```

---

## 🧱 Clases del sistema

### 1. Libro

Representa un libro dentro de la biblioteca.

Atributos principales:

* título
* autor
* categoría
* ISBN
* estado (disponible / prestado)

Se utiliza una **tupla** para almacenar el título y el autor, ya que estos datos no cambian.

---

### 2. Usuario

Representa un usuario registrado en la biblioteca.

Atributos:

* nombre
* ID de usuario
* lista de libros prestados

Se utiliza una **lista** para almacenar los libros que el usuario tiene prestados.

---

### 3. Biblioteca

Es la clase principal que gestiona:

* libros
* usuarios
* préstamos

Estructuras utilizadas:

* **Diccionario:** para almacenar libros usando el ISBN como clave.
* **Conjunto (set):** para garantizar IDs únicos de usuarios.
* **Listas:** para gestionar préstamos.

---

## ⚙️ Funcionalidades

El sistema permite realizar las siguientes acciones:

✔ Agregar libros
✔ Registrar usuarios
✔ Prestar libros
✔ Devolver libros
✔ Visualizar libros en una tabla de control
✔ Mostrar el estado del libro (Disponible / Prestado)

---

## 🖥 Interfaz gráfica

La interfaz fue desarrollada con **Tkinter** y permite interactuar con el sistema mediante botones y campos de entrada.

Incluye:

* Formulario para agregar libros
* Registro de usuarios
* Sistema de préstamo y devolución
* Tabla visual de libros disponibles

---

## ▶️ Cómo ejecutar el programa

1. Clonar o descargar el proyecto.

2. Abrir la carpeta en **Visual Studio Code**.

3. Ejecutar el archivo principal:

```bash
python main.py
```

4. Se abrirá la ventana del sistema de biblioteca.

---

## 📌 Ejemplo de uso

1. Agregar un libro con título, autor, categoría e ISBN.
2. Registrar un usuario.
3. Prestar un libro ingresando el ISBN y el ID del usuario.
4. Ver el cambio de estado del libro en la tabla.

---

## 🚀 Posibles mejoras futuras

* Sistema de búsqueda de libros.
* Lista de usuarios registrados.
* Historial de préstamos.
* Mejor diseño de la interfaz.
* Conexión con base d

