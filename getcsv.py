""""
PROGRAM TO OBTAIN SUMMARIES FROM CSV
"""

import csv
import os


def create_csv(myDataList):
    """Scrolls through the list looking for different .py files. """
    # Remove header
    list = myDataList[1:]
    myDataCsv = ''
    for i in list:
        if (myDataCsv == '') or (i[1] != myDataCsv[1][1]):
            myDataCsv = [['Repository', 'File Name', 'Class', 'Start Line',
                          'End Line', 'Displacement', 'Level']]

        myDataCsv.append(i)
        file_name = myDataCsv[1][1]
        write_FileCsv(myDataCsv, file_name)


def write_FileCsv(myDataCsv, file_name, file_csv=""):
    """ Create and add data in the .csv file. """
    # Get current path
    wd = os.getcwd()
    # Create new folder
    try:
        os.mkdir(wd + "/DATA_CSV")
    except FileExistsError:
        pass
    file_name = file_name.split('.py')[0] + '.csv'
    path_file = wd + '/DATA_CSV/' + file_name
    # Create a csv with each file name
    if not file_csv:
        file_csv = open(path_file, 'w')
        with file_csv:
            writer = csv.writer(file_csv)
            writer.writerows(myDataCsv)
    else:
        with open(path_file, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(myDataCsv)


def read_FileCsv(file_csv=""):
    """ Read data.csv and create a list to iterate. """
    with open('data.csv', newline='') as File:
        reader = csv.reader(File)
        myDataList = []
        for row in reader:
            myDataList.append(row)

        create_csv(myDataList)


if __name__ == '__main__':
    read_FileCsv()
