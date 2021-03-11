#-- PROGRAMA PARA LOS NIVELES DE CADA ATRIBUTO
import ast
#-- Variable global diccionario de niveles
dictNivel = ''

#-- LEER FICHERO CON NIVELES
with open('/home/ana/Documentos/TFG/TFG/dict.txt', 'r') as dict_file:
    dict_text = dict_file.read()
    dictNivel = eval(dict_text)

#-- ASIGNAR NIVELES
def niveles(self):
    if self.atrib == 'ast.List':
        nivel_List(self)
    elif self.atrib == 'ast.ListComp':
        nivel_ListComp(self)
    elif self.atrib == 'ast.Dict':
        nivel_Dict(self)
    elif self.atrib == 'ast.DictComp':
        nivel_DictComp(self)
    elif self.atrib == 'ast.Tuple':
        nivel_Tuple(self)
    elif self.atrib == 'ast.Call':
        tipo_Call(self)


#-- NIVEL DE LISTAS
def nivel_List(self):
    numList = 0
    numDict = 0
    #-- Comprobamos si hay listas
    if 'ast.List' in str(self.node.elts):
        numList = str(self.node.elts).count('ast.List')
        self.nivel = dictNivel['List']['List']
        self.clase = str(numList) + ' Listas en' + str(type(self.node))
    elif 'ast.Dict' in str(self.node.elts):
        numDict = str(self.node.elts).count('ast.Dict')
        self.nivel = dictNivel['List']['Dict']
        self.clase = str(numDict) + ' Diccionarios en' + str(type(self.node))
    else:
        self.nivel = dictNivel['List']['Normal']
        self.clase = type(self.node)


#-- NIVEL LIST COMPREHENSION
def nivel_ListComp(self):
    numComp = 0
    for i in range(0, len(self.node.generators)):
        numComp += 1
    if numComp > 1:
        self.nivel = dictNivel['ListComp']['ListComp']
        self.clase = str(numComp) + ' ' + str(type(self.node))
    else:
        self.nivel = dictNivel['ListComp']['Normal']
        self.clase = type(self.node)

#-- NIVEL DICCIONARIO
def nivel_Dict(self):
    numList = 0
    numDict = 0
    #-- Comprobamos si hay diccionarios
    if 'ast.Dict' in str(self.node.values):
        numDict = str(self.node.values).count('ast.Dict')
        self.nivel = dictNivel['Dict']['Dict']
        self.clase = str(numDict) + ' Diccionarios en el' + str(type(self.node))
        #-- Comprobamos si hay listas dentro de diccionarios de diccionario
        for i in range(0, len(self.node.values)):
            if 'ast.List' in str(self.node.values[i].values):
                numList += str(self.node.values[i].values).count('ast.List')
                self.nivel = dictNivel['Dict']['Dict y List']
                self.clase = (str(numList) + ' Listas en ' + str(numDict) +
                            ' Diccionarios en ' + str(type(self.node)))
    #-- Comprobamos si hay listas
    elif 'ast.List' in str(self.node.values):
        numList = str(self.node.values).count('ast.List')
        self.nivel = dictNivel['Dict']['List']
        self.clase = str(numList) + ' Listas en' + str(type(self.node))
    else:
        self.nivel = dictNivel['Dict']['Normal']
        self.clase = type(self.node)

#-- NIVEL DICT COMPREHENSION
def nivel_DictComp(self):
    numIfs = 0
    ifExp = 0
    numDictComp = 0
    for i in self.node.generators:
        numIfs += str(i.ifs).count('ast.Compare')
        if numIfs > 0:
            self.nivel = dictNivel['DictComp']['If']
            self.clase = (str(numIfs) + ' Ifs en: ' + str(type(self.node)))
        else:
            self.nivel = dictNivel['DictComp']['Normal']
            self.clase = type(self.node)
    if 'ast.IfExp' in str(self.node.value):
        ifExp += str(self.node.value).count('ast.IfExp')
        self.nivel = dictNivel['DictComp']['If-Else']
        self.clase = (str(ifExp) + ' IF - ELSE en : ' + str(type(self.node)))
    elif 'ast.DictComp' in str(self.node.value):
        numDictComp += str(self.node.value).count('ast.DictComp')
        self.nivel = dictNivel['DictComp']['DictComp']
        self.clase = (str(numDictComp) + str(type(self.node)))

#-- NIVEL TUPLA
def nivel_Tuple(self):
    numTuple = 0
    for i in self.node.elts:
        numTuple += str(self.node.elts).count('ast.Tuple')
        if numTuple > 0:
            self.nivel = dictNivel['Tuple']['Tuple']
            self.clase = (str(numTuple) + ' Tuple: ' + str(type(self.node)))
        else:
            self.nivel = dictNivel['Tuple']['Normal']
            self.clase = type(self.node)

def tipo_Call(self):
    if 'ast.Name' in str(self.node.func):
        if (self.node.func.id) == 'open':
            nivel_Files(self)


def nivel_Files(self):
    if (self.node.func.id) == 'open':
        self.nivel = dictNivel['File']['Open']
        self.clase = (str('Fichero Open en ' + str(type(self.node))))
