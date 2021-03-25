
#-- LISTA NORMAL
L = ['PEPE', 1,2]

#-- LISTA ANIDADA
L = ['Bob', 40,0, ['dev', 'mgr']]

#-- LISTA DE DICCIONARIO
L = ['Bob',{'pepe': 1}, 'Martin']


#-- LIST COMPREHENSION normal
L1 = [x**2 for x in range(5)]

#-- LIST COMPREHENSION + IF + EXPRESSION
L2 = [x ** 2 for x in range(10) if x % 2 == 0]

#-- LIST COMPREHENSION ANIDADAS
L3 = [num for elem in vec for num in elem]


#-- DICCIONARIO NORMAL
d1 = {'pepe': 1, 'juan': 2}

#-- DICCIONARIO DE LISTAS
d2 = {'manzana': ['rojas', 'verde', 'amarilla'], 'limon': ['amarillo', 'verde'],'pera': 'verde'}
#-- DICCIONARIO DENTRO DE DICCIONARIO (DE LISTAS)

d3 = {
  'frutas': {
     ' manzanas': [' verdes', ' 7', ' rojas', ' 5'],
      'uvas': [' negras', ' 5', ' verdes', ' 3']
   },
   ' verduras': {
      'papa': ['negras', ' 50', ' blancas', ' 20'],
      'cebolla': [' blancas', ' 30']
   },
   'cereales': {
      ' arroz': [' fino',' 600', ' largo', ' 800']
   }
}


#-- 1- DICT COMPREHENSION
D1 = {x: x*2 for x in range(10)}

#-- 2- DICT COMPREHENSION
#item price in dollars
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
dollar_to_pound = 0.76
new_price = {item: value*dollar_to_pound for (item, value) in old_price.items()}
print(new_price)

#-- 3- DICT COMPREHENSION --> CONDICIONALS: IF
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(even_dict)

#-- 4- DICT COMPREHENSION --> MULTIPLE CONDICIONALS: IF
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
new_dict = {k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40}
print(new_dict)

#-- 5- DICT COMPREHENSION --> CONDICIONALS: IF-ELSE
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
new_dict_1 = {k: ('old' if v > 40 else 'young')for (k, v) in original_dict.items()}
print(new_dict_1)

#-- 6- DICT COMPREHENSION --> ANIDADO
D2 = {k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)}

#-- TUPLAS
#-- Tupla normal
T1 = ()

#-- Tuplas aninadadas
T2 = ('Bob', ('dev', 'mgr'))

#--------------------------NO DETECTA--------------------------
#-- Conversión de tupla
T = tuple('spam')

#-- Concatenación de Tuplas
T3 = T2 * 3

#--Indexacion
#-- Accediendo a tupla mediante clave (Access by Key)
Bob = dict(name='Bob', age = 40.5, jobs = ['dev', 'mgr'])
#-- Accediendo by position
t = T2[1]

#-- Métodos: index() y count()
valores = ("Python", True, "Zope", 5)
print ("True ->", valores.count(True))
print ("'Zope' ->", valores.count('Zope'))
print ("5 ->", valores.count(5))

print (valores.index(True))
print (valores.index(5))

#-- Modulo 'namedtuple':
#-- Modulo que permite que los componentes sean accesibles por posicion y por atributo(key).
from collections import namedtuple
Rec = namedtuple('rec', ['name', 'age', 'jobs']) #-- namedtuple: ast.Call
#---------------------------------------------------------------------------------

#-- STRINGS
#-- Crear un string NORMAL
S = 'spam' #-- Name y Constant

#-- Concatenacion y repeticion
S = S + 'xyz'
S = S*3

#-- Acceder by position
s = S[0]

#-- Metodos--> pag 261

#-- Formas de iterar
#- Tradicional
for x in S:
    print(x)
#-- Otra forma
if 'spam' in S:
    print('si')

#-- Strings comprehension
S = 'spam'
s = [c * 2 for c in S] #-- dict comprehension

#-- Con 'map':
ord = 'hola'
S = 'spam'
s = map(ord, S) #-- map: ast.Call


#-- FILES
#-- Abrir y crear fichero
#-- Write:
output = open(' fichero ', 'w') #-- ast.Call
#-- Read
open(' fichero ', 'r')
input = open('fichero') #-- 'r' por defecto

#--Leer un fichero
lectura = input.read()
lectura = input.readline()

#-- Escribir un fichero
output.write()
output.writelines()

#-- Cerrar un fichero
output.close()

#-- JSON file:
#-- Devuelve estructura JSON
json.dump(rec, fp= open('testjson.txt', 'w'), indent = 4)
print(open('testjson.text').read())
#-- Devuelve diccionario de Listas
P = json.load(open('testjson'))

#-- EVAL
line = F.readline()
parts = line.split('$')
eval(parts[0])
objects = [eval(P) for P in parts]

#-- Modulo Binary Data: Struct
F = open('data.bin', 'rb')
data = F.read()
import struct
values= struct.unpack('>i4sh', data)

#-- Modulo pickle
F = open('datafile.pkl', 'rb')
import pickle
E = pickle.load( F)

#-- ASIGNACIONES
spam = 'Spam'
#-- Asiganciones con aumentos, etc.
spam = spam + 42
spam += 42
spam -= 42
spam *= 42
#--Tuple assigment
spam, ham = 'yum', 'YUM'
#-- List assigment
[spam, ham] = ['yum', 'YUM']
#-- Multiple-target assigment
spam = ham = 'lunch'
#-- Nested sequences
((a, b), c) = ('SP', 'AM')
#-- Extended sequence unpacking
a, *b = 'spam'



#-- IF STATEMENTS
#-- general format
if test1:
    print('hola')
elif test2:
    print('jeje')
else:
    print('adios')
#-- Multiway branching --> equivalente a if statements
if choice == 'spam':
    print(1.25)
elif choice == 'ham':
    print(1.99)
elif choice == 'eggs':
    print(0.99)
elif choice == 'bacon':
    print(1.10)
else:
    print('Bad choice')
#-- Multiway branching --> como no hay switch y cases
#-- usamos indexacion de dict o list
choice = 'ham'
print({'spam': 1.25, 'ham': 1.99, 'eggs': 0.99, 'bacon': 1.10}[choice])
#-- hay que poner el default
branch = {'spam': 1.25, 'ham': 1.99, 'eggs': 0.99}
print(branch.get('spam', 'Bad choice'))
print(branch.get('bacon', 'Bad choice'))
#-- Try. Tambien se puede poner como una excepción
try:
    print(branch[choice])
except KeyError:
    print('Bad choice')
#-- IF-ELSE Expressions
#-- General
if X:
    A = Y
else:
    A = Z
#-- En 1 linea.
A = Y if X else Z
#En 1 linea con operadores
A = ((X and Y) or Z)
#--Con listas
A = [Z, Y][bool(X)]

#-- WHILE LOOPS
#-- General format con else
while test:
    print('si')
else:
    print('no')
#-- Sin else
while test:
    print('si')


#-- Break, continue, pass and the Lopp else.
#-- pass
def func1():
    pass

#-- Continue
x = 10
while x:
    x = x-1
    if x % 2 != 0:
        continue
        print(x, end= ' ' )

#--Break
while True:
    name = input('Enter name: ')
    if name == 'stop':
        break
        age = input('Enter age:  ')
        print('Hello', name, '=>', int(age) ** 2)

#-- Loop else
x = y // 2
while x > 1 :
    if y % x == 0:
        print(y, 'has factor', x)
        break
        x -= 1
    else:
        print(y, 'is aprime')

#-- BUCLE FOR
#-- For ANIDADO
tems = ["aaa", 111, (4, 5), 2.01]
tests = [(4, 5), 3.14]

for key in tests:
    for item in items:
        if item == key:
            print(key, "was found")
            break
        else:
            print(key, "not found!")
#-- Lista
for x in ["spam", "eggs", "ham"]:
    print(x, end = '   ')
#-- Strings Es una herramienta más generica
S = "lumberjack"
for x in S:
    print(x, end = '   ')
#-- Tuplas.
T = ("and", "I'am", "okay")
for x in T:
    print(x, end = '   ')
#-- Tuplas anidadas
for ((a,b), c) in [((1, 2), 3), ((4, 5), 6)]:
    print(a, b, c)
#-- Extended sequence assigment in for loops
for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)

#-- LOOP CODING TECNIQUES
#-- range
list(range(5))
list(range(2, 5))
list(range(0, 10, 2))
#-- zip
dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
#-- map
list(map(ord, 'spam'))
#-- enumerate
S = 'spam'
for (offset, item) in enumerate(S):
    print(item, 'appears at offset', offset)
#-- enumerate + Comprehension
[c * i for (i, c) in enumerate(S)]
for (i, l) in enumerate(open('test.txt')):
    print('%s) %s' % (i, l.rstrip()))

#-- FUNCTIONS
#-- Con print
def printer(message):
    print('Hello' + mssage)
#-- Con return
def adder(a, b=1, *c):
    return a + b + c[0]
#-- Con yield
def squares(x):
    for i in range(x):
        yield i ** 2
#-- Con Lambda
Funcs = [lambda x: x **2, lambda x: x **3]
#-- lambda en listas
L = [lambda x: x ** 2, lambda x: x ** 3,lambda x: x ** 4]
for f in L:
    print(f(2)) # Prints 4, 8, 16
    print(L[0](3)) # Prints 9

#-- ARGUMENTOS
#-- Normal argument: Pasar argumentos por posicion.
def func(name):
    print(name)
#-- Keyword argument: Pasar arguemnto por el nombre (valor)
func(name=value)
#-- Defaults: especifica valores para los argumentos opcionales que no se pasan.
def func(name=value):
    print(name)
#-- Varargs collecting or unpacking:
def func(*name):
    print(name)
def func(**name):
    print(name)
#-- Keyword-only arguments:
def func(*other, name):
    print('hola')
def func(*, name=value):
    print('hola')
#-- Con todo
def f(a: 'annotation', b=1, c=2, *d, e, f=3, **g):
    print('toodo')
#-- Sin argumentos
def func():
    print('pepe')

#-- FUNCIONES RECURSIVAS
def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])
#-- con if-else
def mysum(L):
    return 0 if not L else L[0] + mysum(L[1:])

#-- GENERATOR FUNCTION
def gensquares(N):
    for i in range(N):
        yield i ** 2

#-- GENERATOR EXPRESSION
(x ** 2 for x in range(4))

#-- MODULOS
#-- Formas de importar:
#-- The import statements
import b.py
b.printer('hello')
#-- The from statements
from module1 import printer
module1.printer('hello')
#-- The from *statements: obtenemos copias de todos los nombres
from module1 import *
printer('hello')

#-- Namespace Nesting
X = 1
import mod2
print(X, end=' ')
print(mod2.X, end=' ')
print(mod2.mod3.X)

#-- Relative import
#-- Imports mypkg.string(Searches this package only):
from . import string
# Imports names from mypkg.string:
from .string import name1, name2
#-- Imports string sibling of mypkg :
from .. import string

#-- Declaraciones
#-- __future__
from __future__ import featurename
#-- __name__
def tester():
    print("It's Christmas in Heaven...")
if __name__ == '__main__':
    tester()

#-- The 'as' extension for import and from
import modulename as name
from modulename import attrname as name

#-- Importing modules by name string
#-- Usando __import__
modname = 'string'
string = __import__(modname)
#-- Usando la llamada importlib.import_module’
import importlib
modname = 'string'
string = importlib.import_module(modname)

#-- Modulos importantes
import struct
import pickle
import shelve
import dbm
import re
import importlib
import struct, pickle
from struct import *

#-- CLASES
#-- Crear clase
class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)
#-- Instancias de objetos
x = FirstClass()
y = FirstClass()
#-- Llamar a metodos, haciendo ref a atributos
x.setdata("King Arthur")
y.setdata(3.14159)
#-- Clase heredada
class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s"' % self.data)
#-- Funciones de sobrecarga
#-- Metodo constructor __init__, __add__, __str__
class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return '[ThirdClass: %s]' % self.data
#-- Special class Attributes
#-- Atributo incorporado .__class__
from person import Person
bob = Person('Bob Smith')
print(bob)
bob.__class__
bob.__class__.__name__
#-- Atributo incorporado .__dict__
list(bob.__dict__.keys())
for key in bob.__dict__:
    print(key, '=>', bob.__dict__[key])

#-- Pseudoprivate class attributes:
class Demo:
    def __secret(self):
        print('Nadie puede saber!')

    def public(self):
        self.__secret()

class Child(Demo):
    def __secret(self):
        print('No puedo contarte!')

#-- Slots: attribute declarations
class limiter(object):
    __slots__ = ['age', 'name', 'job']
x = limiter()

#-- Properties: Attribute Accesors
class properties(object):
    def getage(self):
        return 40
    age = property(getage, None, None, None)
x = properties()
x.age
x.name

#-- Descriptores
class AgeDesc(object):
    def __get__(self, instance, owner):
        return 40
    def __set__(self, instance, value):
        instance._age = value
    def __delete__(self, instance, value):
        print('hola')

class descriptors(object):
    age = AgeDesc()
x = descriptors()
x.age
x.age = 42
x._age

#-- Static and Class Method
class Methods:
    def imeth(self, x): print([self, x])
    # Normal instance method: passed a self
    def smeth(x):
        print([x])
    # Static: no instance passed
    def cmeth(cls, x):
        print([cls, x])
        # Class: gets class, not instance
        smeth = staticmethod(smeth)
        cmeth = classmethod(cmeth)
        # Make smeth a static method (or @: ahead)
        # Make cmeth a class method (or @: ahead)

#-- DECORATORS
#-- FUNCTION DECORATOR(funcion evuelve otra funcion)
def decorator(func):
  print("Decorator")
  return func

@decorator
def Hello():
  print("Hello World")

#-- CLASS DECORATOR (Clase envolviendo una funcion)
class Decorator(object):
  """Clase de decorador simple."""
  def __init__(self, func):
    self.func = func

  def __call__(self, *args, **kwargs):
    print('Antes de ser llamada la función.')
    retorno = self.func(*args, **kwargs)
    print('Despues de ser llamada la función.')
    print(retorno)
    return retorno

@Decorator
def function():
  print('Dentro de la función.')
  return "Retorno"


#-- CLASS DECORATOR (clase envuelve otra clase)
class Decorator(object):
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print('Dentro del decorador.')
        return self.func(*args, **kwargs)
    def __get__(self, instance, cls):
        # Retorna un método si se llama en una instancia
        return self if instance is None else MethodType(self, instance)

@Decorator
class Test(object):
  def __init__(self):
    print("Dentro de la función decorada")


#-- METACLASES
#-- Se crea on la palabra clave 'meta'
class Meta(type):
    def __new__(meta, classname, supers, classdict):
        pass
#-- Enumerada en la cabecera 'metaclass'
class C(metaclass=Meta):
    pass
#-- En 2.X se usa el atributo '__metaclass__'
class C:
    __metaclass__ = Meta

#-- SUPER BUILT-IN FUNCTION
class C:
    def act(self):
        print('spam')
class D(C):
    def act(self):
        super().act()
        print('eggs')

#-- EXCEPCIONES
#-- try/except
try:
    fetcher(x, 4)
except IndexError:
    print('got exception')
#-- try/else/except
try:
    print('hola')
except IndexError:
    pass
else:
    print('adios')
#-- try/finally
try:
    fetcher(x, 3)
finally:
    print('after fetch')
#-- try/except/finally
try:
    print('main')
except Exception1:
    print('handler1')
except Exception2:
    print('handler2')
else:
    print('else')
finally:
    print('finally')
#-- try/try
try:
    try:
        print('main-action')
    except Exception1:
        print('handler1')
except Exception2:
    print('handler2')
else:
    print('no-error')
finally:
    print('cleanup')
#-- raise
try:
    raise IndexError
except IndexError:
    print('got exception')

#-- Assert
def f(x):
    assert x < 0, 'x must be negative'
    return x ** 2

#-- with
with open(r'C:\misc\data') as myfile:
    for line in myfile:
        print(line)
