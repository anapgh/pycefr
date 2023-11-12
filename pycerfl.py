"""
Main Program
"""

import ast
import os
import sys
import shlex
import subprocess
import requests
from ClassIterTree import IterTree
from getjson import read_Json
from getcsv import read_FileCsv


# Create lists of each attribute
Literals = ['ast.List', 'ast.Tuple', 'ast.Dict']
Variables = ['ast.Name']
Expressions = ['ast.Call', 'ast.IfExp', 'ast.Attribute']
Comprehensions = ['ast.ListComp', 'ast.GeneratorExp', 'ast.DictComp']
Statements = ['ast.Assign', 'ast.AugAssign', 'ast.Raise', 'ast.Assert',
              'ast.Pass']
Imports = ['ast.Import', 'ast.ImportFrom']
ControlFlow = ['ast.If', 'ast.For', 'ast.While', 'ast.Break', 'ast.Continue',
               'ast.Try', 'ast.With']
FunctionsClass = ['ast.FunctionDef', 'ast.Lambda', 'ast.Return', 'ast.Yield',
                  'ast.ClassDef']

# Create list of attribute lists
SetClass = [Literals, Variables, Expressions, Comprehensions, Statements,
            Imports, ControlFlow, FunctionsClass]


def choose_option():
    """ Choose option. """
    if type_option == 'directory':
        repo = option.split('/')[-1]
        read_Directory(option, repo)
    elif type_option == 'repo-url':
        request_url()
    elif type_option == 'user':
        run_user()
    else:
        sys.exit('Incorrect Option')


def request_url():
    """ Request url by shell. """
    values = option.split("/")
    try:
        protocol = values[0].split(':')[0]
        type_git = values[2]
        user = values[3]
        repo = values[4][0:-4]
    except:
        sys.exit('ERROR --> Usage: http://TYPEGIT/USER/NAMEREPO.git')
    # Check url
    check_url(protocol, type_git)
    # Check languaje
    check_lenguage(option, protocol, type_git, user, repo)


def check_url(protocol, type_git):
    """ Check url sintax. """
    if protocol != 'https':
        sys.exit('Usage: https protocol')
    elif type_git != 'github.com':
        sys.exit('Usage: github.com')


def check_lenguage(url, protocol, type_git, user, repo):
    """ Check lenguaje python. """
    total_elem = 0
    python_leng = False
    python_quantity = 0
    # Create the url of the api
    repo_url = (protocol + "://api." + type_git + "/repos/" + user + "/" +
                repo + "/languages")
    print("Analyzing repository languages...\n")
    # Get content
    r = requests.get(repo_url)
    # Decode JSON response into a Python dict:
    content = r.json()
    # Get used languages and their quantity
    for key in content.keys():
        print(key + ": " + str(content[key]))
        if key == 'Python':
            python_leng = True
            python_quantity = content[key]
        total_elem += content[key]
    # Check if python is 50%
    if python_leng:
        amount = total_elem/2
        if python_quantity >= amount:
            print('\nPython 50% OK\n')
            # Clone the repository
            run_url(url)
        else:
            print('\nThe repository does not contain 50% of the Python.\n')


def run_url(url):
    """ Run url. """
    command_line = "git clone " + url
    print('Run url...')
    # print(command_line)
    # List everything and separate
    args = shlex.split(command_line)
    # Run in the shell the command_line
    subprocess.call(args)
    get_directory(url)


def run_user():
    """ Run user. """
    # Create the url of the api
    user_url = ("https://api.github.com/users/" + option)
    print(user_url)
    print("Analyzing user...\n")
    try:
        # Extract headers
        headers = requests.get(user_url)
        # Decode JSON response into a Python dict:
        content = headers.json()
        # Get repository url
        repo_url = content["repos_url"]
    except KeyError:
        sys.exit('An unavailable user has been entered')
    print("Analyzing repositories...\n")
    # Extract repository names
    names = requests.get(repo_url)
    # Decode JSON response into a Python dict:
    content = names.json()
    # Show repository names
    for repository in content:
        print('\nRepository: ' + str(repository["name"]))
        url = ("https://github.com/" + option + "/" + repository["name"])
        check_lenguage(url, 'https', 'github.com', option, repository["name"])


def get_directory(url):
    """ Get the name of the downloaded repository directory. """
    # Get values rom the url
    values = url.split('/')
    # Last item in the list
    name_directory = values[-1]
    # Remove extension .git
    if '.git' in str(name_directory):
        name_directory = name_directory[0:-4]
    print("The directory is: " + name_directory)
    get_path(name_directory)


def get_path(name_directory):
    """ Get the path to the directory. """
    absFilePath = os.path.abspath(name_directory)
    # Check if the last element is a file.py
    fichero = absFilePath.split('/')[-1]
    if fichero.endswith('.py'):
        absFilePath = absFilePath.replace("/" + fichero, "")
    print("This script absolute path is ", absFilePath)
    read_Directory(absFilePath, name_directory)


def read_Directory(absFilePath, repo):
    """ Extract the .py files from the directory. """
    pos = ''
    print('Directory: ')
    path = absFilePath
    try:
        directory = os.listdir(path)
        print(directory)
        for i in range(0, len(directory)):
            if directory[i].endswith('.py'):
                print('Python File: ' + str(directory[i]))
                pos = path + "/" + directory[i]
                read_File(pos, repo)
            elif '.' not in directory[i]:
                print('\nOpening another directory...\n')
                path2 = absFilePath + '/' + directory[i]
                try:
                    read_Directory(path2, directory[i])
                except NotADirectoryError:
                    pass
    except FileNotFoundError:
        pass



def read_File(pos, repo):
    """ Read the file and return the tree. """
    with open(pos) as fp:
        my_code = fp.read()
        try:
            tree = ast.parse(my_code)
            # print (ast.dump(tree))
            iterate_List(tree, pos, repo)
        except SyntaxError:
            print('There is a misspelled code')
            pass

def read_FileContents(pos, code, repo):
    """ Read the chunk, file and return the tree. """
    try:
        tree = ast.parse(code)
        # print (ast.dump(tree))
        iterate_ListContents(tree, pos, repo)
    except SyntaxError:
        print('There is a misspelled code')
        pass

def iterate_ListContents(tree, pos, repo):
    """ Iterate list and assign attributes."""
    for i in range(0, len(SetClass)):
        for j in range(0, len(SetClass[i])):
            attrib = SetClass[i][j]
            object = IterTree(tree, attrib, pos, repo)

def iterate_List(tree, pos, repo):
    """ Iterate list and assign attributes."""
    for i in range(0, len(SetClass)):
        for j in range(0, len(SetClass[i])):
            attrib = SetClass[i][j]
            deepen(tree, attrib, pos, repo)


def deepen(tree, attrib, pos, repo):
    """ Create class object """
    file = pos.split('/')[-1]
    object = IterTree(tree, attrib, file, repo)


def summary_Levels():
    """ Summary of directory levels """
    result = read_Json()
    read_FileCsv()
    print(result)


if __name__ == "__main__":
    try:
        type_option = sys.argv[1]
        option = sys.argv[2]
    except:
        sys.exit("Usage: python3 file.py type-option('directory', " +
                 "'repo-url', 'user') option(directory, url, user)")
    choose_option()
    summary_Levels()