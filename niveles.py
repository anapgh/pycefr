#-- PROGRAMA PARA LOS NIVELES DE CADA ATRIBUTO
import ast
#-- Variable global diccionario de niveles
dictNivel = ''

#-- Lista de elemtnos break, continue, pass y loop ELSE


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
    elif self.atrib == 'ast.Assign':
        nivel_Assign(self)
    elif self.atrib == 'ast.AugAssign':
        nivel_Assign(self)
    elif self.atrib == 'ast.If':
        nivel_If(self)
    elif self.atrib == 'ast.IfExp':
        nivel_If(self)
    elif self.atrib == 'ast.While':
        nivel_While(self)

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

#-- Lista de atributos de ficheros
list_File_Attr = ['write', 'read', 'readline', 'writelines']

#-- Tipos de llamadas
def tipo_Call(self):
    valor = ''
    if 'ast.Attribute' in str(self.node.func):
        if (self.node.func.attr) in list_File_Attr:
            valor = self.node.func.attr
            nivel_Files(self, valor)
    elif 'ast.Name' in str(self.node.func):
        if (self.node.func.id) == 'open':
            valor = 'open'
            nivel_Files(self, valor)
        elif (self.node.func.id) == 'print':
            valor = 'print'
            nivel_Print(self, valor)

#-- NIVEL FILES
def nivel_Files(self, valor):
    if (valor) == 'open':
        self.nivel = dictNivel['File']['Open']
        self.clase = ('Fichero Open en ' + str(type(self.node)))
    elif valor in list_File_Attr:
        self.nivel = dictNivel['File'][valor]
        self.clase = ('Fichero usando ' + valor + ' en ' + str(type(self.node)))

#-- NIVEL ASIGNACIONES
def nivel_Assign(self):
    op = ''
    if self.atrib == 'ast.Assign':
        self.nivel = dictNivel['Assign']['Normal']
        self.clase = ('Asignación normal ' + str(type(self.node)))
        #print(self.node.targets)
        if 'ast.BinOp' in str(self.node.value):
            self.nivel = dictNivel['Assign']['Assign + suma']
            self.clase = ('Asignación normal con incremento ' + str(type(self.node)))
    else:
        self.nivel = dictNivel['Assign']['AugAssign']
        if 'ast.Add' in str(self.node.op):
            op = 'aumento suma'
        elif 'ast.Sub' in str(self.node.op):
            op = 'decremento resta'
        elif 'ast.Mult' in str(self.node.op):
            op = 'aumento multiplicacion'
        self.clase = ('Asignación simplificada de ' + op + str(type(self.node)))

#-- NIVEL PRINTS
def nivel_Print(self, valor):
    self.nivel = dictNivel['Print'][valor]
    self.clase = ('Llamada Print en ' + str(type(self.node)))

#-- NIVEL IF STATEMENTS
def nivel_If(self):
    orelse = 0
    if self.atrib == 'ast.If':
        #print(self.node.lineno)
        #print(self.node.col_offset)
        #print(self.node.orelse)
        self.nivel = dictNivel['If']['Normal']
        self.clase = ('If statements ' + str(type(self.node)))
    elif self.atrib == 'ast.IfExp':
        self.nivel = dictNivel['If']['Expresion']
        self.clase = ('If expresion ' + str(type(self.node)))

#-- NIVEL WHILE
def nivel_While(self):
    self.nivel = dictNivel['While']['Normal']
    if self.node.orelse == []:
        self.clase = ('Bucle while-else en: ' + str(type(self.node)))
    else:
        self.clase = ('Bucle while en :' + str(type(self.node)))
