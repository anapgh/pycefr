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
Comprehensions = ['ListComp', 'SetComp', 'GeneratorExpr', 'DictComp',
                  'comprehension']
Statements = ['Assig', 'AnnAsign', 'AugAssign', 'Raise', 'Assert', 'Delete',
              'Pass']
Imports = ['Import', 'ImportFrom', 'alias']
ControlFlow = ['If', 'For', 'While', 'Break', 'Continue', 'Try',
               'ExceptHandler', 'With', 'Withitem']
FunctionsClass = ['FunctionDef', 'Lambda', 'arguments', 'arg', 'Return',
                   'Yield', 'YieldFrom', 'Global', 'Nonlocal', 'ClassDef']
AsyncAwait = ['AsyncDFunctionDef', 'Await', 'AsyncFor', 'AsyncWith']

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
    locali_arbol(clase)


def locali_arbol(clase):
    for node in ast.walk(tree):
        #-- Buscamos LITERALES
        if type(node) == clase:
            print (str(clase) + ':')
            print (node.lineno) #-- Primera linea del texto
            print (node.end_lineno) #-- Ultima linea del texto
            print (node.col_offset) #-- Desplazamiento de bytes UTF-8 (Espacios tab)
            print (node)
            print (type(node))

if __name__ == "__main__":
    iterar_lista()
    print ("hola")
