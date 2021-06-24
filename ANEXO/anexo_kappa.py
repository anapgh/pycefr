"""
PROGRAMME FOR CALCULATING THE KAPPA COEFFICIENT.
"""

import csv
import os
import sys
from sklearn.metrics import cohen_kappa_score
import matplotlib.pyplot as plt

# List of annex levels
annex1Level = []
annex2Level = []

# List arguments shell
arguments = []

# List FILES
list_files = []


def get_path():
    """ Get the file path."""
    path = os.getcwd()
    for i in range(0, len(arguments)):
        # Check if it is a csv file
        print(arguments[i])
        if not arguments[i].endswith('.csv'):
            name = arguments[i].split('.')[0]
            name_file = name + '.csv'
            list_files.append(name_file)
            name_new = path + "/" + name_file
            name_old = path + "/" + arguments[i]
            name_new = name_new.encode('utf-8')
            # Change the file name
            os.rename(name_old, name_new)
        else:
            list_files.append(arguments[i])
    read_files()


def read_files():
    """ Read files. """
    for file in list_files:
        index = list_files.index(file)
        with open(str(file), newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if index == 0:
                    annex1Level.append(row[2])
                else:
                    annex2Level.append(row[2])
    show_list(annex1Level, annex2Level)


def show_list(annex1Level, annex2Level):
    """ Delete the first two indexes."""
    annex1Level = annex1Level[2:]
    annex2Level = annex2Level[2:]
    print('Anexo 1: ' + str(annex1Level))
    print('Anexo 2: ' + str(annex2Level))


def get_ckappa():
    """ Calculating the kappa coefficient. """
    print(cohen_kappa_score(annex1Level, annex2Level))


# Show plot
plt.plot(annex1Level)


if __name__ == '__main__':
    # Get ARGUMENTS
    try:
        FILE1 = sys.argv[1]
        FILE2 = sys.argv[2]
        arguments.append(FILE1)
        arguments.append(FILE2)
    except (IndexError, ValueError):
        sys.exit('Usage: python3 file.py file file')
    get_path()
    get_ckappa()
