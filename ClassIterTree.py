import ast
import csv
import json
import niveles

#-- clase para iterar el arbol
class ClassIterTree():

    #-- Constructor de clase
    def __init__(self, tree, atrib, pos):
        self.tree = tree
        self.atrib = atrib
        self.name = pos
        self.locali_arbol()


    #-- Método que itera sobre el árbol
    def locali_arbol(self):
        for self.node in ast.walk(self.tree):
            #-- Buscamos atribs
            if type(self.node) == eval(self.atrib):
                self.nivel= ''
                self.clase = type(self.node)
                niveles.niveles(self)
                self.asignar_lista()
                self.asignar_dict()
                self.leer_fichero_json()


    #-- Crear lista del objeto
    def asignar_lista(self):
        self.list = [self.name, self.clase, self.node.lineno,
                    self.node.end_lineno, self.node.col_offset, self.nivel]
        #print(self.list)
        self.add_csv()

    #-- Cabecera del csv
    myDataCsv =[['Nombre fichero', 'Clase', 'Linea empiece','Linea acabado',
                'Desplazamiento', 'Nivel']]

    #-- Añadir la lista del objeto al CSV
    def add_csv(self):
        self.myDataCsv.append(self.list)
        #print(self.myDataList)
        self.leer_fichero_csv()


    #-- Crear y añadir datos en el fichero.csv
    def leer_fichero_csv(self, fichero_csv = ""):
        if not fichero_csv:
            fichero_csv = open('datos.csv', 'w')
            with fichero_csv:
                writer = csv.writer(fichero_csv)
                writer.writerows(self.myDataCsv)
        else:
            with open(r'datos.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(self.myDataCsv)

    #-- Crear diccionario de json
    myDataJson = {}

    #-- Crear diccionario del objeto
    def asignar_dict(self):
        if not self.name in self.myDataJson:
            self.myDataJson[self.name] = []

        self.myDataJson[self.name].append({
            'Clase'         : str(self.clase),
            'Linea empiece' : str(self.node.lineno),
            'Linea acabado' : str(self.node.end_lineno),
            'Desplazamiento': str(self.node.col_offset),
            'Nivel'         : str(self.nivel)})
        #print(self.myDataJson)


    #-- Crear y añadir datos en el fichero.json
    def leer_fichero_json(self):
        with open('data.json', 'w') as file:
            json.dump(self.myDataJson, file, indent=4)
