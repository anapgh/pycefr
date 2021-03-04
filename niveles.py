#-- NIVELES

#-- NIVEL LIST COMPREHENSION
def nivel_ListComp(self):
    numComp = 0
    for i in range(0, len(self.node.generators)):
        numComp += 1
    if numComp > 1:
        print('ES UNA LIST COMPREHENSION ANIDADA')
        self.nivel = 'C2'
        self.clase = str(numComp) + ' ' + str(type(self.node))
    else:
        print('ES UNA LIST COMPREHENSION NORMAL')
        self.nivel = 'C1'
        self.clase = type(self.node)
