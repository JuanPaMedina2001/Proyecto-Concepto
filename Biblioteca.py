"""
Este proyecto simula una interfaz que utilizaría una biblioteca para
ayudar a los usuarios a encontrar los libros dentre de ella, además de poder
agregar libros nuevos y llevar un registro de las busquedas recientes.

Creado por: Juan Pablo Medina O'Farrill
Matrícula: A01702724
Proyecto: Pensamiento Computacional
"""



"""
============================== Bibliotecas extras ==============================
"""

from tkinter import * # Para crear la interfaz
from datetime import datetime #Para conseguir el formato de fechas
from pytz import timezone # Para conseguir la fecha y hora local





"""
============================== Funciones a utilizar ============================
"""

def buscar(): # Encontrar un libro utilizando una palabra clave
# (Uso de cadenas de texto, operadores, for, if y variables)

""" Empezamos creando la ventana donde apareceran los resutados de la busqueda"""

    clave = buscadorEntry.get() #Sacamos la clave de la entrada de texto del buscador
    buscarWindow = Toplevel() # Creamos la ventana
    buscarWindow.title('Resultados de busqueda') # Le cambiamos el título
    buscarWindowText = Text(buscarWindow, height = 10, width=100) #Abrimos un espacio de texto
    buscarWindowText.insert(INSERT, 'Resultados para tu busqueda:\n\n') # Insertamos encabezado
    buscarWindowText.pack() # Metemos el espacio de texto dentro de la ventana.

""" Ahora buscaremos la palabra clave dentro de el archivo de texto con la
    biblioteca de libros entera e iremos checando libro por libro por la palabra
    clave, ya sea Año, Autor o Título """

    if len(clave) >= 1: # Asegurarse de que haya escrito texto.
        c = 0 # Iniciamos counter
        handle = open('Libros.txt') # Abrimos archivo de texto
        for line in handle: # Checamos cada linea del archivo
            line = line.rstrip() # Evitamos que se impriman más lineas juntas.
            if clave in line: # Comprobamos que la palabra clave esté en la linea
                index1 = line.find('Tít:')
                titulo=index1 + 5 # Indice del título
                index2 = line.find('Aut:')
                autor = index2 + 5 # Indice del Autor
                index3 = line.find('Year:')
                año = index3 + 6 # Inidce del Año
                c = c + 1 # Añadimos 1 al counter por cada libro que coincida.
                buscarWindowText.insert(END, '\t'+str(c)+') '+line[titulo:index3-2]+' - '+
                line[autor:index1-2]+' - '+line[año:]+'\n')
                # Añadimos todo lo que hayamos encontrado al espacio de texto en la ventana.
        c = str(c)
        buscarWindowText.insert(END, '\nHe encontrado '+ c + ' resultados para: ' + clave+ '\n')
        agregar_historial(clave, c) # Agregaremos la busqueda hecha al historial de busquedas.

"""-----------------------------------------------------------------------------"""

def agregar(): # Añadir un libro nuevo al archivode texto.
# (Uso de variables, archivos y cadenas de texto)

""" Añadiremos libros nuevos al archivo de texto donde estan todos los libros"""

    autor = agregarAutorE.get() # Sacamos el nombre del Autor de la entrada de texto.
    titulo = agregarTituloE.get() # Tambien el Título.
    año = agregarAnoE.get() # Y por último el Año.
    handle = open('Libros.txt', 'a') # Abrimos el documento donde estan todos los libros en modo append.
    handle.write('Aut: '+ autor +', ' + 'Tít: ' + titulo + ', ' + 'Year: ' + año + '\n')
    # Añadimos todo lo que escribimos al archivo.

""" Lo siguiente le hará saber a el usuario que su libro ha sido añadido exitosamente al documento"""

    agregarAnadidoL.grid(row=6, column=2, columnspan=2) # Avisamos que se añadió.
    agregarAutorE.delete(0,END) # Borrar todo lo que esté en las entradas de texto.
    agregarAnoE.delete(0,END)
    agregarTituloE.delete(0,END)

"""-----------------------------------------------------------------------------"""

def entero(): # Mostrar la biblioteca entera de libros.
# (Uso de variables, for y cadenas de texto)

""" Esta función le mostrará a el usuario todos los libros de la biblioteca
    Empezamos creando una ventana nueva."""

    enteroWindow = Toplevel() # Creamos ventana nueva.
    enteroWindow.title('Biblioteca Entera') # Le cambiamos el título
    enteroWindowText = Text(enteroWindow, width=100) # Cremos un bloque de texto
    enteroWindowText.insert(INSERT, 'Biblioteca de libros:\n\n') # Agregamos encabezado.
    enteroWindowText.pack() # Metemos el bloque en la ventana.

    c = 0
    handle = open('Libros.txt') # Abre el archivo con todos los libros.
    for line in handle: # Consigue cada una de las lineas/libros.
        line = line.rstrip()
        index1 = line.find('Tít:')
        titulo=index1 + 5 # Indice Título
        index2 = line.find('Aut:')
        autor = index2 + 5 # Indice Autor
        index3 = line.find('Year:')
        año = index3 + 6 # Inidce Año
        c = c + 1 # # Añadimos 1 al counter por cada libro.
        enteroWindowText.insert(END, '\t'+str(c)+') '+line[titulo:index3-2]+' - '
        +line[autor:index1-2]+' - '+line[año:]+'\n') # Le damos un formato amigable
        # Mostramos en el bloque de texto cada una de los libros en la biblioteca.
    c = str(c)
    enteroWindowText.insert(END, '\nExisten '+ c+ ' libros en la biblioteca.\n')
    # Numero de libros en la biblioteca.

"""-----------------------------------------------------------------------------"""

def resumido(): # Mostrar la biblioteca entera de una manera resumida.
# (Uso de archivos, variables, diccionarios, for y cadenas de texto)

""" Tal vez el usuario quiera ver todos los libros pero de manera resumida,
    para eso utilizamos esta opcion la cual solo muestra la cantidad de libros
    por autor"""

    resumenWindow = Toplevel() # Creamos una ventana nueva
    resumenWindow.title('Biblioteca Resumida') # Le cambiaos el título
    resumenWindowText = Text(resumenWindow, width=50) # Abrimos un bloque de texto
    resumenWindowText.insert(INSERT, 'Biblioteca de libros:\n\n') # Le agregamos un encabecado
    resumenWindowText.pack() # Mostramos el bloque de texto en la ventana.

""" Vamos a utilizar diccionarios para guardar el nombre del autor con su cantidad
    de libros en un estilo de histograma que podamos mostrar de manera textual al
    usuario """

    handle = open('Libros.txt') # Abrimos el archivo con los libros.
    for line in handle: # Checamos cada linea/libro
        index = line.find('Tít:')
        y = line[5:index-2] # Le sacamos el Autor a cada Libro.
        dic[y] = dic.get(y,0) + 1 # Añadimos el Autor y # de libro al diccionario, si no existe empieza de 0.
    for keys,values in sorted(dic.items()): # Ordena todo de manera alfabética.
        resumenWindowText.insert(END, '\t'+str(keys)+' - '+str(values)+' libros.'+'\n')
        # Mostramos todo en el bloque de texto dentro de la ventna.

"""-----------------------------------------------------------------------------"""

def ver(): # Decidir qué tipo de resumen ver.
# (Uso de if y funciones)

""" En la interfaz pricipal hay un checkbox que le dejará al usuario decidir
    cómo ver el resumen de libros de la biblioteca, resumida o no. Hay que
    checar qué es lo que decidió"""

    if resumen.get() == 1: # Revisamos si el checkbox está seleccionado o no.
        resumido() # corremos resumido si está seleccionado,
    else:
        entero() # y entero si no lo está.

"""-----------------------------------------------------------------------------"""

def agregar_historial(clave, reps): #Recibe la clave buscada y los libros encontrados.
# (Uso de variables, listas y listas anidadas)

    """ Esta función trabaja junto con la función de buscar para agregar las
    palabras claves a el hitorial de busquedas que el usuario pueda abrir
    desde el menú pricipal."""

    zona_horaria = timezone('America/Monterrey') # Conseguimos la zona horaria local
    fecha_hora = datetime.now(zona_horaria) # Sacamos la fecha y hora de la ZHL.
    fecha_hora_formato = fecha_hora.strftime("%B %d, %Y %H:%M:%S") # Se le da un formato
    value = [fecha_hora_formato, clave, reps] # lista con la fecha/hora, la clave buscada y los libros encontrados.
    historial.append(value) # Se agregan a la lista hitorial. SE OCUPAN LISTAS ANIDADAS.

"""-----------------------------------------------------------------------------"""

def ver_historial(): #Mostrarle al usuario su historial de busqueda.
# (Uos de variables, for, listas anidadas y cadenas de texto)

    """ Ahora sí, debemos mostrarle al usuario todas las búsquedas que ha hecho
    desde que se abrió el buscador, para eso sacaremos los datos de una Lista
    anidada que se hizo en la función anterior"""

    histWindow = Toplevel() # Creamos ventana nueva
    histWindow.title('Historial de Busqueda') # Le cambiamos el título.
    histWindowText = Text(histWindow, width=100) # Añadimos un bloque de texto
    histWindowText.insert(INSERT, 'Historial:\n\n') # Ponemos un encabezado
    histWindowText.pack() # Ponemos el bloque de texto dentro de la ventana.


    for busqueda in historial: # Conseguimos todas las listas dentro de la lista más grande.
        hora = busqueda[0] # Sacamos la hora/fecha
        clave = busqueda[1] # Sacamos la clave buscada
        reps = busqueda[2] # Sacamos la cantidad de libros encontrados
        histWindowText.insert(END, '\tFecha: '+hora+" - Busqueda: "+clave+" - Resultado: "+reps+" libros\n")
        # Lo ponemos en un formato más amigable dentro del bloque de texto.

"""-----------------------------------------------------------------------------"""

def salir(): # Fucnión para cerrar el programa.

    exit()





"""
============================ Constantes del programa ===========================
"""

historial = list() #Abrimos la lista para el historial
dic = dict() # Abrimos el diccionario para el historgrama del resumen de libros.





"""
============================== Interfaz principal ==============================
"""

"""--------------------------- Ventana principal -------------------------------"""
root = Tk() # Abrimos ventana Principal
root.title('Biblioteca de Jp') # Le cambiamos el título

"""-------------------------- Título del programa ------------------------------"""

"""La forma de ordenar los elementos en la ventana será utilizando un grid,
    es decir, una serie de celdas en el que los elementos pueden ocupar una o
    varias de esas celdas de forma que todo que de ordenado. """

titulo = Label(root, text='Bienvenido a la Biblioteca') #Título del programa
titulo.grid(row=0, columnspan=4) # Lo colocamos en grid

"""-------------------------- Sistema de busqueda ------------------------------"""

""" Para el sistema de búsqueda, crearemos una entrada de texto donde el usuraio
    pueda escribir lo que quiera encontrar, además de dos botones, uno para empezar
    la busqueda y otro par apoder ver su historial de busquedas, cada boton tiene
    un enlace directo a la función que debe realizar al ser pulsado."""

buscadorLabel = Label(root, text='Buscar Libro') # Subtitulo
buscadorEntry = Entry(root) # Entrada de texto par aescribir lo que se va a buscar.
buscadorButton = Button(root, text='Buscar', command=buscar) # Botón buscar.
historialButton = Button(root, text="Historial", command=ver_historial) #Botón historial.

buscadorLabel.grid(row=1, column=0, columnspan=2) # Lo colocamos en grid
buscadorEntry.grid(row=2, column=0, columnspan=2)# Lo colocamos en grid
buscadorButton.grid(row=3, column=0)# Lo colocamos en grid
historialButton.grid(row=3, column=1)# Lo colocamos en grid

"""------------------------ Sistema de agregar libros ---------------------------"""

""" Para poder agregar libros, hubo que abrir tres entradas de texto, cada una
    para uno de los datos que se agregaran al documento de texto con los demás
    de los libros. Al final hay un botón para agregar el libro que correrá la
    función de agregar."""

agregarLabel = Label(root, text='Añadir Libro') #Subtítulo
agregarAutorL = Label(root, text='Autor') # Esta etiqueta irá al lado de la entrada de texto.
agregarTituloL = Label(root, text='Título')# Esta etiqueta irá al lado de la entrada de texto.
agregarAnoL = Label(root, text='Año')# Esta etiqueta irá al lado de la entrada de texto.
agregarAutorE = Entry(root) # Entrada de texto para Autor.
agregarTituloE = Entry(root)# Entrada de texto para Título.
agregarAnoE = Entry(root)# Entrada de texto para Año.
agregarButton = Button(root, text='Añadir', command=agregar) # Botón de agregar.
agregarAnadidoL = Label(root, text='Añadido', fg='red') # Etiqueta que estará oculta hasta que se añada el libro.

agregarLabel.grid(row=1, column=2, columnspan=2)# Lo colocamos en grid
agregarAutorL.grid(row=2, column=2)# Lo colocamos en grid
agregarAnoL.grid(row=4, column=2)# Lo colocamos en grid
agregarTituloL.grid(row=3, column=2)# Lo colocamos en grid
agregarTituloE.grid(row=3, column=3)# Lo colocamos en grid
agregarAutorE.grid(row=2, column=3)# Lo colocamos en grid
agregarAnoE.grid(row=4, column=3)# Lo colocamos en grid
agregarButton.grid(row=5, column=2, columnspan=2)# Lo colocamos en grid

"""-------------------------- Ver todos los libros -----------------------------"""

""" Una pequeña sección de la interfaz principal para seleccionar qué tipo de
    vista de los libros quiere ver el usuario. Esta sección tiene un checkbox
    que el usuario puede seleccionar para cambiar el tipo de vista que quiere ver.
    El checkbox funciona en binario, es decir, si esta seleccionado (1) o no (0)."""

resumen = IntVar() # Inicia la variable resumen en formato de entero. Guardará el estatus del checkbox.
verButton = Button(root, text='Ver todo', command=ver) # Botón para iniciar la vista de la biblioteca.
verCheck = Checkbutton(root, text='Resumir', variable = resumen, onvalue=1, offvalue=0)
# Creamos el checkbox el cual puede estar seleccionado o no, y es evalor se guardará en la variable resumen.

verButton.grid(row=5, column=0)# Lo colocamos en grid
verCheck.grid(row=5, column=1)# Lo colocamos en grid

"""--------------------------- Salir del programa ------------------------------"""

""" Un sencillo botón al pie de la interfaz para terminar el programa, cuando
    este se seleccione, el historial se borrará y todo se cerrará"""

salirButton = Button(root, text='Salir', command=salir) #Crear botón para salir.
salirButton.grid(row=6, column=0, columnspan=4) # Lo colocamos en grid

root.mainloop() # Esto solo mantendrá el programa abierto hasta que salga manualmente.





"""
======================== Referencias de Autoaprendizaje ========================

Libro "Python for Everybody" de Charles R. Severance (2009). Atualizado a Python3
    en 2015

MOOC "Python for Everybody" Modulo 1 y 2 de Michigan Univerity atraves de coursera.com
cursado en Junio-Julio 2020

Tutorialspoint (2020) "Python 3 - GUI Programming (Tkinter)" URL:
    https://www.tutorialspoint.com/python3/python_gui_programming.htm ,
    revisado en Septiembre 2020

thenewboston (2014) "Python GUI with Tkinter" episodios 1-8, YouTube, URL:
    https://www.youtube.com/watch?v=RJB1Ek2Ko_Y , revisado en Septiembre 2020.

"""
