# Version para JSON
def new_artist_json ():
    """Esta función construye un diccionario que contiene 5 datos sobre un artista
    ingresados desde teclado: nombre, si es solista, ciudad, país y referencia.
    
    Returns:
        dict: Un diccionario con los datos del artista ubicados respectivamente
        en los indices 'nombre', 'es_solista', 'ciudad', 'pais' y 'ref'."""
    
    data = {}

    data['nombre'] = input("Ingrese el nombre del artista: ")
    es_solista = input("¿Es solista? y/n: ").lower
    if es_solista == 'y':
        data['es_solista'] = True
    else: data['es_solista'] = False
    data['ciudad'] = input("Ingrese la ciudad de proveniencia: ")
    data['pais'] = input("Ingrese el pais de proveniencia: ")
    data['ref'] = input("¿Dónde puedo escuchar sus canciones? (link) ")

    print(data)

    return data

# Version para CSV
def new_artist_csv ():
    """Esta función construye una lista que contiene 5 datos sobre un artista
    ingresados desde teclado: nombre, si es solista, ciudad, país y referencia.
    
    Returns:
        list: Lista con los datos del artista."""
    
    data = []

    data.append(input("Ingrese el nombre del artista: "))
    es_solista = input("¿Es solista? y/n: ").lower
    if es_solista == 'y':
        data.append(True)
    else: data.append(False)
    data.append(input("Ingrese la ciudad de proveniencia: "))
    data.append(input("Ingrese el pais de proveniencia: "))
    data.append(input("¿Dónde puedo escuchar sus canciones? (link) "))

    print(data)

    return data