import sys
import shlex, subprocess
import os
import json
import requests

def show_menu():
    print('Choose the option to analyze:')
    print('By default, current directory: 0')
    print('Url repository: 1')
    print('User: 2')
    option = input()
    if (option == '0'):
        file = 'gitdownload.py'
        return get_path(file)
    elif(option == '1'):
        request_url()
    elif(option == '2'):
        request_user()
        pass


def request_url():
    print("Enter the Github url: ")
    url = input()
    values = url.split("/")
    try:
        protocol = values[0].split(':')[0]
        type_git = values[2]
        user = values[3]
        repo = values[4][0:-4]
    except:
        sys.exit('ERROR --> Usage: http://TYPEGIT/USER/NAMEREPO.git')
    #-- Check url
    check_url(protocol, type_git, user, repo)
    #-- Check languaje
    check_lenguage(url, protocol, type_git, user, repo)

def check_url(protocol, type_git, user, repo):
    if protocol != 'https':
        sys.exit('Usage: https protocol')
    elif type_git != 'github.com':
        sys.exit('Usage: github.com')


def check_lenguage(url, protocol, type_git, user, repo):
    total_elem = 0
    python_leng = False
    python_quantity = 0
    #-- Create the url of the api
    repo_url = (protocol + "://api." + type_git + "/repos/" + user + "/" +
                 repo + "/languages")
    print("Analyzing repository languages...\n")
    # Get content
    r = requests.get(repo_url)
    # Decode JSON response into a Python dict:
    content = r.json()
    #-- Get used languages and their quantity
    for key in content.keys():
        print(key + ": " + str(content[key]))
        if key == 'Python':
            python_leng = True
            python_quantity = content[key]
        total_elem += content[key]
    #-- Check if python is 50%
    if python_leng == True:
        amount = total_elem/2
        #print('The 50% is: ' + str(amount))
        if python_quantity >= amount:
            print('\nPython 50% OK\n')
            #-- Clone the repository
            run_url(url)
        else:
            print('\nThe repository does not contain 50% of the Python.\n')


def run_url(url):
    command_line = "git clone " + url
    print('Run url...')
    #print(command_line)
    #-- List everything and separate
    args = shlex.split(command_line)
    #-- Run in the shell the command_line
    subprocess.call(args)
    get_directory(url)

def request_user():
    print("Enter the Github User: ")
    user = input()
    print(user)
    #-- Check USER
    #-- Run USER
    run_user(user)

def run_user(user):
    #-- Create the url of the api
    user_url = ("https://api.github.com/users/"  + user)
    print(user_url)
    print("Analyzing user...\n")
    try:
        #-- Extract headers
        headers = requests.get(user_url)
        #-- Decode JSON response into a Python dict:
        content = headers.json()
        #-- Get repository url
        repo_url = content["repos_url"]
    except KeyError:
        sys.exit('An unavailable user has been entered')
    print("Analyzing repositories...\n")
    #-- Extract repository names
    names = requests.get(repo_url)
    #-- Decode JSON response into a Python dict:
    content = names.json()
    #-- Show repository names
    for repository in content:
        print('\nRepository: ' + str(repository["name"]))
        url = ("https://github.com/" + user + "/" + repository["name"])
        check_lenguage(url, 'https', 'github.com', user, repository["name"])


def get_directory(url):
    #-- Get values rom the url
    values = url.split('/')
    #-- Last item in the list
    name_directory = values[-1]
    #-- Remove extension .git
    if ('.git' in str(name_directory)):
        name_directory = name_directory[0:-4]
    print("The directory is: " + name_directory)
    get_path(name_directory)


def get_path(name_directory):

    #wd = os.getcwd()
    #print("working directory is ", wd)
    absFilePath = os.path.abspath(name_directory)
    print("This script absolute path is ", absFilePath)
    #path, filename = os.path.split(absFilePath)
    #print("Script file path is {}, filename is {}".format(path, filename))
    return (absFilePath)

if __name__ == '__main__':
    show_menu()
