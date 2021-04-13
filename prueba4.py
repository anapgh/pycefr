#-- MAIN PROGRAMME

import ast
import os
from ClassIterTree import ClassIterTree
from extraerjson import read_Json

#-- Create lists of each attribute
Literals = ['ast.Constant', 'ast.FormattedValue', 'ast.JoinedStr', 'ast.List', 'ast.Tuple', 'ast.Set',
            'ast.Dict']

Variables = ['ast.Name', 'ast.Starred']
Expressions = ['ast.Expr', 'ast.UnaryOp', 'ast.UAdd','ast.Invert', 'ast.BinOp',
                'ast.LShift', 'ast.RShift', 'ast.BitOr', 'ast.BitXor',
                'ast.BitAnd', 'ast.MatMult', 'ast.BoolOp', 'ast.Compare', 'ast.LtE',
                'ast.IsNot', 'ast.Call', 'ast.IfExp',
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

#-- Create list of attribute lists
SetClass = [Literals, Variables, Expressions, Subscripting, Comprehensions,
            Statements, Imports, ControlFlow, FunctionsClass, AsyncAwait]

#-- Extract the .py files from the directory
def read_Directory():
    pos = ''
    print('Directory: ')
    path = "/home/ana/Documentos/TFG/TFG"
    directory = os.listdir(path)
    print(directory)
    for i in range(0, len(directory)):
        if directory[i].endswith('.py'):
            print('Python File: ' + str(directory[i]))
            pos = path + "/" + directory[i]
            read_File(pos)


#-- Read the file and return the tree
def read_File(pos):
    with open(pos) as fp:
        my_code = fp.read()
        tree = ast.parse(my_code)
        #print (ast.dump(tree))
        iterate_List(tree, pos)


#-- Iterate list and assign attributes
def iterate_List(tree, pos):
    for i in range(0, len(SetClass)):
        for j in range(0, len(SetClass[i])):
            attrib = SetClass[i][j]
            deepen(tree, attrib, pos)

#-- Create class object
def deepen(tree, attrib, pos):
    object = ClassIterTree(tree, attrib, pos)

#-- Summary of directory levels
def summary_Levels():
    read_Json()

if __name__ == "__main__":
    read_Directory()
    summary_Levels()
