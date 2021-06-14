"""
PROGRAM FOR THE LEVELS OF EACH ATTRIBUTE
"""

import ast

# Level dictionary global variable
dictLevel = ''

# List of loop elements: break, continue, pass,for, while
listElemLoop = ['ast.Break', 'ast.Continue', 'ast.Pass', 'ast.While',
                'ast.For']
# List of imports
listImport = ['ast.Import', 'ast.ImportFrom']


with open('dicc.txt', 'r') as dict_file:
    """ Read file with levels """

    dict_text = dict_file.read()
    dictLevel = eval(dict_text)


def levels(self):
    """ Assign levels. """
    if self.attrib == 'ast.List':
        level_List(self)
    elif self.attrib == 'ast.ListComp':
        level_ListComp(self)
    elif self.attrib == 'ast.Dict':
        level_Dict(self)
    elif self.attrib == 'ast.DictComp':
        level_DictComp(self)
    elif self.attrib == 'ast.Tuple':
        level_Tuple(self)
    elif self.attrib == 'ast.Call':
        type_Call(self)
    elif self.attrib == 'ast.Assign':
        level_Assign(self)
    elif self.attrib == 'ast.AugAssign':
        level_Assign(self)
    elif self.attrib == 'ast.If':
        level_If(self)
    elif self.attrib == 'ast.IfExp':
        level_If(self)
    elif self.attrib in listElemLoop:
        type_ElemLoop(self)
    elif self.attrib == 'ast.FunctionDef':
        level_FunctionDef(self)
    elif self.attrib == 'ast.Return':
        level_Return(self)
    elif self.attrib == 'ast.Lambda':
        level_Lambda(self)
    elif self.attrib == 'ast.Yield':
        level_GeneratorFunct(self)
    elif self.attrib == 'ast.GeneratorExp':
        level_GeneratorExpr(self)
    elif self.attrib in listImport:
        level_Module(self)
    elif self.attrib == 'ast.ClassDef':
        level_Class(self)
    elif self.attrib == 'ast.Attribute':
        level_atributte(self)
        specialClassAttributes(self)
    elif self.attrib == 'ast.Name':
        typeName(self)
    elif self.attrib == 'ast.Try':
        level_Try(self)
    elif self.attrib == 'ast.Raise':
        level_Raise(self)
    elif self.attrib == 'ast.Assert':
        level_Assert(self)
    elif self.attrib == 'ast.With':
        level_With(self)


def level_List(self):
    """ List level. """
    numList = 0
    numDict = 0
    # Check for lists
    if 'ast.List' in str(self.node.elts):
        numList = str(self.node.elts).count('ast.List')
        self.level = dictLevel['List'][1]['nested']
        self.clase = (str(numList) + ' Nested List')
    elif 'ast.Dict' in str(self.node.elts):
        numDict = str(self.node.elts).count('ast.Dict')
        self.level = dictLevel['List'][2]['with-dict']
        self.clase = (str(numDict) + ' Dictionary List')
    else:
        self.level = dictLevel['List'][0]['simple']
        self.clase = ('Simple List')


def level_ListComp(self):
    """ List comprehension level. """
    numComp = 0
    ifExp = 0
    self.level = dictLevel['ListComp'][0]['simple']
    self.clase = ('Simple List Comprehension')
    for i in range(0, len(self.node.generators)):
        numComp += 1
        ifExp += 1
        if (self.node.generators[i].ifs) != []:
            self.level = dictLevel['ListComp'][2]['with-if']
            self.clase = ('List Comprehension with ' + str(ifExp) +
                          'If statements')
        if numComp > 1:
            self.level = dictLevel['ListComp'][1]['nested']
            self.clase = (str(numComp) + 'Nested List Comprehension with')


def level_Dict(self):
    """ Dictionary Level. """
    numList = 0
    numDict = 0
    # Check for dictionaries
    if 'ast.Dict' in str(self.node.values):
        numDict = str(self.node.values).count('ast.Dict')
        self.level = dictLevel['Dict'][1]['nested']
        self.clase = (str(numDict) + ' Nested Dictionary')
        # Check for lists inside dictionary dictionaries
        for i in range(0, len(self.node.values)):
            if 'ast.List' in str(self.node.values[i].values):
                numList += str(self.node.values[i].values).count('ast.List')
                self.level = dictLevel['Dict'][3]['with-dict-list']
                self.clase = (str(numList) + ' List in ' + str(numDict) +
                              'Dictionary of Dictionary')
    # Check for lists
    elif 'ast.List' in str(self.node.values):
        numList = str(self.node.values).count('ast.List')
        self.level = dictLevel['Dict'][2]['with-list']
        self.clase = str(numList) + ' List Dictionary'
    else:
        self.level = dictLevel['Dict'][0]['simple']
        self.clase = 'Simple Dictionary'


def level_DictComp(self):
    """ Dict Comprehension level. """
    numIfs = 0
    ifExp = 0
    numDictComp = 0
    for i in self.node.generators:
        numIfs += str(i.ifs).count('ast.Compare')
        if numIfs > 0:
            self.level = dictLevel['DictComp'][1]['with-if']
            self.clase = ('Dictionary Comprehension with ' + str(numIfs) + ' If statements')
        else:
            self.level = dictLevel['DictComp'][0]['simple']
            self.clase = 'Simple Dictionary Comprehension'
    if 'ast.IfExp' in str(self.node.value):
        ifExp += str(self.node.value).count('ast.IfExp')
        self.level = dictLevel['DictComp'][2]['with-if-else']
        self.clase = ('Dictionary Comprehension with ' + str(ifExp) + ' if expression (If-Else)')
    elif 'ast.DictComp' in str(self.node.value):
        numDictComp += str(self.node.value).count('ast.DictComp')
        self.level = dictLevel['DictComp'][3]['nested']
        self.clase = (str(numDictComp) + ' Nested Dictionary Comprehension')


def level_Tuple(self):
    """ Tuple Level. """
    numTuple = 0
    for i in self.node.elts:
        numTuple += str(self.node.elts).count('ast.Tuple')
        if numTuple > 0:
            self.level = dictLevel['Tuple'][1]['nested']
            self.clase = (str(numTuple) + ' Nested Tuple')
        else:
            self.level = dictLevel['Tuple'][0]['simple']
            self.clase = ('Simple Tuple')


# List of file attributes
list_File_Attr = ['write', 'read', 'readline', 'writelines']
# List of tools loop coding
list_LoopCoding = ['range', 'zip', 'map', 'enumerate']
# List of static class
listStaticClass = ['staticmethod', 'classmethod']


def type_Call(self):
    """ Types of calls. """
    value = ''
    if 'ast.Attribute' in str(self.node.func):
        if (self.node.func.attr) in list_File_Attr:
            value = self.node.func.attr
            level_Files(self, value)
    elif 'ast.Name' in str(self.node.func):
        if (self.node.func.id) == 'open':
            value = 'open'
            level_Files(self, value)
        elif (self.node.func.id) == 'print':
            value = 'print'
            level_Print(self, value)
        elif (self.node.func.id) in list_LoopCoding:
            value = self.node.func.id
            level_LoopCoding(self, value)
        elif (self.node.func.id) in listStaticClass:
            value = self.node.func.id
            level_StaticClass(self, value)
        elif (self.node.func.id) == 'super':
            level_SuperFunction(self)


def level_Files(self, value):
    """ Files level. """
    if (value) == 'open':
        self.level = dictLevel['File'][0]['open']
        self.clase = ("Files --> 'open' call function")
    elif value in list_File_Attr:
        level = dictLevel['File']
        for i in range(1, len(level)):
            keys = dictLevel['File'][i].keys()
            for k in keys:
                if k == value:
                    self.level = dictLevel['File'][i][k]
                    self.clase = ("Files --> '" + value + "' call function")


def level_Print(self, value):
    """ Print level. """
    self.level = dictLevel['Print'][0]['simple']
    self.clase = ('Print')


def level_Assign(self):
    """ Level Assignments. """
    op = ''
    if self.attrib == 'ast.Assign':
        self.level = dictLevel['Assign'][0]['simple']
        self.clase = ('Simple Assignment')
        if 'ast.BinOp' in str(self.node.value):
            self.level = dictLevel['Assign'][1]['with-sum']
            self.clase = ('Assigment with sum (total = total + 1)')
    else:
        self.level = dictLevel['Assign'][2]['increments']
        if 'ast.Add' in str(self.node.op):
            op = 'increase amount'
        elif 'ast.Sub' in str(self.node.op):
            op = 'decrease subtraction'
        elif 'ast.Mult' in str(self.node.op):
            op = 'increase multiplication'
        self.clase = ('Simplified incremental Assignment with ' + op)


def level_NameMain(self):
    """ Expression if __name __ == '__main__' level. """
    name = False
    eq = False
    constant = False
    if 'ast.Compare' in str(self.node.test):
        if 'ast.Name' in str(self.node.test.left):
            if self.node.test.left.id == '__name__':
                name = True
        if 'ast.Eq' in str(self.node.test.ops):
            eq = True
        for i in self.node.test.comparators:
            if 'ast.Constant' in str(i):
                if i.value == '__main__':
                    constant = True
        if (name and eq and constant):
            return True


def level_If(self):
    """ If statements level. """
    orelse = 0
    if self.attrib == 'ast.If':
        self.level = dictLevel['If-Statements'][0]['simple']
        self.clase = ('Simple If statements')
        # Check the if expression
        name = level_NameMain(self)
        if name:
            self.level = dictLevel['If-Statements'][2]['__name__']
            self.clase = ("If statements using → __name__ == ‘__main__’")
    elif self.attrib == 'ast.IfExp':
        self.level = dictLevel['If-Statements'][1]['expression']
        self.clase = ('If statements expression (else)')


def type_ElemLoop(self):
    """ Loop element type. """
    if self.attrib == 'ast.While':
        level_While(self)
    elif self.attrib == 'ast.Break':
        level_Break(self)
    elif self.attrib == 'ast.Continue':
        level_Continue(self)
    elif self.attrib == 'ast.Pass':
        level_Pass(self)
    elif self.attrib == 'ast.For':
        level_For(self)


def level_While(self):
    """ While level. """
    if self.node.orelse == []:
        self.clase = ('While with Else Loop')
        self.level = dictLevel['Loop'][4]['while-else']
    else:
        self.clase = ('Simple While Loop')
        self.level = dictLevel['Loop'][3]['while-simple']


def level_Break(self):
    """ Break level. """
    self.level = dictLevel['Loop'][0]['break']
    self.clase = ("'break' statement")


def level_Continue(self):
    """ Continue level. """
    self.level = dictLevel['Loop'][1]['continue']
    self.clase = ("'continue' statement")


def level_Pass(self):
    """ Pass level. """
    self.level = dictLevel['Loop'][2]['pass']
    self.clase = ("'pass' statement")


def level_For(self):
    """ For level. """
    numFor = 0
    numList = 0
    numTupleI = 0
    numTupleT = 0
    self.level = dictLevel['Loop'][5]['for-simple']
    self.clase = ('Simple For Loop')
    if 'ast.For' in str(self.node.body):
        numFor += (str(self.node.body)).count('ast.For')
        self.level = dictLevel['Loop'][6]['for-nested']
        self.clase = (str(numFor) + ' Nested For Loop')
    if 'ast.Tuple' in str(self.node.target):
        self.level = dictLevel['Loop'][7]['for-tuple-name']
        numTupleT += (str(self.node.target)).count('ast.Tuple')
        self.clase = ('For Loop with Tuple as name')
    if 'ast.List' in str(self.node.iter):
        self.level = dictLevel['Loop'][8]['for-list-iterate']
        numList += (str(self.node.iter)).count('ast.List')
        self.clase = ('For Loop with ' + str(numList) + ' List to iterate')
    elif 'ast.Tuple' in str(self.node.iter):
        self.level = dictLevel['Loop'][9]['for-tuple-iterate']
        numTupleI += (str(self.node.iter)).count('ast.Tuple')
        self.clase = ('For Loop with ' + str(numTupleI) + ' Tuples to iterate')


def level_LoopCoding(self, value):
    """ Loop coding tecniques levels. """
    if value == 'range':
        self.level = dictLevel['Loop'][10]['range']
    elif value == 'zip':
        self.level = dictLevel['Loop'][11]['zip']
    elif value == 'map':
        self.level = dictLevel['Loop'][12]['map']
    elif value == 'enumerate':
        self.level = dictLevel['Loop'][13]['enumerate']
    self.clase = ("'" + value + "' call function")


def level_FunctionDef(self):
    """ Level functions. """
    self.level = dictLevel['FunctionDef'][0]['simple']
    self.clase = ('Function')
    # Classify according to the arguments passed
    level_DefArguments(self)
    # Check for recursive function
    level_RecursiveFunction(self)
    # Check for decorators
    level_Decorators(self, 'Function')


def level_DefArguments(self):
    """ Level of arguments passed to functions. """
    # simpleargument
    if self.node.args.args != []:
        self.clase += (' with Simple argument')
    # Default arguments
    if self.node.args.defaults != []:
        self.level = dictLevel['FunctionDef'][1]['argum-default']
        self.clase += (' with Default argument')
    # * Arguments
    if self.node.args.vararg is not None:
        self.level = dictLevel['FunctionDef'][2]['argum-*']
        self.clase += (' with * argument ')
    # Keyword-only arguments
    if self.node.args.kwonlyargs != []:
        self.level = dictLevel['FunctionDef'][4]['argum-keyword-only']
        self.clase += (' with Keyword-Only argument')
    # ** arguments
    if self.node.args.kwarg is not None:
        self.level = dictLevel['FunctionDef'][3]['argum-**']
        self.clase += (' with ** argument')


def level_Return(self):
    """ Return level. """
    self.level = dictLevel['Return'][0]['simple']
    self.clase = ('Return')


def level_Lambda(self):
    """ Lambda level. """
    self.level = dictLevel['Lambda'][0]['simple']
    self.clase = ('Lambda')


def level_RecursiveFunction(self):
    """ Recursive function level. """
    for i in ast.walk(self.node):
        if 'ast.Call' in str(i):
            try:
                if i.func.id == self.node.name:
                    self.level = dictLevel['FunctionDef'][5]['recursive']
                    self.clase = ('Recursive Functions')
            except:
                pass


def level_GeneratorFunct(self):
    """ Generator function level (yield). """
    self.level = dictLevel['Generators'][0]['function']
    self.clase = ('Generator Function (yield)')


def level_GeneratorExpr(self):
    """ Generator expression level. """
    self.level = dictLevel['Generators'][1]['expression']
    self.clase = ('Generator Expression')


# List of important modules
listModules = ['struct', 'pickle', 'shelve', 'dbm', 're', 'importlib']


def nameModules(self, name):
    """ Important modules levels. """
    for i in range(0, len(name)):
        if name[i] in listModules:
            level = dictLevel['Modules']
            for j in range(0, len(level)):
                keys = dictLevel['Modules'][j].keys()
                for k in keys:
                    if k == name[i]:
                        self.level = dictLevel['Modules'][j][k]
                        self.clase += ("'" + k + "' module")


def level_AsExtension(self):
    """ 'as' etension level """
    for i in self.node.names:
        if i.asname is not None:
            self.level = dictLevel['Import'][4]['as-extension']
            self.clase += (" with 'as' extension ")


def level_From(self):
    """ From level. """
    # Check whether it is relative or absolute import
    if (self.node.level == 1) or (self.node.level == 2):
        self.level = dictLevel['Import'][2]['from-relative']
        self.clase = ('Relative From')
    # Check if from *statements
    for i in self.node.names:
        if i.name == '*':
            self.level = dictLevel['Import'][3]['from-*statements']
            self.clase += (' with *statements ')


def level_Module(self):
    """ Modules level. """
    nameModule = []
    if self.attrib == 'ast.Import':
        self.level = dictLevel['Import'][0]['import']
        self.clase = ('Import')
        for i in self.node.names:
            nameModule.append(i.name)
    else:
        self.level = dictLevel['Import'][1]['from-simple']
        self.clase = ('From')
        level_From(self)
        nameModule.append(self.node.module)
    level_AsExtension(self)
    nameModules(self, nameModule)


def PrivateClass(self):
    """ Private class function. """
    for funct in self.node.body:
        # Check if the function is private
        if(funct.name.startswith('__')) and (not funct.name.endswith('__')):
            self.level = dictLevel['Class'][5]['private']
            self.clase += (' Private Methods ' + str(funct.name) +
                           ' of the class')
    # Check for private attributes/methods
        for i in ast.walk(funct):
            if 'ast.Attribute' in str(i):
                if (i.attr.startswith('__')) and (not i.attr.endswith('__')):
                    self.level = dictLevel['Class'][5]['private']
                    self.clase += (' Private Attributes ' + str(i.attr) +
                                   ' of the class')


def constrMethod(self):
    """ Level of the constructor method. """
    for i in self.node.body:
        if i.name == '__init__':
            self.level = dictLevel['Class'][2]['__init__']
            self.clase += (' Using the constructor method --> ' + str(i.name))


# List of descriptors
listDescriptors = ['__get__', '__set__', '__delete__']


def Descriptors(self):
    """ Descriptor level."""
    for elem in self.node.body:
        if elem.name in listDescriptors:
            self.level += dictLevel['Class'][3]['descriptors']
            self.clase += (' with Descriptors ' + str(elem.name))


def level_Properties(self):
    """ Properties level. """
    for node in self.node.body:
        for elem in ast.walk(node):
            if 'ast.Call' in str(elem):
                try:
                    if elem.func.id == 'property':
                        self.level = dictLevel['Class'][4]['properties']
                        self.clase += (' with Class Properties ')
                except:
                    pass


def level_Class(self):
    """ Class level. """
    self.level = dictLevel['Class'][0]['simple']
    self.clase = ('Simple Class ')
    # Check for inherited class
    for i in self.node.bases:
        try:
            self.level = dictLevel['Class'][1]['inherited']
            self.clase = ('Inherited Class from ' + str(i.id))
        except:
            pass
    # Check for properties
    level_Properties(self)
    # Check the function name
    if 'ast.FunctionDef' in str(self.node.body):
        try:
            # Check for constructor method
            constrMethod(self)
            # Check for descriptors
            Descriptors(self)
            # Check for private functions and attributes
            PrivateClass(self)
            # Check for metaclasses in functions
            level_Metaclass(self, 'function')
        except:
            pass
    # Check for class decorators
    level_Decorators(self, 'Class')
    # Check for metaclasses
    level_Metaclass(self, 'header')


# List of special attributes of CLASSES
listClassAttr = ['__class__', '__dict__']


def level_atributte(self):
    """ Simple attribute level."""
    self.level = dictLevel['Attributes'][0]['simple']
    self.clase = ('Simple Atributte')


def specialClassAttributes(self):
    """ Special class attrbutes level. """
    if self.node.attr in listClassAttr:
        level = dictLevel['Attributes']
        for i in range(1, len(level)):
            keys = dictLevel['Attributes'][i].keys()
            for k in keys:
                if k == self.node.attr:
                    self.level = dictLevel['Attributes'][i][k]
                    self.clase = ('Special Class Attribute ' + str(self.node.attr))


def level_StaticClass(self, value):
    """ Static and class method level. """
    level = dictLevel['Static']
    for i in range(0, len(level)):
        keys = dictLevel['Static'][i].keys()
        for k in keys:
            if k == value:
                self.level = dictLevel['Static'][i][k]
                self.clase = (value)


def level_Decorators(self, type):
    """ Functions and classes decorators level. """
    for i in self.node.decorator_list:
        level = dictLevel['Decorators']
        for j in range(0, len(level)):
            keys = dictLevel['Decorators'][j].keys()
            for k in keys:
                if k == type:
                    self.level = dictLevel['Decorators'][j][k]
                    self.clase = ('Decorator ' + type)


def typeName(self):
    """ Type of ast.name. """
    if self.node.id == '__metaclass__':
        level_Metaclass(self, 'attrib')
    elif self.node.id == '__slots__':
        level_Slots(self)


def level_Metaclass(self, pos):
    """ Metaclass level. """
    # Creation method __new__
    if pos == 'function':
        for i in self.node.body:
            if i.name == '__new__':
                for argum in i.args.args:
                    if (argum.arg) == 'meta':
                        self.level = dictLevel['Metaclass'][0]['__new__']
                        self.clase += (' Metaclass (3.X) created with --> __new__')
    # Class header
    elif pos == 'header':
        for i in self.node.keywords:
            if i.arg == 'metaclass':
                self.level = dictLevel['Metaclass'][1]['metaclass']
                self.clase += (" Metaclass created in the class header --> 'metaclass = '"
                               + i.value.id)
    # As an attribute, 2.X
    elif pos == 'atrib':
        self.level = dictLevel['Metaclass'][2]['__metaclass__']
        self.clase = ('Metaclass (2.X) created as attribute with --> __metaclass__')


def level_Slots(self):
    """ __slots__ level. """
    self.level = dictLevel['Slots'][0]['__slots__']
    self.clase = ('Attribute  statements __slots__')


def level_SuperFunction(self):
    """ Super built-in function level. """
    self.level = dictLevel['SuperFunction'][0]['simple']
    self.clase = ('Super Function')


# Exception levels
def level_Try(self):
    """ try level. """
    self.clase = ('Exception --> try')
    if 'ast.Try' in str(self.node.body):
        self.level = dictLevel['Exception'][2]['try/try']
        self.clase += ('/try')
    if (self.node.handlers) != []:
        self.level = dictLevel['Exception'][0]['try/except']
        self.clase += ('/except')
    if (self.node.orelse) != []:
        self.level = dictLevel['Exception'][1]['try/else/except']
        self.clase += ('/else')
    if (self.node.finalbody) != []:
        self.level = dictLevel['Exception'][4]['try/except/finally']
        self.clase += ('/finally')


def level_Raise(self):
    """ raise level. """
    self.level = dictLevel['Exception'][6]['raise']
    self.clase = ("'raise' exception")


def level_Assert(self):
    """ assert level. """
    self.level = dictLevel['Exception'][7]['assert']
    self.clase = ("'assert' exception")


def level_With(self):
    """ with level. """
    self.level = dictLevel['With'][0]['simple']
    self.clase = ('With')
