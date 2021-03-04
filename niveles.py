import ast
#-- NIVELES

#-- NIVEL LIST COMPREHENSION
def nivel_ListComp(self):
    numComp = 0
    for i in range(0, len(self.node.generators)):
        numComp += 1
    if numComp > 1:
        print('ES UNA LIST COMPREHENSION ANIDADA')
        self.nivel = 'C2'
        self.clase = str(numComp) + ' ' + str(type(self.node))
    else:
        print('ES UNA LIST COMPREHENSION NORMAL')
        self.nivel = 'C1'
        self.clase = type(self.node)

#-- NIVEL DICCIONARIO
def nivel_dict(self):
    numList = 0
    if 'ast.List' in str(self.node.values):
        print('hay lista')
        numList = str(self.node.values).count('ast.List')
        self.nivel = 'B1'
        self.clase = str(numList) + ' Listas en' + str(type(self.node))
    else:
        print('no hay listas')
        self.nivel = 'A2'
        self.clase = type(self.node)
