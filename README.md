# Proyecto Biblioteca Virtual - Concepto

## Definición
El proyecto consiste en crear una mini base de datos que cualquier secretario de biblioteca o usuario de tal pueda ocupar para encontrar un libro o varios libros dentro de la misma biblioteca. El punto pricipal es crear una interfaz sencilla en la que se pueda escribir una busqueda exacta, agregar libros a la biblioteca, o ver la biblioteca entera, incluso guardar un historial de busquedas del usuario. 

## Elementos Extra
El programa usara un archivo local donde se guarden todos los libros, en conjunto con sus autores y el año de publicación. Durante el código se abrirá ese archivo y se utilizará para buscar los libros, y además agregar nuevos. 

Utilizarémos 3 bibliotecas distintas; Tkinter para crear la interfaz, Pytz para conseguir la hora y la fecha, y Datetime para darle el formato correcto. Estas últimas 2 tienen el propósito de poderle mostrar al usuario la hora y la fecha de sus busquedas en el historial. Con Tkinter usaremos los elementos de Toplevel, Button, Label, Checkbutton, Text, etc. para crear ventanas donde se mostrará la información y los controles de la biblioteca. 

## Funciones
El programa lleva diferentes funciones:

buscar(): Abrirá el archivo de texto y usará la palabra clave para buscar en él todos los libros que concuerden con la palabra clave.

agregar(): Tomará 3 parametros: la Fecha de publicación, el Título del libro y el nombre y apellido del Autor, y ocupando esas tres cosas creará una nueva entrada el archivo de texto.

ver(): Esta función se divide en dos: enter() y resumido(), en el que el usuario puede ver todos los libros en la biblioteca, el entero mostrará todos los libros individualmente de manera alfabética, y el resumido mostrará todos los autores con la cantidad de libros que tiene cada uno también ordenados alfabéticamente.

ver_historial(): Le mostrará al usuario unaventana donde pueden ver todas las busquedas que han hecho desde que se abrió el busquador junto con la hora y la fecha de la busqueda.
 
agregar_hitorial(): Trabaja en colaboración con buscar() para añadir cada una de las busquedas a la lista de historial junto con su hora y la cantidad d e libros que se encontraron.


## Instrucciones

Para correr el programa es necesario bajar los documentos: Biblioteca.py y el achivo de texto Libros.txt del repositorio. Es necasario que ambos archivos esten ubicados en la misma dirección o carpeta en el ordenador del usuario. Depues correr desde la terminal, escribir la direccion de los archivos y el codigo python3 Biblioteca.py
