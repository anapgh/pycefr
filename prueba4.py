#-- probando el modulo de ast
import ast
import os
import csv
from ClassTree import ClassTree

#-- Creamos listas de cada atrib
Literals = ['ast.Constant', 'ast.FormattedValue', 'ast.JoinedStr', 'ast.List', 'ast.Tuple', 'ast.Set',
            'ast.Dict']

Variables = ['ast.Name', 'ast.Load', 'ast.Store', 'ast.Del', 'ast.Starred']
Expressions = ['ast.Expr', 'ast.UnaryOp', 'ast.UAdd', 'ast.USub', 'ast.Not', 'ast.Invert', 'ast.BinOp',
                'ast.Add', 'ast.Sub', 'ast.Mult', 'ast.Div', 'ast.FloorDiv', 'ast.Mod', 'ast.Pow', 'ast.LShift',
                'ast.RShift', 'ast.BitOr', 'ast.BitXor', 'ast.BitAnd', 'ast.MatMult', 'ast.BoolOp',
                'ast.And', 'ast.Or', 'ast.Compare', 'ast.Eq', 'ast.NotEq', 'ast.Lt', 'ast.LtE', 'ast.Gt', 'ast.GtE',
                'ast.Is', 'ast.IsNot', 'ast.In', 'ast.NotIn', 'ast.Call', 'ast.keyword', 'ast.IfExp',
                'ast.Attribute', 'ast.NamedExpr']
Subscripting = ['ast.Subscript', 'ast.Slice']
Comprehensions = ['ast.ListComp', 'ast.SetComp', 'ast.GeneratorExp', 'ast.DictComp',
                  'ast.comprehension']
Statements = ['ast.Assig', 'ast.AnnAssign', 'ast.AugAssign', 'ast.Raise', 'ast.Assert', 'ast.Delete',
              'ast.Pass']
Imports = ['ast.Import', 'ast.ImportFrom', 'ast.alias']
ControlFlow = ['ast.If', 'ast.For', 'ast.While', 'ast.Break', 'ast.Continue', 'ast.Try',
               'ast.ExceptHandler', 'ast.With', 'ast.Withitem']
FunctionsClass = ['ast.FunctionDef', 'ast.Lambda', 'ast.arguments', 'ast.arg', 'ast.Return',
                   'ast.Yield', 'ast.YieldFrom', 'ast.Global', 'ast.Nonlocal', 'ast.ClassDef']
AsyncAwait = ['ast.AsyncFunctionDef', 'ast.Await', 'ast.AsyncFor', 'ast.AsyncWith']

#-- Creamos lista de listas de atribs
SetClass = [Literals, Variables, Expressions, Subscripting, Comprehensions,
          Statements, Imports, ControlFlow, FunctionsClass, AsyncAwait]


#-- Extraemos del directorio los archivos .py
def leer_directorio():
    pos = ''
    print('directorio: ')
    directorio = os.listdir("/home/ana/Documentos/TFG/TFG")
    print(directorio)
    for i in range(0, len(directorio)):
        if directorio[i].endswith('.py'):
            print('fichero python: ' + str(directorio[i]))
            pos = directorio[i]
            leer_fichero(directorio[i], pos)



#-- Leemos el fichero y nos devuelve el arbol
def leer_fichero(fichero, pos):
    with open(fichero) as fp:
        my_code = fp.read()
        tree = ast.parse(my_code)
        print (ast.dump(tree))
        iterar_lista(tree, pos)


#-- Iterar lista y asignar atributos
def iterar_lista(tree, pos):
    for i in range(0, len(SetClass)):
        for j in range(0, len(SetClass[i])):
            atrib = SetClass[i][j]
            profundizar(tree, atrib, pos)

#-- Lista del csv
myData =[['Nombre fichero', 'Clase', 'Linea empiece','Linea acabado',
            'Desplazamiento', 'Nivel']]

#-- Crear fichero.csv
def leer_fichero_csv():
    myCsv = open('datos.csv', 'w')
    with myCsv:
        writer = csv.writer(myCsv)
        writer.writerows(myData)

#-- LISTAS
def lista(tree, atrib,pos):
    nivel = ''
    clase = ''
    if atrib == 'ast.List':
        for node in ast.walk(tree):
            if type(node) == eval(atrib):
                print ('LISTA:')
                #print(ast.literal_eval(node))
                print(node.elts)
                for node1 in ast.walk(node):
                    if type(node1) == eval(atrib):
                        print('LISTA DE LISTAS')
                        nivel = 'A2'
                        clase = str(type(node)) + str(type(node1))
                    else:
                        print ('LISTA NORMAL')
                        nivel = 'A1'
                        clase = type(node)
                    #-- Añadir datos en list:
                    list = [pos, clase, node.lineno, node.end_lineno,
                                node.col_offset, nivel]
                    #-- Añadir list en la lista myData que se convierte en .csv
                    myData.append(list)


#-- LIST COMPREHENSION
def list_comprehension2(tree, atrib, pos):
    nivel = ''
    clase = ''
    if atrib == 'ast.ListComp':
        for node in ast.walk(tree):
            numComp = 0
            if type(node) == eval(atrib):
                print('LIST COMPREHENSION:')
                print(node.generators)
                for i in node.generators:
                    print (i)
                    numComp += 1
                if numComp > 1:
                    print('ES UNA LIST COMPREHENSION ANIDADA')
                    nivel = 'C2'
                    clase = str(numComp) + ' ' + str(type(node))
                else:
                    print('ES UNA LIST COMPREHENSION NORMAL')
                    nivel = 'C1'
                    clase = type(node)
                #-- Añadir datos en listComp:
                listComp = [pos, clase,node.lineno, node.end_lineno,
                            node.col_offset, nivel]
                #-- Añadir listComp en la lista myData que se convierte en .csv
                myData.append(listComp)

#-- USANSO CLASE TREE
def list_comprehension(tree, atrib, pos):
    nivel = ''
    clase = ''
    if atrib == 'ast.ListComp':
        for node in ast.walk(tree):
            numComp = 0
            if type(node) == eval(atrib):
                print('LIST COMPREHENSION:')
                print(node.generators)
                for i in node.generators:
                    print (i)
                    numComp += 1
                if numComp > 1:
                    print('ES UNA LIST COMPREHENSION ANIDADA')
                    nivel = 'C2'
                    clase = str(numComp) + ' ' + str(type(node))
                else:
                    print('ES UNA LIST COMPREHENSION NORMAL')
                    nivel = 'C1'
                    clase = type(node)
                #-- Crear instancia de objeto
                LC = ClassTree(pos, clase, node.lineno, node.end_lineno,node.col_offset, nivel)
                LC.add_csv()
                LC.leer_fichero_csv()


#-- DICCIONARIOS
def diccionario(tree, atrib, pos):
    nivel = ''
    if atrib == 'ast.Dict':
        for node in ast.walk(tree):
            #-- Buscamos atribs
            if type(node) == eval(atrib):
                print('DICCIONARIO:')
                d1 = ast.literal_eval(node)
                print(d1)
                nivel = 'A1'
                clase = type(node)
                #-- Añadir datos en dicc:
                #-- Crear instancia de objeto
                D = ClassTree(pos, clase, node.lineno, node.end_lineno,node.col_offset, nivel)
                D.add_csv()
                D.leer_fichero_csv()
                for node1 in ast.walk(node):
                    atrib1 = ast.List
                    """
                    if type(node1) == atrib:
                        print('DICCIONARIO DENTRO DE DICCIONARIO')
                        print(ast.literal_eval(node1))
                        print (str(atrib1) + ':')
                        print (node1.lineno) #-- Primera linea del texto
                        print (node1.end_lineno) #-- Ultima linea del texto
                        print('elementos:')
                        print(node1.values)
                    """
                    if type(node1) == atrib1:
                        print('DICCIONARIO DE LISTAS:')
                        print(ast.literal_eval(node1))
                        nivel = 'A2'
                        clase = str(type(node)) + str(type(node1))
                        #-- Añadir datos en dicc:
                        D = ClassTree(pos, clase, node1.lineno, node1.end_lineno,
                                        node1.col_offset, nivel)
                        #-- Añadir dicc en la lista myData que se convierte en .csv
                        D.add_csv()
                        D.leer_fichero_csv()


#-- DICT COMPREHENSION
def dict_comprehension(tree, atrib, pos):
    nivel = ''
    clase = ''
    if atrib == 'ast.DictComp':
        for node in ast.walk(tree):
            numComp = 0
            numIfs = 0
            if type(node) == eval(atrib):
                print('DICT COMPREHENSION:')
                for i in node.generators:
                    print(i.ifs)
                    for j in i.ifs:
                        numIfs += 1
                        numComp += 1
                        if numIfs > 1:
                            print('ES UN DICT COMPREHENSION CONDICIONAL')
                            nivel = 'C2'
                            clase = str(numIfs) + 'IFS +  ' + str(type(node))
                        if numComp > 1:
                            print('ES UN DICT COMPREHENSION ANIDADO')
                            nivel = 'C2'
                            clase = str(numComp) + ' ' + str(type(node))
                        else:
                            print('ES UN DICT COMPREHENSION')
                            nivel = 'C1'
                            clase = type(node)
                        #-- Añadir datos en dictComp:
                        dictComp = [pos, clase,node.lineno, node.end_lineno,
                                    node.col_offset, nivel]
                        #-- Añadir dictComp en la lista myData que se convierte en .csv
                        myData.append(dictComp)


def profundizar(tree, atrib, pos):
    #lista(tree, atrib,pos)
    list_comprehension(tree, atrib, pos)
    diccionario(tree, atrib, pos)
    #dict_comprehension(tree, atrib, pos)


    #leer_fichero_csv()



def locali_arbol(tree, atrib):
    for node in ast.walk(tree):
        #-- Buscamos atribs
        if type(node) == eval(atrib):
            print (str(atrib) + ':')
            print (node.lineno) #-- Primera linea del texto
            print (node.end_lineno) #-- Ultima linea del texto
            print (node.col_offset) #-- Desplazamiento de bytes UTF-8 (Espacios tab)
            print (node)
            print (type(node))

if __name__ == "__main__":
    leer_directorio()
