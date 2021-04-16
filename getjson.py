
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
                    dict_total[repo][file]['Levels'] = {}
                ini_values(repo, file, 'Levels', level)
                #get_level(level, repo, file)
                clase = i['Class']
                if not 'Class' in dict_total[repo][file]:
                    #-- Initialize the dictionary values to 0
                    #-- Create the 'Class' key
                    dict_total[repo][file]['Class'] = {}
                ini_values(repo, file, 'Class', clase)

        write_Results(repo)
    #print(dict_total)


def ini_values(repo, file, type, key):
    if not key in dict_total[repo][file][type]:
        if key != "":
            dict_total[repo][file][type][key] = 1
    else:
        dict_total[repo][file][type][key] += 1


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
