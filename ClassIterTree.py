#-- CLASS PROGRAM TO ITERATE ON THE TREE

import ast
import csv
import json
import levels

""" Class to iterate tree. """
class IterTree():

    """ Class constructor. """
    def __init__(self, tree, attrib, file, repo):
        self.tree = tree
        self.attrib = attrib
        self.name = file
        self.repo = repo
        self.locate_Tree()


    """ Method iterating on the tree. """
    def locate_Tree(self):
        for self.node in ast.walk(self.tree):
            #-- Find attributes
            if type(self.node) == eval(self.attrib):
                self.level = ''
                self.clase = ''
                levels.levels(self)
                self.assign_List()
                self.assign_Dict()
                self.read_FileJson()


    """ Create object list. """
    def assign_List(self):
        if (self.clase != '') and (self.level != ''):
            self.list = [self.repo, self.name, self.clase, self.node.lineno,
                        self.node.end_lineno, self.node.col_offset, self.level]
            #print(self.list)
            self.add_Csv()


    #-- Csv header
    myDataCsv =[['Repository', 'File Name', 'Class', 'Start Line','End Line',
                'Displacement', 'Level']]


    """ Add object list to CSV. """
    def add_Csv(self):
        self.myDataCsv.append(self.list)
        #print(self.myDataList)
        self.read_FileCsv()


    """ Create and add data in the .csv file. """
    def read_FileCsv(self, file_csv = ""):
        if not file_csv:
            file_csv = open('data.csv', 'w')
            with file_csv:
                writer = csv.writer(file_csv)
                writer.writerows(self.myDataCsv)
        else:
            with open(r'data.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(self.myDataCsv)


    #-- Create json dictionary
    myDataJson = {}


    """ Create object dictionary. """
    def assign_Dict(self):
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


    """ Create and add data in the .json file. """
    def read_FileJson(self):
        with open('data.json', 'w') as file:
            json.dump(self.myDataJson, file, indent=4)
