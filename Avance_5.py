import time         #Importa biblioteca de tiempo para controlar las esperas entre lineas

def buscar():           #Función para buscar libros.
    rep = True
    while rep == True:          #Comprobar si el usuario quiere repetir la función.
        clave = input('\n¿Qué busca?\nPuede ingresar Título, Autor o Año\n')
        time.sleep(1)
        if len(clave) >= 1:         #Asegura que no haya busquedas vacías.
            c = 0           #Inicia un counter para saber cuántos libros se muestran.
            handle = open('Libros.txt')         #Abre el archivo con los libros.
            for line in handle:         #Revisa cada linea de el documento.
                line = line.rstrip()
                if clave in line:           #Revisa que la clave esté en la linea buscada.
                    index1 = line.find('Tít:')
                    titulo=index1 + 5           #Coinsigue el Título.
                    index2 = line.find('Aut:')
                    autor = index2 + 5          #Consigue el Autor.
                    index3 = line.find('Year:')
                    año = index3 + 6            #Consigue el Año.
                    c = c + 1           #Suma al counter.
                    print('\t'+str(c)+') '+line[titulo:index3-2]+' - '+line[autor:index1-2]+' - '+line[año:])           #Muestra los resultados.
            print('\nHe encontrado', c, 'resultados para:', clave, '\n')            #Cantidad de libros encontrados.
        else:
            error()         #Mensaje de error en caso no se ingrese una busqueda.
            rep = False
            break           #Regresa a menu inicial.
        t = input('¿Volver a buscar?\n')
        t = t.capitalize()
        if t == 'No':
            rep = False         #Regresa a menu inicial.
        elif t == 'Sí' or t == 'Si':
            rep = True          #Repite búsqueda.
        else:
            error()         #Mensaje de error en caso de que no se ingrese lo deseado.
            break

def agregar():          #Función para agregar un libro a la biblioteca.
    rep = True
    while rep == True:          #Comprobar si el usuario quiere repetir la función.
        autor = input('\nIngrese Autor\n')
        titulo = input('Ingrese Título\n')
        año = input('Ingrese Año\n')
        handle = open('Libros.txt', 'a')            #Abre el documento en modo editar.
        try:
            handle.write('Aut: '+ autor +', ' + 'Tít: ' + titulo + ', ' + 'Year: ' + año + '\n')            #Añade los datos el documento.
            time.sleep(1)
            print('¡Agregado!\n')
        except:
            print('Hubo un error\n')            #Mensaje de error si no se pudo agregar correctamente al documento.
        t = input('¿Añadir otro libro?\n')
        t = t.capitalize()
        if t == 'No':           #Comprobar si se quiere repetir.
            rep = False
        elif t == 'Sí' or t == 'Si':
            rep = True
        else:
            error()         #Mensjae de error si no se entendió.
            break

def entero():           #Función para mostrar la biblioteca entera,
    time.sleep(1)
    print('\n')
    c = 0
    handle = open('Libros.txt')         #Abre el documento con los libros.
    for line in handle:         #Checa cada lina del documento.
        line = line.rstrip()
        index1 = line.find('Tít:')
        titulo=index1 + 5           #Encuentra los títulos.
        index2 = line.find('Aut:')
        autor = index2 + 5          #·ncuentra los Autores.
        index3 = line.find('Year:')
        año = index3 + 6            #Encuentra los Años.
        c = c + 1
        print('\t'+str(c)+') '+line[titulo:index3-2]+' - '+line[autor:index1-2]+' - '+line[año:]) #Muestra cada libro.
    print('\nExisten', c, 'libros en la biblioteca.\n')       #Muestra número de libros.

def resumido():
    time.sleep(1)
    dic = dict()            #Inicia un diccionario.
    handle = open('Libros.txt')         #Se abre el documento donde están los libros.
    for line in handle:         #Revisa cada linea del documento.
        index = line.find('Tít:')
        y = line[5:index-2]         #Consigue cada Autor.
        dic[y] = dic.get(y,0) + 1           #Crea un histograma de libros por autor.
    for keys,values in sorted(dic.items()):
        print('\t'+keys+' - '+str(values)+' libros.')           #Muestra la cantidad de libros por autor.

def ver():          #Función de selección de vista.
    x = input('\n¿Desea ver la lista entera o resumida?\n')
    x = x.capitalize()
    if x == 'Entera':
        print('\n')
        entero()            #Inicia función entero().
    elif x == 'Resumida':
        print('\n')
        resumido()          #Inicia función resumido().
    else:
        error()         #Muestra error en caso de que no se entendiera.

def error():            #Función de error en caso de que no se entienda algun input.
    print('Lo siento, no he podido entenderte\n')


while True:         #Función principal
    print('\n¡Bienvenido a la Biblioteca!')
    time.sleep(1)
    f = input('¿Qué desea hacer? (Buscar, Añadir, Ver, Salir):\n')
    f = f.capitalize()
    rep = True
    if f == 'Buscar':
        buscar()            #Inicia Función buscar()
    elif f == ('Añadir' or 'Agregar'):
        agregar()           #Inicia función agregar()
    elif f == 'Ver':
        ver()           #Inicia función ver()
    elif f == 'Salir':
        print('\n¡Vuelva Pronto!\n')
        time.sleep(1)
        exit()          #Se sale del programa.
    else:
        error()         #Muestra error en caso de no enteder.
