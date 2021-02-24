#-- probando el modulo de ast
import ast
import os
import json
import csv

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
    print('directorio: ')
    directorio = os.listdir("/home/ana/Documentos/TFG/TFG")
    print(directorio)
    for i in range(0, len(directorio)):
        if directorio[i].endswith('.py'):
            print('fichero python: ' + str(directorio[i]))
            leer_fichero(directorio[i])


#-- Leemos el fichero y nos devuelve el arbol
def leer_fichero(fichero):
    with open(fichero) as fp:
        my_code = fp.read()
        tree = ast.parse(my_code)
        print (ast.dump(tree))
        iterar_lista(tree)


#-- Iterar lista y asignar atributos
def iterar_lista(tree):
    for i in range(0, len(SetClass)):
        for j in range(0, len(SetClass[i])):
            atrib = SetClass[i][j]
            profundizar(tree, atrib)

myData =[['Nombre fichero', 'Clase', 'Linea empiece','Linea acabado',
            'Desplazamiento', 'Nivel'], [1,1,1,1,1,1],[2,2,2,2,2,2],
            [3,3,3,3,3,3],[4,4,4,4,4,4],[5,5,5,5,5,5],[6,6,6,6,6,6]]

def leer_fichero_csv():
    myCsv = open('datos.csv', 'w'):
    with myCsv:
        writer = csv.writer(myCsv)
        writer.writerows(myData)

#-- LISTAS
def lista(tree, atrib):
    if atrib == 'ast.List':
        for node in ast.walk(tree):
            if type(node) == eval(atrib):
                print ('LISTA:')
                print(ast.literal_eval(node))
                print(node.elts)
                for node1 in ast.walk(node):
                    if type(node1) == eval(atrib):
                        print('LISTA DE LISTAS')
                        print(ast.literal_eval(node1))
                        print (node1.lineno) #-- Primera linea del texto
                        print (node1.end_lineno) #-- Ultima linea del texto
                        print (node.col_offset) #-- Desplazamiento de bytes UTF-8 (Espacios tab)
                        print('elementos:')
                        print(node1.elts)
                    else:
                        print ('LISTA NORMAL')

#-- LIST COMPREHENSION
def list_comprehension(tree, atrib):
    if atrib == 'ast.ListComp':
        for node in ast.walk(tree):
            num_comp = 0
            if type(node) == eval(atrib):
                print('LIST COMPREHENSION:')
                print(node.lineno)
                print(node.end_lineno)
                print(node.elt)
                print(node.generators)
                for i in node.generators:
                    print (i)
                    num_comp += 1
                if num_comp > 1:
                    print('ES UNA LIST COMPREHENSION ANIDADA')
                else:
                    print('ES UNA LIST COMPREHENSION NORMAL')


#-- DICCIONARIOS
def diccionario(tree, atrib):
    if atrib == 'ast.Dict':
        for node in ast.walk(tree):
            #-- Buscamos atribs
            if type(node) == eval(atrib):
                print('DICCIONARIO:')
                print (str(atrib) + ':')
                print (node.lineno) #-- Primera linea del texto
                print (node.end_lineno) #-- Ultima linea del texto
                print('Valores:')
                print(type(node.values))
                d1 = ast.literal_eval(node)
                print(d1)
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
                        print (str(atrib1) + ':')
                        print (node1.lineno) #-- Primera linea del texto
                        print (node1.end_lineno) #-- Ultima linea del texto
                        print('elementos:')
                        print(node1.elts)




def profundizar(tree, atrib):
    #lista(tree, atrib)
    list_comprehension(tree, atrib)
    #diccionario(tree, atrib)


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
    #iterar_lista()
    leer_directorio()
    leer_fichero_csv()
