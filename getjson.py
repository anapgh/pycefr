"""
PROGRAM TO OBTAIN SUMMARIES FROM JSON
"""

import json
import os
import re

# Dictionary of all repositories and files
dict_total = {}
# Dictionary of all repositories
dict_summary = {}
# Dictionary of all files
dict_repo = {}
dict_summary['Levels'] = {}

def extract_Levels(data):
    """ Extract repository levels. """
    # Take out the repositories
    for repo in data.keys():
        dict_total[repo] = {}
        dict_repo[repo] = {}
        for file in data[repo]:
            dict_total[repo][file] = {}
            for i in data[repo][file]:
                level = i['Level']
                ini_total('Levels', level)
                if 'Levels' not in dict_repo[repo]:
                    dict_repo[repo]['Levels'] = {}
                ini_repo(repo, 'Levels', level)
                if 'Levels' not in dict_total[repo][file]:
                    # Initialize the dictionary values to 0
                    # Create the 'Levels' key
                    dict_total[repo][file]['Levels'] = {}
                ini_values(repo, file, 'Levels', level)
                clase = i['Class']
                # Remove numbers
                clase = re.sub("\s?\d", "", clase)
                if 'Class' not in dict_summary:
                    dict_summary['Class'] = {}
                ini_total('Class', clase)
                if 'Class' not in dict_repo[repo]:
                    dict_repo[repo]['Class'] = {}
                ini_repo(repo, 'Class', clase)
                if 'Class' not in dict_total[repo][file]:
                    # Initialize the dictionary values to 0
                    # Create the 'Class' key
                    dict_total[repo][file]['Class'] = {}
                ini_values(repo, file, 'Class', clase)

        write_Results(repo)


def ini_total(type, key):
    """ Initialize or increment values. """
    if key not in dict_summary[type]:
        if key != "":
            dict_summary[type][key] = 1
    else:
        dict_summary[type][key] += 1


def ini_repo(repo, type, key):
    """ Initialize or increment values. """
    if key not in dict_repo[repo][type]:
        if key != "":
            dict_repo[repo][type][key] = 1
    else:
        dict_repo[repo][type][key] += 1


def ini_values(repo, file, type, key):
    """ Initialize or increment values. """
    if key not in dict_total[repo][file][type]:
        if key != "":
            dict_total[repo][file][type][key] = 1
    else:
        dict_total[repo][file][type][key] += 1


def write_Results(repo):
    """ Create a .txt file with a summary of results. """
    # Get current path
    wd = os.getcwd()
    # Create new folder
    try:
        os.mkdir(wd + "/DATA_JSON")
    except FileExistsError:
        pass
    # Create a file for each repository
    name_file = wd + "/DATA_JSON/" + repo + '.json'
    repository = dict()
    repository[repo] = dict_total[repo]
    with open(name_file, 'w') as file:
        json.dump(repository, file, indent=4)
    # Create a total file
    name_file = wd + "/DATA_JSON/total_data.json"
    with open(name_file, 'w') as file:
        json.dump(dict_total, file, indent=4)
    # Create a summary data
    name_file = wd + "/DATA_JSON/summary_data.json"
    with open(name_file, 'w') as file:
        json.dump(dict_summary, file, indent=4)
    # Create a repo data
    name_file = wd + "/DATA_JSON/repo_data.json"
    with open(name_file, 'w') as file:
        json.dump(dict_repo, file, indent=4)


def show_Results():
    """ Returns the result of the analysis. """
    repos = dict_total.keys()
    num_files = 0
    result = '====================================='
    result += '\nRESULT OF THE ANALYSIS:'
    for keys in repos:
        files = dict_total[keys]
        for key, value in files.items():
            num_files += 1

    result += ('\nAnalyzed .py files: ' + str(num_files))

    levels = dict_summary['Levels']
    levels = sorted(levels.items())
    for key, value in levels:
        result += ('\nElements of level ' + key + ': ' + str(value))
    result += '\n====================================='
    return result


def read_Json():
    """ Read json file. """
    with open('data.json') as file:
        data = json.load(file)
        extract_Levels(data)
        result = show_Results()
        return result


if __name__ == "__main__":
    read_Json()
