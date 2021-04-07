#-- PROGRAMA PARA EXTRAER NIVELES DEL JSON

import json

listNiveles = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']

def extraer_niveles(data):
    #-- Sacamos los ficheros que hay (keys)
    for fich in data.keys():
        #-- Inicilizo los niveles a 0
        A1 = 0
        A2 = 0
        B1 = 0
        B2 = 0
        C1 = 0
        C2 = 0
        for i in data[fich]:
            nivel = (i["Nivel"])
            #-- Contamos cada nivel en cada fichero
            for valor in listNiveles:
                if valor in nivel:
                    if valor == 'A1':
                        A1 += nivel.count(valor)
                    elif valor == 'A2':
                        A2 += nivel.count(valor)
                    elif valor == 'B1':
                        B1 += nivel.count(valor)
                    elif valor == 'B2':
                        B2 += nivel.count(valor)
                    elif valor == 'C1':
                        C1 += nivel.count(valor)
                    elif valor == 'C2':
                        C2 += nivel.count(valor)

        #-- Guardamos resultados en myDataNivel
        myDataNivel = ('Fichero: ' + fich + '\n' + 'Niveles: ' + '\n' +
                        'A1: ' + str(A1) + '\n' + 'A2: ' + str(A2) + '\n' +
                        'B1: ' + str(B1) + '\n' + 'B2: ' + str(B2) + '\n'+
                        'C1: ' + str(C1) + '\n' + 'C2: ' + str(C2) + '\n\n')
        escribir_resultados(myDataNivel)

#-- Creamos un archivo.txt con un resumen de resultados
def escribir_resultados(myDataNivel):
    with open('resumen.txt', 'a') as file:
        file.write(myDataNivel)
        file.close()
    print('Fichero creado...')

def leer_json():
    with open('data.json') as file:
        data = json.load(file)
        extraer_niveles(data)


if __name__ == "__main__":
    leer_json()
