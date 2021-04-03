import configparser
configuracion = configparser.ConfigParser()

#-- Leer el archivo de configuracion
configuracion.read('Configuracion.cfg')

#-- Diccionario de NIVELES
levels = []
element = {}

#-- Mostrar lista con las secciones leidas en el archivo
configuracion.sections()
for seccion in configuracion.sections():
    element[seccion] = []
    # Listar opciones y valores de una sección:
    for opcion, valor in configuracion[seccion].items():
        element[seccion].append({opcion : valor})

print(element)
