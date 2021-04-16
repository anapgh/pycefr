
import json

dict_total = {}



#-- Extract repository levels
def extract_Levels(data):
    #-- Take out the repositories
    for repo in data.keys():
        dict_total[repo] = {}
        for file in data[repo]:
            dict_total[repo][file] = {}
            for i in data[repo][file]:
                level = i['Level']
                if not 'Levels' in dict_total[repo][file]:
                    #-- Initialize the dictionary values to 0
                    #-- Create the 'Levels' key
                    dict_total[repo][file]['Levels'] = ini_values('Levels')
                get_level(level, repo, file)
                clase = i['Class']
                if not 'Class' in dict_total[repo][file]:
                    #-- Initialize the dictionary values to 0
                    #-- Create the 'Class' key
                    dict_total[repo][file]['Class'] = {}

        write_Results(repo)
    #print(dict_total)


def ini_values(type):
    dict_aux = dict()
    list_levels = []
    if type == 'Levels':
        list_levels = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']

    else:
        list_levels = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
    #-- Initialize the dictionary values to 0
    for k in list_levels:
        dict_aux[k] = 0

    return dict_aux
def get_level(level, repo, file):
    list_levels = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
    for value in list_levels:
        if value == level:
            dict_total[repo][file]['Levels'][value] += 1


def get_class(clase, repo, file):
    class_list(clase, repo, file)


def class_list(clase, repo, file):
    list_list = ['Simple List', 'Nested List', 'Dictionary List']
    for value in list_list:
        if value in str(clase):
            dict_total[repo][file]['Class'][value] += 1


#-- Create a .txt file with a summary of results
def write_Results(repo):
    name_file = repo + '.json'
    repository = dict()
    repository[repo] = dict_total[repo]
    with open(name_file, 'w') as file:
        json.dump(repository, file, indent=4)
        print('Fichero creado...')

def read_Json():
    with open('data.json') as file:
        data = json.load(file)
        #print(data)
        extract_Levels(data)


if __name__ == "__main__":
    read_Json()
