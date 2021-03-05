import ast
import csv
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


    #-- Crear lista del objeto
    def asignar_lista(self):
        self.list = [self.name, self.clase, self.node.lineno,
                    self.node.end_lineno, self.node.col_offset, self.nivel]
        #print(self.list)
        self.add_csv()

    #-- Cabecera del csv
    myData =[['Nombre fichero', 'Clase', 'Linea empiece','Linea acabado',
                'Desplazamiento', 'Nivel']]

    #-- Añadir la lista del objeto al CSV
    def add_csv(self):
        self.myData.append(self.list)
        #print(self.myData)
        self.leer_fichero_csv()


    #-- Crear y añadir datos en el fichero.csv
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
