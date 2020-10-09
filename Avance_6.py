# Bibliotecas

from tkinter import *
from datetime import datetime
from pytz import timezone

#Funciones

def buscar():
    clave = buscadorEntry.get()
    buscarWindow = Toplevel()
    buscarWindow.title('Resultados de busqueda')
    buscarWindowText = Text(buscarWindow, height = 10, width=100)
    buscarWindowText.insert(INSERT, 'Resultados para tu busqueda:\n\n')
    buscarWindowText.pack()
    if len(clave) >= 1: # If / Operadores
        c = 0
        handle = open('Libros.txt') #Archivos
        for line in handle: # For
            line = line.rstrip() #Strings
            if clave in line: # If
                index1 = line.find('Tít:')
                titulo=index1 + 5
                index2 = line.find('Aut:')
                autor = index2 + 5
                index3 = line.find('Year:')
                año = index3 + 6
                c = c + 1 # Opreadores
                buscarWindowText.insert(END, '\t'+str(c)+') '+line[titulo:index3-2]+' - '+line[autor:index1-2]+' - '+line[año:]+'\n')
        c = str(c)
        buscarWindowText.insert(END, '\nHe encontrado '+ c + ' resultados para: ' + clave+ '\n')
        agregar_historial(clave, c)

def agregar():
    autor = agregarAutorE.get()
    titulo = agregarTituloE.get()
    año = agregarAnoE.get()
    handle = open('Libros.txt', 'a')
    handle.write('Aut: '+ autor +', ' + 'Tít: ' + titulo + ', ' + 'Year: ' + año + '\n') # Strings
    agregarAnadidoL.grid(row=6, column=2, columnspan=2)
    agregarAutorE.delete(0,END)
    agregarAnoE.delete(0,END)
    agregarTituloE.delete(0,END)

def entero():
    enteroWindow = Toplevel()
    enteroWindow.title('Biblioteca Entera')
    enteroWindowText = Text(enteroWindow, width=100)
    enteroWindowText.insert(INSERT, 'Biblioteca de libros:\n\n')
    enteroWindowText.pack()
    c = 0
    handle = open('Libros.txt') # Archivos
    for line in handle: # For
        line = line.rstrip() # Strings
        index1 = line.find('Tít:')
        titulo=index1 + 5 # Operadores
        index2 = line.find('Aut:')
        autor = index2 + 5 # Operadores
        index3 = line.find('Year:')
        año = index3 + 6 # Operadores
        c = c + 1 # Operadores
        enteroWindowText.insert(END, '\t'+str(c)+') '+line[titulo:index3-2]+' - '
        +line[autor:index1-2]+' - '+line[año:]+'\n')
    c = str(c)
    enteroWindowText.insert(END, '\nExisten '+ c+ ' libros en la biblioteca.\n')

def resumido():
    resumenWindow = Toplevel()
    resumenWindow.title('Biblioteca Resumida')
    resumenWindowText = Text(resumenWindow, width=50)
    resumenWindowText.insert(INSERT, 'Biblioteca de libros:\n\n')
    resumenWindowText.pack()
    dic = dict() # Diccionarios
    handle = open('Libros.txt') # Archivos
    for line in handle: # For
        index = line.find('Tít:') # Strings
        y = line[5:index-2]
        dic[y] = dic.get(y,0) + 1
    for keys,values in sorted(dic.items()): # For
        resumenWindowText.insert(END, '\t'+str(keys)+' - '+str(values)+' libros.'+'\n')

def ver():
    if resumen.get() == 1: # If
        resumido()
    else:
        entero()

def agregar_historial(clave, reps):
    zona_horaria = timezone('America/Monterrey')
    fecha_hora = datetime.now(zona_horaria)
    fecha_hora_formato = fecha_hora.strftime("%B %d, %Y %H:%M:%S")
    value = [fecha_hora_formato, clave, reps] # Listas anidadas
    historial.append(value)

def ver_historial():
    histWindow = Toplevel()
    histWindow.title('Historial de Busqueda')
    histWindowText = Text(histWindow, width=100)
    histWindowText.insert(INSERT, 'Historial:\n\n')
    histWindowText.pack()
    for busqueda in historial: # Listas anidadas / Strings / For
        hora = busqueda[0]
        clave = busqueda[1]
        reps = busqueda[2]
        histWindowText.insert(END, '\tFecha: '+hora+" - Busqueda: "+clave+" - Resultado: "+reps+" libros\n")

def salir():
    exit()

# Constantes
historial = list() #Listas

# Visuales

#Ventana 1
root = Tk()
root.title('Biblioteca de Jp')

#Título
titulo = Label(root, text='Bienvenido a la Biblioteca')
titulo.grid(row=0, columnspan=4)

#Buscar
buscadorLabel = Label(root, text='Buscar Libro')
buscadorEntry = Entry(root)
buscadorButton = Button(root, text='Buscar', command=buscar)
historialButton = Button(root, text="Historial", command=ver_historial)
buscadorLabel.grid(row=1, column=0, columnspan=2)
buscadorEntry.grid(row=2, column=0, columnspan=2)
buscadorButton.grid(row=3, column=0)
historialButton.grid(row=3, column=1)

#Añadir
agregarLabel = Label(root, text='Añadir Libro')
agregarAutorL = Label(root, text='Autor')
agregarTituloL = Label(root, text='Título')
agregarAnoL = Label(root, text='Año')
agregarAutorE = Entry(root)
agregarTituloE = Entry(root)
agregarAnoE = Entry(root)
agregarButton = Button(root, text='Añadir', command=agregar)
agregarAnadidoL = Label(root, text='Añadido', fg='red')
agregarLabel.grid(row=1, column=2, columnspan=2)
agregarAutorL.grid(row=2, column=2)
agregarAnoL.grid(row=4, column=2)
agregarTituloL.grid(row=3, column=2)
agregarTituloE.grid(row=3, column=3)
agregarAutorE.grid(row=2, column=3)
agregarAnoE.grid(row=4, column=3)
agregarButton.grid(row=5, column=2, columnspan=2)

#Ver
resumen = IntVar()
CheckVar1 = IntVar()
verButton = Button(root, text='Ver todo', command=ver)
verCheck = Checkbutton(root, text='Resumir', variable = resumen, onvalue=1, offvalue=0)
verButton.grid(row=5, column=0)
verCheck.grid(row=5, column=1)

#Salir
salirButton = Button(root, text='Salir', command=salir)
salirButton.grid(row=6, column=0, columnspan=4)

root.mainloop()
