#-- PROGRAMA PARA LOS NIVELES DE CADA ATRIBUTO
import ast
#-- Variable global diccionario de niveles
dictNivel = ''

#-- Lista elementos de bucle: break, continue, pass,for, while
listElemLoop = ['ast.Break', 'ast.Continue', 'ast.Pass', 'ast.While', 'ast.For']
#-- Lista de importaciones
listImport = ['ast.Import', 'ast.ImportFrom']

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
    elif self.atrib in listElemLoop:
        tipo_ElemLoop(self)
    elif self.atrib == 'ast.FunctionDef':
        nivel_FunctionDef(self)
    elif self.atrib == 'ast.Return':
        nivel_Return(self)
    elif self.atrib == 'ast.Lambda':
        nivel_Lambda(self)
    elif self.atrib == 'ast.Yield':
        nivel_GeneratorFunct(self)
    elif self.atrib == 'ast.GeneratorExp':
        nivel_GeneratorExpr(self)
    elif self.atrib in listImport:
        nivel_Module(self)
    elif self.atrib == 'ast.ClassDef':
        nivel_Class(self)
    elif self.atrib == 'ast.Attribute':
        specialClassAttributes(self)
    elif self.atrib == 'ast.Name':
        typeName(self)
    elif self.atrib == 'ast.Try':
        nivel_Try(self)
    elif self.atrib == 'ast.Raise':
        nivel_Raise(self)
    elif self.atrib == 'ast.Assert':
        nivel_Assert(self)
    elif self.atrib == 'ast.With':
        nivel_With(self)



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
    ifExp = 0
    self.nivel = dictNivel['ListComp']['Normal']
    self.clase = str(type(self.node))
    for i in range(0, len(self.node.generators)):
        numComp += 1
        ifExp += 1
        if (self.node.generators[i].ifs) != []:
            self.nivel = dictNivel['ListComp']['If']
            self.clase += (' Con sentencias de ' + str(ifExp) + ' IF')
        if numComp > 1:
            self.nivel = dictNivel['ListComp']['ListComp']
            self.clase += (' Con ' + str(numComp) + ' ListComp mas')


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
list_LoopCoding = ['range', 'zip', 'map', 'enumerate']
listStaticClass = ['staticmethod', 'classmethod']

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
        elif (self.node.func.id) in list_LoopCoding:
            valor = self.node.func.id
            nivel_LoopCoding(self, valor)
        elif (self.node.func.id) in listStaticClass:
            valor = self.node.func.id
            nivel_StaticClass(self, valor)
        elif (self.node.func.id) == 'super':
            nivel_SuperFunction(self)


#-- NIVEL FILES
def nivel_Files(self, valor):
    if (valor) == 'open':
        self.nivel = dictNivel['File']['Open']
        self.clase = ('Fichero Open en ' + str(type(self.node)))
    elif valor in list_File_Attr:
        self.nivel = dictNivel['File'][valor]
        self.clase = ('Fichero usando ' + valor + ' en ' + str(type(self.node)))

#-- NIVEL PRINTS
def nivel_Print(self, valor):
    self.nivel = dictNivel['Print'][valor]
    self.clase = ('Llamada Print en ' + str(type(self.node)))

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


#-- NIVEL IF STATEMENTS
def nivel_If(self):
    orelse = 0
    if self.atrib == 'ast.If':
        self.nivel = dictNivel['If']['Normal']
        self.clase = ('If statements ' + str(type(self.node)))
    elif self.atrib == 'ast.IfExp':
        self.nivel = dictNivel['If']['Expresion']
        self.clase = ('If expresion ' + str(type(self.node)))

#-- TIPO ELEMENTO LOOP
def tipo_ElemLoop(self):
    if self.atrib == 'ast.While':
        nivel_While(self)
    elif self.atrib == 'ast.Break':
        nivel_Break(self)
    elif self.atrib == 'ast.Continue':
        nivel_Continue(self)
    elif self.atrib == 'ast.Pass':
        nivel_Pass(self)
    elif self.atrib == 'ast.For':
        nivel_For(self)

#-- NIVEL WHILE
def nivel_While(self):
    self.nivel = dictNivel['While']['Normal']
    if self.node.orelse == []:
        self.clase = ('Bucle while-else en :' + str(type(self.node)))
    else:
        self.clase = ('Bucle while en :' + str(type(self.node)))

#-- NIVEL BREAK
def nivel_Break(self):
    self.nivel = dictNivel['Break']
    self.clase = ('Sentencia Break en : ' + str(type(self.node)))

#-- NIVEL CONTINUE
def nivel_Continue(self):
    self.nivel = dictNivel['Continue']
    self.clase = ('Sentencia Continue en : ' + str(type(self.node)))

#-- NIVEL PASS
def nivel_Pass(self):
    self.nivel = dictNivel['Pass']
    self.clase = ('Sentencia Pass en : ' + str(type(self.node)))

#-- NIVEL FOR
def nivel_For(self):
    numFor = 0
    numList = 0
    numTupleI = 0
    numTupleT = 0
    self.nivel = dictNivel['For']['Normal']
    self.clase = ('Bucle for en : ' + str(type(self.node)))
    if 'ast.For' in str(self.node.body):
        numFor += (str(self.node.body)).count('ast.For')
        self.nivel = dictNivel['For']['For']
        self.clase += (' Con ' + str(numFor) + ' For anidados')
    if 'ast.Tuple' in str(self.node.target):
        numTupleT += (str(self.node.target)).count('ast.Tuple')
        self.clase += (' Con ' + str(numTupleT) + ' Tuplas como nombre')
    if 'ast.List' in str(self.node.iter):
        numList += (str(self.node.iter)).count('ast.List')
        self.clase += (' Con ' + str(numList) + ' Listas para iterar')
    elif 'ast.Tuple' in str(self.node.iter):
        numTupleI += (str(self.node.iter)).count('ast.Tuple')
        self.clase += (' Con ' + str(numTupleI) + ' Tuplas para iterar')

#-- NIVEL LOOP CODING TECNIQUES
def nivel_LoopCoding(self, valor):
    if valor == 'range':
        self.nivel = dictNivel['LoopCoding']['range']
    elif valor == 'zip':
        self.nivel = dictNivel['LoopCoding']['zip']
    elif valor == 'map':
        self.nivel = dictNivel['LoopCoding']['map']
    elif valor == 'enumerate':
        self.nivel = dictNivel['LoopCoding']['enumerate']
    self.clase = ('Llamada a ' + valor.upper() + ' ' + str(type(self.node)))

#-- NIVEL FUNCIONES
def nivel_FunctionDef(self):
    self.nivel = dictNivel['FunctionDef']['Normal']
    self.clase = ('FUNCION DEF en ' + str(type(self.node)))
    #-- Clasificamos segun se pasan los argumentos
    nivel_DefArguments(self)
    #-- Comprobamos si hay funcion recursiva
    nivel_RecursiveFunction(self)
    #-- Comprobamos si tiene decoradores
    nivel_Decorators(self, 'function')


#-- NIVEL DE ARGUMENTOS PASADOS A FUNCIONES
def nivel_DefArguments(self):
    #-- Argumento normal
    if self.node.args.args != []:
        self.clase += (' con argumento normal')
    #-- Argumentos por defecto
    if self.node.args.defaults != []:
        self.nivel = dictNivel['FunctionDef']['Default']
        self.clase += (' con argumento por defecto')
    #-- Argumentos con *
    if self.node.args.vararg != None:
        self.nivel = dictNivel['FunctionDef']['*']
        self.clase += (' con argumento de *')
    #-- Argumentos keyword-only
    if self.node.args.kwonlyargs != []:
        self.nivel = dictNivel['FunctionDef']['Keyword-Only']
        self.clase += (' con argumento de Keyword-Only')
    #-- Argumentos con **
    if self.node.args.kwarg != None:
        self.nivel = dictNivel['FunctionDef']['**']
        self.clase += (' con argumento de **')

#-- NIVEL RETURN
def nivel_Return(self):
    self.nivel = dictNivel['Return']
    self.clase = ('Usando un RETURN en una funcion ' + str(type(self.node)))

#-- NIVEL LAMBDA
def nivel_Lambda(self):
    self.nivel = dictNivel['Lambda']
    self.clase = ('Usando LAMBDA ' + str(type(self.node)))


#-- NIVEL FUNCIONES RECURSIVAS
def nivel_RecursiveFunction(self):
    for i in ast.walk(self.node):
        if 'ast.Call' in str(i):
            try:
                if i.func.id == self.node.name:
                    self.nivel = dictNivel['FunctionDef']['Recursive']
                    self.clase += (' con funcion RECURSIVA')
            except:
                pass

#-- NIVEL GENERATOR FUNCTION
#-- nivel Yield
def nivel_GeneratorFunct(self):
    self.nivel = dictNivel['GeneratorFunct']
    self.clase = ('GENERATOR FUNTION (YIELD) ' + str(type(self.node)))

#-- GENERATOR EXPRESION
def nivel_GeneratorExpr(self):
    self.nivel = dictNivel['GeneratorExpr']
    self.clase = ('GENERATOR EXPRESSION ' + str(type(self.node)))

#-- Lista de modulos importantes
listModules = ['struct', 'pickle', 'shelve', 'dbm', 're', 'importlib']

#-- MODULOS IMPORTANTES
def nameModules(self, name):
    for i in range(0, len(name)):
        if name[i] in listModules:
            self.nivel = dictNivel['Module']['Names']
            self.clase += (' modulo ' + name[i])


#-- NIVEL 'AS' EXTENSION
def nivel_AsExtension(self):
    for i in self.node.names:
        if i.asname != None:
            self.nivel = dictNivel['Module']['As']
            self.clase += (' con Extension AS ')

#-- NIVEL FROM
def nivel_From(self):
    #-- Comprobamos si es importacion relativa o absoluta
    if (self.node.level == 1) or (self.node.level == 2):
        self.nivel = dictNivel['Module']['From']['Relative']
        self.clase += (' Importacion RELATIVA de nivel ' + str(self.node.level))
    #-- Comprobamos si es from *statements
    for i in self.node.names:
        if i.name == '*':
            self.nivel = dictNivel['Module']['From']['*']
            self.clase += (' importacion con * ')

#-- NIVEL MODULOS
def nivel_Module(self):
    nameModule = []
    if self.atrib == 'ast.Import':
        self.nivel = dictNivel['Module']['Import']
        self.clase = ('Importado con IMPORT ' + str(type(self.node)))
        for i in self.node.names:
            nameModule.append(i.name)
    else:
        self.nivel = dictNivel['Module']['From']['Normal']
        self.clase = ('Importado con FROM IMPORT' + str(type(self.node)))
        nivel_From(self)
        nameModule.append(self.node.module)
    nivel_AsExtension(self)
    nameModules(self, nameModule)


#-- FUNCION PRIVADA DE CLASE
def PrivateClass(self):
    for funct in self.node.body:
        #-- Comprobamos si la funcion es privada
        if(funct.name.startswith('__')) and (not funct.name.endswith('__')):
            self.nivel = dictNivel['Class']['Private']
            self.clase += (' funcion PRIVADA ' + str(funct.name))
    #-- Comprobamos si hay atributos/metodos privados
        for i in ast.walk(funct):
            if 'ast.Attribute' in str(i):
                if (i.attr.startswith('__')) and (not i.attr.endswith('__')):
                    self.nivel = dictNivel['Class']['Private']
                    self.clase += (' atributo PRIVADO ' + str(i.attr))

#-- METODO CONSTRUCTOR
def constrMethod(self):
    for i in self.node.body:
        if i.name == '__init__':
            self.clase += (' metodo CONSTRUCTOR ' + str(i.name))

#-- lista de descriptores
listDescriptors = ['__get__', '__set__', '__delete__']

#-- DESCRIPTORES
def Descriptors(self):
    for elem in self.node.body:
        if elem.name in listDescriptors:
            self.nivel += dictNivel['Class']['Descriptor']
            self.clase += (' con DESCRIPTOR ' + str(elem.name))

#-- PROPERTIES
def nivel_Properties(self):
    for node in self.node.body:
        for elem in ast.walk(node):
            if 'ast.Call' in str(elem):
                try:
                    if elem.func.id == 'property':
                        self.nivel = dictNivel['Class']['Properties']
                        self.clase += (' con PROPERTIES ')
                except:
                    pass


#-- NIVEL CLASE
def nivel_Class(self):
    self.nivel = dictNivel['Class']['Normal']
    self.clase = ('CLASE ' + str(type(self.node)))
    #-- Comprobamos si tiene clase heredada
    for i in self.node.bases:
        try:
            self.nivel = dictNivel['Class']['Heredada']
            self.clase += (' hereda de la clase ' + str(i.id))
        except:
            pass
    #-- Comprobamos si tiene propiedades
    nivel_Properties(self)
    #-- Comprobamos el nombre de las funciones
    if 'ast.FunctionDef' in str(self.node.body):
        try:
            #-- Comprobamos si hay metodo constructor
            constrMethod(self)
            #-- Comprobamos si hay descriptores
            Descriptors(self)
            #-- Comprobamos si hay funciones y atributos privados
            PrivateClass(self)
        except:
            pass
    #-- Comprobamos si tiene decoradores de clase
    nivel_Decorators(self, 'class')
    #-- Comprobamos si tiene metaclases
    nivel_Metaclass(self, 'cabecera')

#-- Lista de atributos especiales de CLASES
listClassAttr = ['__class__', '__dict__']

#-- Special Class Attributes
def specialClassAttributes(self):
    if self.node.attr in listClassAttr:
        self.nivel = dictNivel['Attribute']['SpecClass']
        self.clase = (' Atributo especial de clases ' + str(self.node.attr) +
                       ' ' + str(type(self.node)))

#-- NIVEL STATIC AND CLASS METHOD
def nivel_StaticClass(self, valor):
    self.nivel = dictNivel['StaticClass']
    self.clase = (valor.upper() + ' en ' + str(type(self.node)))

#-- FUNCTIONS AND CLASSES DECORATORS
def nivel_Decorators(self, type):
    for i in self.node.decorator_list:
        self.nivel = dictNivel['Decorator']
        self.clase += (' con ' + type.upper() + ' DECORATOR ')

#-- Tipo de ast.Name
def typeName(self):
    if self.node.id == '__metaclass__':
        nivel_Metaclass(self, 'atrib')

#-- METACLASS
def nivel_Metaclass(self, pos):
    if pos == 'cabecera':
        for i in self.node.keywords:
            if i.arg == 'metaclass':
                self.nivel = dictNivel['Metaclass']
                self.clase += (' cabecera METACLASE ' + i.value.id)
    elif pos == 'atrib':
        self.nivel = dictNivel['Metaclass']
        self.clase = ('atrib METACLASE ' + self.node.id + str(type(self.node)))

#-- SUPER BUILT-IN FUNCTION
def nivel_SuperFunction(self):
    self.nivel = dictNivel['SuperFunction']
    self.clase = ('function SUPER ' + str(type(self.node)))

#-- NIVEL EXCEPCIONES
#-- TRY
def nivel_Try(self):
    self.nivel = dictNivel['Exception']['Try']
    self.clase = (str(type(self.node))+ ' Excepcion TRY')
    if 'ast.Try' in str(self.node.body):
        self.clase += ('/TRY')
    if (self.node.handlers) != []:
        self.clase += ('/EXCEPT')
    if (self.node.orelse) != []:
        self.clase += ('/ELSE')
    if (self.node.finalbody) != []:
        self.clase += ('/FINALLY')

#-- RAISE
def nivel_Raise(self):
    self.nivel = dictNivel['Exception']['Raise']
    self.clase = ('Excepcion RAISE ' + str(type(self.node)))

#-- ASSERT
def nivel_Assert(self):
    self.nivel = dictNivel['Exception']['Assert']
    self.clase = ('Excepcion ASSERT ' + str(type(self.node)))

#-- WITH
def nivel_With(self):
    self.nivel = dictNivel['With']
    self.clase = ('uso de WITH ' + str(type(self.node)))
