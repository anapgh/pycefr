#-- probando el modulo de ast
import ast
import os
from ClassIterTree import ClassIterTree

#-- Creamos listas de cada atrib
Literals = ['ast.Constant', 'ast.FormattedValue', 'ast.JoinedStr', 'ast.List', 'ast.Tuple', 'ast.Set',
            'ast.Dict']

Variables = ['ast.Name', 'ast.Del', 'ast.Starred']
Expressions = ['ast.Expr', 'ast.UnaryOp', 'ast.UAdd', 'ast.USub', 'ast.Invert', 'ast.BinOp',
                'ast.Div', 'ast.LShift', 'ast.RShift', 'ast.BitOr', 'ast.BitXor',
                'ast.BitAnd', 'ast.MatMult', 'ast.BoolOp', 'ast.Compare', 'ast.LtE',
                'ast.GtE', 'ast.Is', 'ast.IsNot', 'ast.NotIn', 'ast.Call', 'ast.IfExp',
                'ast.Attribute', 'ast.NamedExpr']
Subscripting = ['ast.Subscript']
Comprehensions = ['ast.ListComp', 'ast.SetComp', 'ast.GeneratorExp', 'ast.DictComp']
Statements = ['ast.Assign', 'ast.AnnAssign', 'ast.AugAssign', 'ast.Raise', 'ast.Assert', 'ast.Delete',
              'ast.Pass']
Imports = ['ast.Import', 'ast.ImportFrom']
ControlFlow = ['ast.If', 'ast.For', 'ast.While', 'ast.Break', 'ast.Continue', 'ast.Try',
               'ast.ExceptHandler', 'ast.With']
FunctionsClass = ['ast.FunctionDef', 'ast.Lambda', 'ast.arg', 'ast.Return',
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
        #print (ast.dump(tree))
        iterar_lista(tree, pos)


#-- Iterar lista y asignar atributos
def iterar_lista(tree, pos):
    for i in range(0, len(SetClass)):
        for j in range(0, len(SetClass[i])):
            atrib = SetClass[i][j]
            profundizar(tree, atrib, pos)


def profundizar(tree, atrib, pos):
    objeto = ClassIterTree(tree, atrib, pos)


if __name__ == "__main__":
    leer_directorio()
