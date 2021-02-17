#-- probando el modulo de ast
import ast

#-- Creamos listas de cada clase
Literals = ['Constant', 'FormattedValue', 'JoinedStr', 'List', 'Tuple', 'Set',
            'Dict']

Variables = ['Name', 'Load', 'Store', 'Del', 'Starred']
Expressions = ['Expr', 'UnaryOp', 'UAdd', 'USub', 'Not', 'Invert', 'BinOp',
                'Add', 'Sub', 'Mult', 'Div', 'FloorDiv', 'Mod', 'Pow', 'LShift',
                'RShift', 'BitOr', 'BitXor', 'BitAnd', 'MatMult', 'BoolOp',
                'And', 'Or', 'Compare', 'Eq', 'NotEq', 'Lt', 'LtE', 'Gt', 'GtE',
                'Is', 'IsNot', 'In', 'NotIn', 'Call', 'keyword', 'IfExp',
                'Attribute', 'NamedExpr']
Subscripting = ['Subscript', 'Slice']
Comprehensions = ['ListComp', 'SetComp', 'GeneratorExp', 'DictComp',
                  'comprehension']
Statements = ['Assig', 'AnnAssign', 'AugAssign', 'Raise', 'Assert', 'Delete',
              'Pass']
Imports = ['Import', 'ImportFrom', 'alias']
ControlFlow = ['If', 'For', 'While', 'Break', 'Continue', 'Try',
               'ExceptHandler', 'With', 'Withitem']
FunctionsClass = ['FunctionDef', 'Lambda', 'arguments', 'arg', 'Return',
                   'Yield', 'YieldFrom', 'Global', 'Nonlocal', 'ClassDef']
AsyncAwait = ['AsyncFunctionDef', 'Await', 'AsyncFor', 'AsyncWith']

#-- Creamos lista de listas de clases
SetClass = [Literals, Variables, Expressions, Subscripting, Comprehensions,
          Statements, Imports, ControlFlow, FunctionsClass, AsyncAwait]

#-- Leemos el fichero y nos devuelve el arbol
with open("smallsmilhandler.py") as fp:
    my_code = fp.read()
    tree = ast.parse(my_code)
    print (ast.dump(tree))


def iterar_lista():
    for i in range(0, len(SetClass)):
        for j in range(0, len(SetClass[i])):
            atrib = SetClass[i][j]
            asignar_clase(atrib)

def asignar_clase(atrib):
    clase = ''
    #-- Literals
    if atrib == 'Constant':
        clase = ast.Constant
    elif atrib == 'FormattedValue':
        clase = ast.FormattedValue
    elif atrib == 'JoinedStr':
        clase = ast.JoinedStr
    elif atrib == 'List':
        clase = ast.List
    elif atrib == 'Tuple':
        clase = ast.Tuple
    elif atrib == 'Set':
        clase = ast.Set
    elif atrib == 'Dict':
        clase = ast.Dict
    #-- Variables
    elif atrib == 'Name':
        clase = ast.Name
    elif atrib == 'Load':
        clase == ast.Load
    elif atrib == 'Store':
        clase == ast.Store
    elif atrib == 'Del':
        clase == ast.Del
    elif atrib == 'Starred':
        clase = ast.Starred
    #-- Expressions
    elif atrib == 'Expr':
        clase = ast.Expr
    elif atrib == 'UnaryOp':
        clase = ast.UnaryOp
    elif atrib == 'UAdd':
        clase = ast.UAdd
    elif atrib == 'USub':
        clase = ast.USub
    elif atrib == 'Not':
        clase = ast.Not
    elif atrib == 'Invert':
        clase = ast.Invert
    elif atrib == 'BinOp':
        clase = ast.BinOp
    elif atrib == 'Add':
        clase = ast.Add
    elif atrib == 'Sub':
        clase = ast.Sub
    elif atrib == 'Mult':
        clase = ast.Mult
    elif atrib == 'Div':
        clase = ast.Div
    elif atrib == 'FloorDiv':
        clase = ast.FloorDiv
    elif atrib == 'Mod':
        clase = ast.Mod
    elif atrib == 'Pow':
        clase = ast.Pow
    elif atrib == 'LShift':
        clase = ast.LShift
    elif atrib == 'RShift':
        clase = ast.RShift
    elif atrib == 'BitOr':
        clase = ast.BitOr
    elif atrib == 'BitXor':
        clase = ast.BitXor
    elif atrib == 'BitAnd':
        clase = ast.BitAnd
    elif atrib =='MatMult':
        clase = ast.MatMult
    elif atrib == 'BoolOp':
        clase = ast.BoolOp
    elif atrib == 'And':
        clase = ast.And
    elif atrib == 'Or':
        clase = ast.Or
    elif atrib == 'Compare':
        clase = ast.Compare
    #elif atrib == 'Eq':
    #    clase = ast.Eq
    elif atrib == 'NotEq':
        clase = ast.NotEq
    elif atrib == 'Lt':
        clase = ast.Lt
    elif atrib == 'LtE':
        clase = ast.LtE
    elif atrib == 'Gt':
        clase = ast.Gt
    elif atrib == 'GtE':
        clase = ast.GtE
    elif atrib =='Is':
        clase = ast.Is
    elif atrib == 'IsNot':
        clase = ast.IsNot
    #elif atrib == 'In':
    #    clase = ast.In
    elif atrib == 'NotIn':
        clase = ast.NotIn
    elif atrib == 'Call':
        clase = ast.Call
    elif atrib == 'keyword':
        clase = ast.keyword
    elif atrib == 'IfExp':
        clase = ast.IfExp
    elif atrib == 'Attribute':
        clase = ast.Attribute
    elif atrib == 'NamedExpr':
        clase = ast.NamedExpr
    #-- Subscripting
    elif atrib == 'Subscript':
        clase = ast.Subscript
    elif atrib == 'Slice':
        clase = ast.Slice
    #-- Comprehensions
    elif atrib == 'ListComp':
        clase = ast.ListComp
    elif atrib == 'SetComp':
        clase = ast.SetComp
    elif atrib == 'GeneratorExp':
        clase = ast.GeneratorExp
    elif atrib == 'DictComp':
        clase = ast.DictComp
    elif atrib == 'Comprehension':
        clase = ast.Comprehension
    #-- Statements
    elif atrib == 'Assign':
        clase = ast.Assign
    elif atrib == 'AnnAssign':
        clase = ast.AnnAssign
    elif atrib == 'AugAssign':
        clase = ast.AugAssign
    elif atrib == 'Raise':
        clase = ast.Raise
    elif atrib == 'Assert':
        clase = ast.Assert
    elif atrib == 'Delete':
        clase = ast.Delete
    elif atrib == 'Pass':
        clase = ast.Pass
    #-- Imports
    elif atrib == 'Import':
        clase = ast.Import
    elif atrib == 'ImportFrom':
        clase = ast.ImportFrom
    #elif atrib == 'alias': #.. NO lineno
    #    clase = ast.alias
    #-- ControlFlow
    elif atrib == 'If':
        clase = ast.If
    elif atrib == 'For':
        clase = ast.For
    elif atrib == 'While':
        clase == ast.While
    elif atrib =='Break':
        clase = ast.Break
    elif atrib == 'Continue':
        clase = ast.Continue
    elif atrib == 'Try':
        clase = ast.Try
    elif atrib == 'ExceptHandler':
        clase = ast.ExceptHandler
    elif atrib == 'With':
        clase = ast.With
    elif atrib == 'withithem':
        clase = ast.withithem
    #-- FunctionsClass
    elif atrib == 'FunctionDef':
        clase = ast.FunctionDef
    elif atrib == 'Lambda':
        clase = ast.Lambda
    #elif atrib == 'arguments': #.. NO lineno
    #    clase = ast.arguments
    elif atrib == 'arg':
        clase = ast.arg
    elif atrib == 'Return':
        clase = ast.Return
    elif atrib == 'Yield':
        clase = ast.Yield
    elif atrib == 'YieldFrom':
        clase = ast.YieldFrom
    elif atrib == 'Global':
        clase = ast.Global
    elif atrib == 'Nonlocal':
        clase = ast.Nonlocal
    elif atrib == 'ClassDef':
        clase = ast.Nonlocal
    #-- AsyncAwait
    elif atrib == 'AsyncFunctionDef':
        clase = ast.AsyncFunctionDef
    elif atrib == 'Await':
        clase = ast.Await
    elif atrib == 'AsyncFor':
        clase == ast.AsyncFor
    elif atrib == 'AsyncWith':
        clase = ast.AsyncWith
    profundizar(clase)
    #locali_arbol(clase)

def profundizar(clase):
    if clase == ast.Dict:
        for node in ast.walk(tree):
            #-- Buscamos clases
            if type(node) == clase:
                print (str(clase) + ':')
                print (node.lineno) #-- Primera linea del texto
                print (node.end_lineno) #-- Ultima linea del texto
                #print (node.col_offset) #-- Desplazamiento de bytes UTF-8 (Espacios tab)
                #print (node)
                #print (type(node))
                print('Valores:')
                print(type(node.values))
                for node1 in ast.walk(node):
                    clase1 = ast.List
                    if type(node1) == clase1:
                        print (str(clase1) + ':')
                        print (node1.lineno) #-- Primera linea del texto
                        print (node1.end_lineno) #-- Ultima linea del texto
                        #print (node.col_offset) #-- Desplazamiento de bytes UTF-8 (Espacios tab)
                        #print (node)
                        #print (type(node))
                        print('Valores:')
                        print(node1.elts)

def locali_arbol(clase):
    for node in ast.walk(tree):
        #-- Buscamos clases
        if type(node) == clase:
            print (str(clase) + ':')
            print (node.lineno) #-- Primera linea del texto
            print (node.end_lineno) #-- Ultima linea del texto
            print (node.col_offset) #-- Desplazamiento de bytes UTF-8 (Espacios tab)
            print (node)
            print (type(node))

if __name__ == "__main__":
    iterar_lista()
