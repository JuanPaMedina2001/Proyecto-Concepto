def buscar(clave):
    if len(clave) > 1 and clave != 'salir':
        c = 0  #Counter

        # Por cada linea del docuento...
        for line in handle:
            line = line.rstrip() #Quita whitespace \n

            # Revisar qué linea tiene la palabra clave
            if clave in line:

                #Sacar los títulos de los libros
                index1 = line.find('Tít:')
                titulo=index1 + 4
                c = c + 1

                #Sacar el autor de el libro
                index2 = line.find('Aut:')
                autor = index2 + 5

                #Imprimir cada libro con su autor
                print(line[titulo:], '-', line[autor:index1-2])


        # Número de libros encontrados
        print('Mostrando', c, 'resultados para:', clave)

    #Para salir del buscador
    elif clave == 'salir' or 'Salir':
        exit()
    #Si no escribe nada
    else:
        print('Por favor ingrese algo')


while True:

    # Abre el documento
    handle = open('Libros.txt') # Un archivo de texto en mi pc con los títulos y autores de los libros

    #Pide al usuario un apalabra clave
    clave = input('Inserte busqueda:\n')
    buscar(clave)
