import csv

#-- Creando una clase arbol
class ClassTree():
    #-- Lista del csv
    myData =[['Nombre fichero', 'Clase', 'Linea empiece','Linea acabado',
                'Desplazamiento', 'Nivel']]
    #-- Contructor de clase
    def __init__(self, name, clase, start, end, offset, nivel):
        self.name = name # Nombre del fichero
        self.clase = clase # clase
        self.line_start = start # linea donde empieza
        self.line_end = end # Linea donde acaba
        self.offset = offset # Desplazamiento columna
        self.nivel = nivel # Nivel
        self.list = [self.name, self.clase, self.line_start, self.line_end,
                self.offset, self.nivel]
        print('hola')
        print(list)

    def add_csv(self):
        self.myData.append(self.list)
        print(self.myData)

    #-- Crear fichero.csv
    def leer_fichero_csv(self, fichero_csv = ""):
        if not fichero_csv:
            fichero_csv = open('datos.csv', 'w')
            with fichero_csv:
                writer = csv.writer(fichero_csv)
                writer.writerows(self.myData)
        else:
            with open(r'datos.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(self.myData)
