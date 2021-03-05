#-- PROGRAMA PARA LOS NIVELES DE CADA ATRIBUTO

#-- NIVELES
def niveles(self):
    if self.atrib == 'ast.List':
        nivel_List(self)
    elif self.atrib == 'ast.ListComp':
        nivel_ListComp(self)
    elif self.atrib == 'ast.Dict':
        nivel_Dict(self)
    elif self.atrib == 'ast.DictComp':
        nivel_DictComp(self)


#-- NIVEL DE LISTAS
def nivel_List(self):
    num_List = 0
    num_Dict = 0
    #-- Comprobamos si hay listas
    if 'ast.List' in str(self.node.elts):
        print('hay lista')
        numList = str(self.node.elts).count('ast.List')
        self.nivel = 'A2'
        self.clase = str(numList) + ' Listas en' + str(type(self.node))
    else:
        print('no hay nada')
        self.nivel = 'A1'
        self.clase = type(self.node)


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
def nivel_Dict(self):
    numList = 0
    numDict = 0
    #-- Comprobamos si hay diccionarios
    if 'ast.Dict' in str(self.node.values):
        print('hay diccionario dentro')
        numDict = str(self.node.values).count('ast.Dict')
        self.nivel = 'B1'
        self.clase = str(numDict) + ' Diccionarios en el' + str(type(self.node))
        #-- Comprobamos si hay listas dentro de diccionarios de diccionario
        for i in range(0, len(self.node.values)):
            print('HOLAA')
            print(self.node.values[i].values)
            if 'ast.List' in str(self.node.values[i].values):
                print('diccionario de diccionario de  listas')
                numList += str(self.node.values[i].values).count('ast.List')
                self.nivel = 'B2'
                self.clase = (str(numList) + ' Listas en ' + str(numDict) +
                            ' Diccionarios en ' + str(type(self.node)))
                print(self.clase)
    #-- Comprobamos si hay listas
    elif 'ast.List' in str(self.node.values):
        print('hay lista')
        numList = str(self.node.values).count('ast.List')
        self.nivel = 'B1'
        self.clase = str(numList) + ' Listas en' + str(type(self.node))
    else:
        print('no hay nada')
        self.nivel = 'A2'
        self.clase = type(self.node)

def nivel_DictComp(self):
    numIfs = 0
    ifExp = 0
    numDictComp = 0
    print('DICT COMP:')
    print(self.node.generators)
    print('VALUE')
    print(self.node.value)
    for i in self.node.generators:
        print('IFSSSSSSSS')
        print(i.ifs)
        numIfs += str(i.ifs).count('ast.Compare')
        if numIfs > 0:
            print('DICT COMPREHENSION CONDICIONAL')
            self.nivel = 'C2'
            self.clase = (str(numIfs) + ' Ifs en: ' + str(type(self.node)))
        else:
            print('DICT COMPREHENSION NORMAL')
            self.nivel = 'C1'
            self.clase = type(self.node)
    if 'ast.IfExp' in str(self.node.value):
        ifExp += str(self.node.value).count('ast.IfExp')
        print('DICT COMPREHENSION IF - ELSE')
        self.nivel = 'C2'
        self.clase = (str(ifExp) + ' IF - ELSE en : ' + str(type(self.node)))
    elif 'ast.DictComp' in str(self.node.value):
        numDictComp += str(self.node.value).count('ast.DictComp')
        print('DICT COMPREHENSION ANIDADA')
        self.nivel = 'C2'
        self.clase = (str(numDictComp) + str(type(self.node)))
