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
    locali_arbol(clase)


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
