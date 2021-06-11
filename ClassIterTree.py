#-- CLASS PROGRAM TO ITERATE ON THE TREE

import ast
import csv
import json
import levels


class IterTree():
    """ Class to iterate tree. """

    #-- CSV header
    myDataCsv =[['Repository', 'File Name', 'Class', 'Start Line','End Line',
                'Displacement', 'Level']]

    # JSON dictionary
    myDataJson = {}
    
    def __init__(self, tree, attrib, file, repo):
        """ Class constructor. """
        self.tree = tree
        self.attrib = attrib
        self.name = file
        self.repo = repo
        self.locate_Tree()

    def locate_Tree(self):
        """ Method iterating on the tree. """
        for self.node in ast.walk(self.tree):
            #-- Find attributes
            if type(self.node) == eval(self.attrib):
                self.level = ''
                self.clase = ''
                levels.levels(self)
                self.assign_List()
                self.assign_Dict()
                self.read_FileJson()


    def assign_List(self):
        """ Create object list. """
        if (self.clase != '') and (self.level != ''):
            self.list = [self.repo, self.name, self.clase, self.node.lineno,
                        self.node.end_lineno, self.node.col_offset, self.level]
            #print(self.list)
            self.add_Csv()

    def add_Csv(self):
        """ Add object list to CSV. """
        self.myDataCsv.append(self.list)
        #print(self.myDataList)
        self.read_FileCsv()

    def read_FileCsv(self, file_csv = ""):
        """ Create and add data in the .csv file. """
        if not file_csv:
            file_csv = open('data.csv', 'w')
            with file_csv:
                writer = csv.writer(file_csv)
                writer.writerows(self.myDataCsv)
        else:
            with open(r'data.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(self.myDataCsv)

    def assign_Dict(self):
        """ Create object dictionary. """
        if (self.clase != '') and (self.level != ''):
            if not self.repo in self.myDataJson:
                self.myDataJson[self.repo] = {}

            if not self.name in self.myDataJson[self.repo]:
                self.myDataJson[self.repo][self.name] = []

            self.myDataJson[self.repo][self.name].append({
                'Class'       : str(self.clase),
                'Start Line'  : str(self.node.lineno),
                'End Line'    : str(self.node.end_lineno),
                'Displacement': str(self.node.col_offset),
                'Level'       : str(self.level)})

    def read_FileJson(self):
        """ Create and add data in the .json file. """
        with open('data.json', 'w') as file:
            json.dump(self.myDataJson, file, indent=4)
