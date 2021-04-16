#-- PROGRAM TO EXTRACT LEVELS FROM JSON

import json

listLevels = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']

#-- Extract repository levels
def extract_Levels(data):
    myDataLevel = ' '
    #-- Take out the repositories
    for repo in data.keys():
        #-- Initialise levels to 0
        A1, A2, B1, B2, C1, C2 = (0,0,0,0,0,0)
        for file in data[repo]:
            for i in data[repo][file]:
                level = i['Level']
                for value in listLevels:
                    if value in level:
                        if value == 'A1':
                            A1 += level.count(value)
                        elif value == 'A2':
                            A2 += level.count(value)
                        elif value == 'B1':
                            B1 += level.count(value)
                        elif value == 'B2':
                            B2 += level.count(value)
                        elif value == 'C1':
                            C1 += level.count(value)
                        elif value == 'C2':
                            C2 += level.count(value)
            #-- Save results in myDataLevel
            if not repo in myDataLevel:
                myDataLevel = ('\nREPOSITORY: ' + repo + '\n\n')

            myDataLevel += ('File: ' + file + '\n' + 'Levels: ' + '\n' + 'A1: ' +
                            str(A1) + '\n' + 'A2: ' + str(A2) + '\n' + 'B1: ' +
                            str(B1) + '\n' + 'B2: ' + str(B2) + '\n'+ 'C1: ' +
                            str(C1) + '\n' + 'C2: ' + str(C2) + '\n\n')
        write_Results(myDataLevel)


#-- Create a .txt file with a summary of results
def write_Results(myDataLevel):
    with open('summary.txt', 'a') as file:
        file.write(myDataLevel)
        file.close()
    print('Fichero creado...')

def read_Json():
    with open('data.json') as file:
        data = json.load(file)
        print(data)
        extract_Levels(data)


if __name__ == "__main__":
    read_Json()
