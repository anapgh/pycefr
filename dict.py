import configparser
configuracion = configparser.ConfigParser()

#-- Leer el archivo de configuracion
configuracion.read('Configuracion.cfg')

#-- Diccionario de NIVELES
levels = {}

#-- Mostrar lista con las secciones leidas en el archivo
configuracion.sections()
for seccion in configuracion.sections():
    levels[seccion] = []
    # Listar opciones y valores de una sección:
    for opcion, valor in configuracion[seccion].items():
        levels[seccion].append({opcion : valor})

print(levels)

#-- Creamos archivo.txt con el diccionario
with open('dicc.txt', 'w') as file:
    file.write(str(levels))
    file.close()
