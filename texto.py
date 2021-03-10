
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
Rec = namedtuple('rec', ['name', 'age', 'jobs'])

"""
#-- STRINGS
#-- Crear un string NORMAL
S = 'spam'

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
'spam' in S:

#-- Strings comprehension
S = 'spam'
s = [c * 2 for c in S]

#-- Con 'map':
ord = 'hola'
S = 'spam'
s = map(ord, S)
"""
