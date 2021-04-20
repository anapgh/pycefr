
import json
import os

dict_total = {}
dict_summary = {}

#-- Extract repository levels
def extract_Levels(data):
    #-- Take out the repositories
    for repo in data.keys():
        dict_total[repo] = {}
        for file in data[repo]:
            dict_total[repo][file] = {}
            for i in data[repo][file]:
                level = i['Level']
                if not 'Levels' in dict_summary:
                    dict_summary['Levels'] = {}
                ini_total('Levels', level)
                if not 'Levels' in dict_total[repo][file]:
                    #-- Initialize the dictionary values to 0
                    #-- Create the 'Levels' key
                    dict_total[repo][file]['Levels'] = {}
                ini_values(repo, file, 'Levels', level)
                clase = i['Class']
                if not 'Class' in dict_summary:
                    dict_summary['Class'] = {}
                ini_total('Class', clase)
                if not 'Class' in dict_total[repo][file]:
                    #-- Initialize the dictionary values to 0
                    #-- Create the 'Class' key
                    dict_total[repo][file]['Class'] = {}
                ini_values(repo, file, 'Class', clase)

        write_Results(repo)
    #print(dict_total)
    #print(dict_summary)


def ini_values(repo, file, type, key):
    if not key in dict_total[repo][file][type]:
        if key != "":
            dict_total[repo][file][type][key] = 1
    else:
        dict_total[repo][file][type][key] += 1

def ini_total(type, key):
    if not key in dict_summary[type]:
        if key != "":
            dict_summary[type][key] = 1
    else:
        dict_summary[type][key] += 1

#-- Create a .txt file with a summary of results
def write_Results(repo):
    #-- get current path
    wd = os.getcwd()
    #-- create new folder
    try:
        os.mkdir(wd + "/DATA_JSON")
    except FileExistsError:
        pass
    #-- Create a file for each repository
    name_file =  wd + "/DATA_JSON/"+ repo + '.json'
    repository = dict()
    repository[repo] = dict_total[repo]
    with open(name_file, 'w') as file:
        json.dump(repository, file, indent=4)
        print('Fichero creado...')
    #-- Create a total file
    name_file =  wd + "/DATA_JSON/total_data.json"
    with open(name_file, 'w') as file:
        json.dump(dict_total, file, indent=4)
    #-- Create a summary data
    name_file =  wd + "/DATA_JSON/summary_data.json"
    with open(name_file, 'w') as file:
        json.dump(dict_summary, file, indent=4)

def read_Json():
    with open('data.json') as file:
        data = json.load(file)
        #print(data)
        extract_Levels(data)


if __name__ == "__main__":
    read_Json()
