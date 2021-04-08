import sys
import shlex, subprocess
import os
import json
import requests

def request_url():
    print("Enter the Github url: ")
    url = input()
    values = url.split("/")
    protocol = values[0].split(':')[0]
    type_git = values[2]
    user = values[3]
    repo = values[4][0:-4]
    #-- Check url

    #-- Check languaje
    check_lenguage(url, protocol, type_git, user, repo)


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

def get_directory(url):
    #-- Get values rom the url
    values = url.split('/')
    #-- Last item in the list
    name_item = values[-1]
    #-- Remove extension .git
    name_directory = name_item[0:-4]
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
    request_url()
